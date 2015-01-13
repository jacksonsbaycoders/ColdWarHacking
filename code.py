


#code a simple message with a caeser cipher

def encode(letter,shift):
	code = ord(letter)
	code -= 97
	code += shift
	code = code % 26
	code += 97
	return chr(code)


message = "abcdefghijklmnopqrstuvwxyz"
for e in message:
	print encode(e,2),
