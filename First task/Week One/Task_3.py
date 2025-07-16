deposit = int(input("Сумма первоначального депозита:"))

depositOneYear = deposit * 1.04
depositTwoYear = depositOneYear * 1.04
depositThreeYear = depositTwoYear * 1.04

print("В конце первого года сумма на депозите составит:", depositOneYear)
print("В конце второго года сумма на депозите составит:", depositTwoYear)
print("В конце третьего года сумма на депозите составит:%.2f"  % depositThreeYear)