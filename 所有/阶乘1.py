def jiecheng(numbers):
    sum = 0
    while numbers>0:
        if numbers > 0:

            sum = sum + numbers ** 2
            numbers = numbers - 1
    return sum


print(jiecheng(3))

