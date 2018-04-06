import datetime

import msgpack


msgpack.packb([1, 2, 3], use_bin_type=True)

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
    {'when': encode_datetime(datetime.datetime.now())}
]

def main():
    for i, s in enumerate(samples):
        packed = msgpack.packb(s)
        redone = msgpack.unpackb(packed, raw=False)
        with open('./unpackm/{}'.format(i), 'wb') as f:
            f.write(packed)

if __name__ == '__main__':
    main()
