import sys
import datetime

inp=open(sys.argv[1],'r')
intro=[]
outro=[]
sum=[0 for i in range(1440)]
final=[]
sw=0
for i in inp: # creating list with times of customers entering and exiting
    i=i.replace(':',' ').strip().split()
    intro.append(int(i[0])*60+int(i[1]))
    outro.append(int(i[2])*60+int(i[3])-1)
for i in range(1440): # creating a list for every minute, lol
    for j in range(len(intro)):
        if intro[j]<=i and outro[j]>=i:
        	sum[i]=sum[i]+1
i=0
while i<1440:
    if sum[i]==max(sum): # start of the segment marking
        if sw==0: final.append(i)
        sw=1
        i=i+1
        continue
    if sw==1:
        final.append(i)
    sw=0 # end of the segment marking
    i=i+1
for i in final:
    output=str(i//60)+':'+str(i%60)
    if output[-1]=='0' and output[-2]==':': output=output+'0'
    print (output, end='')
    if final.index(i)%2==0: print (' ',end='')
    if final.index(i)%2==1: print ('')
