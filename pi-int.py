k=1

s=0

for i in range(10000000):
   if i% 2 == 0:
     s+=4/k
   else:
     s-=4/k

   k+=2

print(s)


#0.x secs termux
#10 secs webvm
#7 seconds alpine x 64 vm on phone
#20 secs copy x86


