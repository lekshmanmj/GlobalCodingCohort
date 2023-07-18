import time,sys,io
# start = time.time()
out = io.open('sample_out.txt','wb')
temp = []
for each in range(10):
    temp.append(sys.stdin.readline())
    out.write(temp[-1].encode())
sys.stdout.write(str(temp))

# end = time.time()
# print('\n',end-start)