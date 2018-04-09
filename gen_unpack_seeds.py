import datetime

from struct import pack

import msgpack


def encode_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return {'__datetime__': True, 'as_str': obj.strftime("%Y%m%dT%H:%M:%S.%f")}
    return obj

samples = [
    [1, 2, 3],
    None,
    5,
    10,
    {'a': 'b'},
    {'a': {'b': {'c': 'd'}}},
    {'data': b'just a bit of binary'},
    {'data': u'unicode specific'},
    {'when': encode_datetime(datetime.datetime.now())},
    True,
    False,
    {},
    (),
    [],
    1.22345,
]


def main():
    for i, s in enumerate(samples):
        packed = msgpack.packb(s)
        redone = msgpack.unpackb(packed, raw=False)
        with open('./unpack/{}'.format(i), 'wb') as f:
            f.write(packed)

    # the first byte is a byte in range
    idx = len(samples)
    for i in range(256):
        idx = len(samples) + i
        with open('./unpack/{}'.format(idx), 'wb') as f:
            f.write(pack("<I", *bytearray([i])))

if __name__ == '__main__':
    main()
