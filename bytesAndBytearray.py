blist = [1, 2, 3, 255]
the_bytes = bytes(blist)

print(the_bytes)

the_byte_array = bytearray(blist)
print(the_byte_array)

# the_bytes[1] = 127
the_byte_array[1] = 127

the_bytes_0_255 = bytes(range(0, 256))
the_byte_array_0_255 = bytearray(range(0, 256))

print(the_bytes_0_255)

print(2*'\n')

print(the_bytes_0_255)
