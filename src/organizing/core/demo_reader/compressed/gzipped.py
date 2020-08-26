import gzip
from ..util.writer import main

opener = gzip.open

if __name__ == '__main__':
    main(opener)