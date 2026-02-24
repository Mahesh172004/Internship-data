def count_to(n):
    numbers=[]
    count = 1
    while count <= n:
        numbers.append(count)
        count += 1
    return numbers
number = int(input("Enter a number: "))
for num in count_to(number):
    print(num)


    #iterato version
    #here it will not give the o/p for larger number as it will not store all the numbers in memory at once