import sys
from organizing.core.demo_reader.multireader import MultiReader


filename = sys.argv[1]
r = MultiReader(filename)
print(r.read())
r.close()