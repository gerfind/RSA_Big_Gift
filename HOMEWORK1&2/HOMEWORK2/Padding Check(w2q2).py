def check_padding(s: bytes):
	padding = s[-s[-1]:]
	for i in padding:
		if not i == len(padding):
			return False
	return True
 
print(check_padding(b'ICE ICE BABY\x04\x04\x04\x04'))
print(check_padding(b'ICE ICE BABY\x05\x05\x05\x05'))
print(check_padding(b'ICE ICE BABY\x01\x02\x03\x04'))
print(check_padding(b'ICE ICE BABY'))