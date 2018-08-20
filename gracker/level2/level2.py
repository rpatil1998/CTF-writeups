#In this question the zero in not decrypting his secret password infact he is encrypting ours and then 
#comparing so what we have to do is to find out the xorkey by reading the value of register 0x600e80 and then esi
# to get the encrypted value of secret_message,after setting break point before strcmp. 
#Then a simple pyhton script will help us!!!




string1=")q6\036(2\036\065)p2\036)u\"*r3\036'q--q6(/&\036,r"
xorkey="41"
string2=""
for i in range(0,len(string1)):
	string2=string2+chr(ord(string1[i])^int(xorkey,16))


print(string2)	
#h0w_is_th1s_h4ck3r_f0ll0wing_m3
