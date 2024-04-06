from array import array
from random import random

FILE_NAME = 'floats.bin'

print("Generating numbers...")
floats_generated = array('d', (random() for i in range(10**7)))
last_item_generated = floats_generated[-1]
print(f"{last_item_generated=}")

print("Writing to file...")
fp = open(FILE_NAME, 'wb')
floats_generated.tofile(fp)
fp.close()
print("Done")

fp = open(FILE_NAME, 'rb')
print("Reading from file...")
floats_read = array('d')
floats_read.fromfile(fp, 10**7)
print("Done")

print("Asserting the last item is intact")
last_item_read = floats_read[-1]
assert last_item_read == last_item_generated

