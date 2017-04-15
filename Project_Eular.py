# 2nd question

value1 = 1
value2 = 2
value3 = 0
sum = 2
count = 3

while (value1+value2<4000000):
    count += 1
    value3 = value1 + value2
    value1 = value2
    value2 = value3
    if(value3%2 == 0):
        sum += value3
print(sum)
