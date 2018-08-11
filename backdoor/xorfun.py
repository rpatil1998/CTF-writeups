from base64 import b64decode as be


#msg and KEY are meaningful english sentences in l33t
#msg2 = msg.replace('_','')#
#KEY = KEY.replace('_','')

#assert  (len(KEY)==7) and KEY.isalnum() and msg2.isalnum()
#assert 'n00bCTF' in msg2
decode=be("DRcGGQBfGw1QEA4XBUURCA0MDQdGBlFTCTo7MxwJUhgAXBQa")

def XOR(A, B):
	return ''.join(chr(ord(A[i])^ord(B[i%len(B)])) for i in range(len(A)))

def dencryption(msg):
	return XOR(decode,msg)

def print_flag(msg):
	print 'CTF{%s}' % msg

def getflag(msg, KEY):
	return (XOR(msg, KEY))	

if __name__ == '__main__':
	msg2="n00bCTF"
	print dencryption(msg2)
	print print_flag(getflag(decode,"hackyou"))

						#DRcGGQBfGw1QEA4XBUURCA0MDQdGBlFTCTo7MxwJUhgAXBQa
	#Decrypt msg2 to get the flag
	
	#then encode it into sha256 online
	