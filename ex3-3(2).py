dayup, dayfactor = 1.0, 0.01
for i in range(365):
    if i % 15 in [3,4,5,6,10,11,12,13]:
        dayup = dayup * (1 + dayfactor)
    print("{}：天的能力{}".format(i+1,dayup))
print("连续学习3天能力值不变，从第4天至第7天和第10天至第13天每天能力增长为前一天1%，每15天休息一天的力量: {:.2f}.".format(dayup))
