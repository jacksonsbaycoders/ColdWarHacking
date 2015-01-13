


#code a simple message with a caeser cipher

def encode(c):
	t = c+1
	t = t%96
	return t


message = "aAzZ"
for e in message:
	print e,ord(e)-97,
