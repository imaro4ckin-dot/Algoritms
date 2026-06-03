#Q1

def recursive_factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive call
    else:
        return n * recursive_factorial(n - 1)


 # Q2
def loop_fibonacci(n):
    # Base case
    if n <= 0:
        return 0

    elif n == 1:
        return 1

    seies = [0,1]
    # Recursive call
    for i in range(2,n):
        seies.append(seies[i-1] + seies[i-2])

    return seies

 # from the Q3
def countdown(n):
    # Base case: stop when n is less than 1
    if n < 1:
        return

    print(n)
    countdown(n - 1)