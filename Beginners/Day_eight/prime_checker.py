def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 1:
            is_prime = False
            
                           
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

number = int(input("Enter a number: "))
prime_checker(number)
