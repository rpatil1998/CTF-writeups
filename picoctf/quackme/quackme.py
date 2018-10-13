string1="You have now entered the Duck Web, and you're in for a honkin'"
string2=")O+50Q[K]+P]YR]	"
string3=""
for i in range(0,len(string2)):
	string3=string3+chr(ord(string1[i])^ord(string2[i]))


print(string3)	
#h0w_is_th1s_h4ck3r_f0ll0wing_m3	