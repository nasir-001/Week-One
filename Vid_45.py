# Authur: Nasir Lawal
# Date: 25-Nov-2019

"""
Descrition: Tutorial how to use "Strucks"
"""

from struct import *

# Store as bytes data

packed_data = pack('iif', 6, 19, 4.73)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To get data bytes back to normal 

original_data = unpack('iif', packed_data)

print(original_data)

print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))