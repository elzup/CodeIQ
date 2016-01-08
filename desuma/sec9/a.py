print("".join(chr(i%26+97)if i%8 else chr(i%26+97).upper()for i in range(0,208)))
