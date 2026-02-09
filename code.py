def validUtf8(data):
    remaining = 0
    for num in data:
        num = num & 0xFF  # Ensure only the least significant 8 bits are considered
        if remaining == 0:
            if (num >> 7) == 0:  # 1-byte character
                remaining = 0
            elif (num >> 5) == 0b110:  # 2-byte character
                remaining = 1
            elif (num >> 4) == 0b1110:  # 3-byte character
                remaining = 2
            elif (num >> 3) == 0b11110:  # 4-byte character
          