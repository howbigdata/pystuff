import bz2
from ..util.writer import main

opener = bz2.open

if __name__ == '__main__':
    main(opener)


