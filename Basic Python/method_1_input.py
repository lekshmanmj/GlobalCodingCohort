import time
start = time.time()

temp = []
for each in range(10):
    temp.append(input())
print(temp)

end = time.time()
print(end - start)