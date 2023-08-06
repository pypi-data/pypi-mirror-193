"""DDS parsing and handling

You usually just want to use a ``DDSReader`` instance like this::

    for ddspacket in DDSReader('thatfile.dds'):
        print("Packet's timestamp:", ddspacket.timestamp)
        # extract a usable PUS packet using your SCOS instance:
        packet = ddspacket.payload.interprete(my_scos)

"""
import datetime
import struct
import enum
import io
from collections import namedtuple
from pathlib import Path

from .internal import SCOSPUSError
from .pus import PUSPacket


GroundStation = namedtuple('GroundStation', ('id', 'organisation', 'name'))
"""A ground station

DDS headers contain ground stations by ID."""


GROUNDSTATIONS = {gs[0]: GroundStation(*gs)
                  for gs in [
                      (0, '', ''),
                      (0x0d, 'ESA', 'Villafranca2'),
                      (0x15, 'ESA', 'Kourou'),
                      (0x16, '', 'NDIU Lite'),
                      (0x17, 'ESA', 'New Norcia'),
                      (0x18, 'ESA', 'Cebreros'),
                      (0x22, 'NASA', 'Goldstone (old)'),
                      (0x67, 'NASA', 'Goldstone (new)'),
                      (0x23, 'NASA', 'Canberra (old)'),
                      (0x70, 'NASA', 'Canberra (new)'),
                      (0x24, 'NASA', 'Madrid (old)'),
                      (0x6c, 'NASA', 'Madrid (new)'),
                      (0x7f, 'ESA/ESOC', 'Test Station'),
                      (0x82, '', 'NDIU Classic'),
                  ]}
"""The ground stations as defined in RO-MEX-VEX-ESC-IF-5003_DDID_C4"""


class PrematureEndOfFileError(SCOSPUSError):
    """Raised when trying a file is too short to hold the entire DDS packet"""


class TimeQuality(enum.Enum):
    """DDS packet time quality"""
    GOOD = 0
    INACCURATE = 1
    BAD = 2


class DDSPacket:
    """A DDS header with payload"""

    def __init__(self, header):
        self.dds = header
        self.payload = None
        self._timestamp = None
        self.offset = -1
        """Byte offset position of this DDS packet in the source data stream"""

    @property
    def coarse_time(self):
        return struct.unpack(">I", self.dds[0:4])[0]

    @property
    def fine_time(self):
        return struct.unpack(">I", self.dds[4:8])[0]

    @property
    def timestamp(self):
        """The DDS timestamp"""
        if self._timestamp is None:
            self._timestamp = datetime.datetime.fromtimestamp(self.coarse_time,
                                                              tz=datetime.timezone.utc) + \
                              datetime.timedelta(microseconds=self.fine_time)
        return self._timestamp

    @property
    def groundstation(self):
        """The ground station this packet is coming from"""
        gsid = struct.unpack(">H", self.dds[12:14])
        return GROUNDSTATIONS.get(gsid, GroundStation(gsid, '', 'Unknown'))

    @property
    def virtual_channel(self):
        """Virtual Channel ID"""
        return struct.unpack(">H", self.dds[14:16])

    @property
    def SLE(self):
        """The packet's 'SLE' field"""
        return self.dds[16]

    @property
    def time_quality(self):
        """Time quality"""
        return TimeQuality(self.dds[17])

    @property
    def length(self):
        """The packet's 'length' field"""
        return struct.unpack(">I", self.dds[8:12])[0]

    def __len__(self):
        len_ = len(self.dds)
        if self.payload is not None:
            len_ += len(self.payload)
        return len_

    def __lt__(self, other):
        return self.sorting() < other.sorting()

    def sorting(self):
        """Return the list used for sorting"""
        if hasattr(self.payload, 'sorting'):
            return [self.timestamp] + self.payload.sorting()
        return [self.timestamp]

    def __bytes__(self):
        return self.dds + bytes(self.payload)

    @classmethod
    def parse(cls, stream):
        """Parse a DDS packet from the ``stream``

        This will read out only the DDS header. It's up to you to read the
        remaining packet using ``DDSPacket.length`` as an indicator how long
        the following packet is.
        """
        offset = stream.tell()
        blob = stream.read(18)
        if len(blob) < 18:
            raise EOFError()
        packet = DDSPacket(blob)
        packet.offset = offset
        return packet

    def __str__(self):
        return f"<DDS {self.timestamp} payload: {len(self.payload)} bytes>"


class DDSReader:
    """State-aware reader for DDS files

    Must be given a path to a DDS file.

    Can also be used as a context like this::

        with DDSReader('thatfile.dds') as reader:
            packet = reader.read_next()
            # equivalent:
            packet = next(reader)

    If ``next`` or ``read_next`` fail (and raise an exception), you can query
    ``DDSReader.position`` to get the byte offset in the stream where the DDS
    packet started that caused the failure.
    """

    def __init__(self, filepath):
        if isinstance(filepath, str):
            filepath = Path(filepath).expanduser()
        self.filepath = filepath
        self.stream = None
        self.position = -1
        self.raise_errors = True

    def seek(self, position):
        """Jump to this position in the stream"""
        assert self.stream is not None
        self.position = self.stream.seek(position)

    def open(self):
        """Open the source file for reading

        Will open the stream only once"""
        if self.stream is None:
            self.stream = open(self.filepath, 'rb')
            self.position = 0

    def close(self):
        """Close the source file"""
        if self.stream is not None:
            self.stream.close()
        self.stream = None
        self.position = -1

    def __enter__(self):
        if self.stream is None:
            self.open()
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def read_next(self):
        """Read the next packet from the stream

        Will skip over initial stretches of ``0`` bytes.

        Will return ``None`` when the end of the stream is reached.
        """
        assert self.stream is not None
        # skip over lengths of zeroes
        while True:
            try:
                peeked = self.stream.peek(1)
            except EOFError:
                break
            zeroes = 0
            for char in peeked:
                if char != 0:
                    break
                zeroes += 1
            if zeroes == 0:
                break
            self.stream.read(zeroes)
            self.position = self.stream.tell()

        try:
            self.position = self.stream.tell()
            ddspacket = DDSPacket.parse(self.stream)
        except EOFError:
            return None
        try:
            self.position = self.stream.tell()
            blob = self.stream.read(ddspacket.length)
        except EOFError:
            return None

        if len(blob) < ddspacket.length:
            raise PrematureEndOfFileError()

        try:
            ddspacket.payload = PUSPacket.parse(io.BytesIO(blob))
        except (ValueError,) as exc:
            if self.raise_errors:
                raise RuntimeError(f"Failed to parse at {self.position}: {exc}") from exc
            ddspacket = None

        return ddspacket

    def __next__(self):
        if self.stream is None:
            self.open()
        packet = self.read_next()
        if packet is None:
            raise StopIteration()
        return packet

    def __iter__(self):
        if self.stream is None:
            self.open()
        return self


def read_from_dds(filepath):
    """Read all interpreted DDS packets from the given dds file

    A DDS packet is the DDS packet header and the PUS packet.

    ``filepath`` is the location of a ``.dds`` file,
    """
    with DDSReader(filepath) as reader:
        yield from reader
