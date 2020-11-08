"""Să se calculeze sumele: 	s1=1+2+3+…+n
			s2=1*2+2*3+3*4+…+(n-1)*n
			s3=1+1*2+1*2*3+…+1*2*3*…*n
			s4=12+22+32+…+n2
			s5=1/2+2/3+3/4+…+n/(n+1)
			s6=1+2+22+23+24+…+2n"""
n=eval(input("introduceti n="))
s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
a=1
for i in range(1,n+1):
    s1+=1
    s2+=(i-1)*i
    a*=i
    s3+=a
    s4+=1**2
    s5+=i/(i+1)
    s6+=i*2
print(s1,s2,s3,s4,s5,s6)