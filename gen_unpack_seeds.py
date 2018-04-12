import datetime
import json

from os import listdir
from os.path import isfile, join

from struct import pack

import msgpack

# download a json corpus and convert it to msgpack

def main():
    mypath = './seed_corpus'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for fname in onlyfiles:
        full = '{}/{}'.format(mypath, fname)
        print(full)
        try:
            with open(full, 'rb') as fin:
                old = json.loads(fin.read())
        except:
            continue
        newname = fname.split(".")[0] + '.mpk'
        with open('./packed/{}'.format(newname), 'wb') as fout:
            fout.write(msgpack.packb(old, use_bin_type=True))

if __name__ == '__main__':
    main()
