list = [1,2,3,4,5]
for i in list:
    if i == 4:
        print(i)
    else:
        print("Breaking at", i)
        continue
print("Loop ended")