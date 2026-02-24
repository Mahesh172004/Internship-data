def count_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
number=int(input("Enter a number to count to: "))        

for number in count_to(number):
    print(number)


    #generator version
    #here it will give the o/p for larger number as it will not store all the numbers in memory at once