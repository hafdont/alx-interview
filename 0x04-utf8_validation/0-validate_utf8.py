#!/usr/bin/python3

def validUTF8(data):
    """
    Determine if a given det represents a valid UTF_8 encoding.


    Args:
    data (list): A list of integers representing the data bytes.


    Retunrs:
    bool: True if data is a valid UTF-8 encoding, else fAlse.
    """

    num_bytes = 0

    mask1 = 1 << 7 
    mask2 = 1 << 6


    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes> 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
