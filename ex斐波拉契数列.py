fibs = [0,1]
num = int(input('你想得到多少斐波那契数字？'))
for i in range(num-2):
 fibs.append(fibs[-2]+fibs[-1])
print(fibs)
