import struct

f = open("2.bmp", "rb")
ftype = f.read(2)
print(ftype)

buf = f.read(4)
size = struct.unpack('i', buf)
print(size)

buf = f.read(4)
reserv = struct.unpack('i', buf)
print(reserv)

buf = f.read(4)
offset = struct.unpack('i', buf)
print(offset)

buf = f.read(4)
head_size = struct.unpack('i', buf)
print(head_size)

buf = f.read(4)
width = struct.unpack('i', buf)
print(width)

buf = f.read(4)
height = struct.unpack('i', buf)
print(height)

buf = f.read(4*7)

buf = f.read(3)
pixel = struct.unpack('BBB', buf)
print(pixel)

