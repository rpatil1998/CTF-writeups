string="zo1b_1e_f0j4l10i"
i=6
for x in string:
	
	if(x!='4' and x!='0' and x!='_' and x!='1' ):
		var=ord(x)
		if(var-i<97):
			var=var-i+26
			print(chr(var))
		else:
			var=var-i
			print(chr(var))	
	else:
		print(x)	
	i=i+1