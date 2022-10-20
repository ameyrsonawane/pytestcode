
a = int(input('enter:'))
i = 2
if a <= 1:
    print("Not prime number")
else:
    while i <= a:
        if int(a % i) == 0:
            print(f'{a} is not a prime number')
            break
        i += 1
    else:
        print(f'{a} is a prime number')

