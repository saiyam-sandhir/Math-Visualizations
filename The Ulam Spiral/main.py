import turtle

# Create Python Turtle screen
screen = turtle.Screen()
screen.title("Ulam Spiral")
screen.bgcolor("black")

# Create Spiral drawing turtle
tur = turtle.Turtle()
tur.shape("circle")
tur.color("white")
tur.penup()
tur.shapesize(0.1, 0.1, 1)
tur.speed(0)

# My algorithm to find primes
primes = []
def check_if_prime(num):
    if num == 1:
        return False
    if num == 2:
        primes.append(num)
        return True
    else:
        for i in primes:
            if num % i == 0:
                return False
        primes.append(num)
        return True

#----------Sieve of Eratosthenes algorithm to find the primes----------#
# def sieve_of_eratosthenes(n):
#     is_prime = [True] * (n+1)
#     is_prime[0] = is_prime[1] = False
#     for i in range(2, int(n**0.5)+1):
#         if is_prime[i]:
#             for j in range(i*i, n+1, i):
#                 is_prime[j] = False
#     return [i for i in range(2, n+1) if is_prime[i]]

# primes = sieve_of_eratosthenes(203**2)

# Draw the spiral
moves = 0
num = 0
for i in range(203):
    if i % 2 == 0:
        moves += 1
    for j in range(moves):
        num += 1
        if check_if_prime(num):
            tur.color("red")
        else:
            tur.color("white")
        tur.stamp()
        tur.forward(4)

    tur.left(90)

turtle.done()