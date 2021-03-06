def decrypt(input):
    import sys
    characters = []
    for i in range(0, len(input), 2):
        try:
            ascii = int(input[i:i + 2], 16)
            characters.append(chr(ascii))
        except:
            continue

    output = ''.join(characters).strip()
    if len(output) == 0:
        return None

    if sys.version_info[0] >= 3:
        # Python 3 specific definitions
        return output
    else:
        # Python 2 specific definitions
        return output.decode('iso-8859-1')
