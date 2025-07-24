nums = []
while True:
    n = input("Число (Enter - стоп): ")
    if not n: break
    nums.append(float(n))

avg = sum(nums)/len(nums)
print(f"\nСреднее: {avg:.1f}")

print("Ниже среднего:", [x for x in nums if x < avg])
print("Равны среднему:", [x for x in nums if x == avg]) 
print("Выше среднего:", [x for x in nums if x > avg])