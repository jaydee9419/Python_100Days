def prime_checker(number):
    is_prime = True
    for i in range (2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("This is prime number") 
    else:
        print("Not prime number")  
            
    
prime_checker(11)
    
    