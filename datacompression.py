# import zlib
# s = b"i am anjai aryal"
# len(s)
# print(len(s))

import zlib

s = b" i am a student of bicte"

original_length = len(s)
print("Original length", original_length)

compressed_data = zlib.compress(s)
compressed_length = len(compressed_data)
print("compressed length:", compressed_length)

decompressed_data = zlib.decompress(compressed_data)
print("decompressed data:",decompressed_data.decode("utf-8"))

