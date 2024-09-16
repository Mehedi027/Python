def prime_checker(number):
    if number < 2:
        print("It's not a prime number.")
        return
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")

n = int(input())
prime_checker(number=n)