import time


def algorithm_1(n):
    c = [True] * (n + 1)  # Initialize all values of c to True
    c[1] = False  # Set c[1] to False
    i = 2

    while i <= n:
        if c[i]:
            j = 2 * i
            while j <= n:
                c[j] = False
                j = j + i
        i = i + 1
    return c


def algorithm_2(n):
    c = [True] * (n + 1)  # Initialize all values of c to True
    c[1] = False  # Set c[1] to False
    i = 2

    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j = j + i
        i = i + 1
    return c


def algorithm_3(n):
    c = [True] * (n + 1)  # Initialize all values of c to True
    c[1] = False  # Set c[1] to False
    i = 2

    while i <= n:
        if c[i]:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j = j + 1
        i = i + 1

    return c


def algorithm_4(n):
    c = [True] * (n + 1)  # Initialize all values of c to True
    c[1] = False  # Set c[1] to False
    i = 2

    while i <= n:
        j = 2
        is_prime = True
        while j < i:
            if i % j == 0:
                is_prime = False
                break
            j = j + 1
        if not is_prime:
            c[i] = False
        i = i + 1

    return c


def algorithm_5(n):
    c = [True] * (n + 1)  # Initialize all values of c to True
    c[1] = False  # Set c[1] to False
    i = 2

    while i <= n:
        j = 2
        while j <= i**0.5:
            if i % j == 0:
                c[i] = False
            j = j + 1
        i = i + 1

    return c



def exec_time(function, n):
    start_time = time.time()
    function(n)
    end_time = time.time()
    return end_time - start_time


n = 50000

first = exec_time(algorithm_1, n)
second = exec_time(algorithm_2, n)
third = exec_time(algorithm_3, n)
fourth = exec_time(algorithm_4, n)
fifth = exec_time(algorithm_5, n)

print("Algorithm 1: ", first, "seconds")
print("Algorithm 2: ", second, "seconds")
print("Algorithm 3: ", third, "seconds")
print("Algorithm 4: ", fourth, "seconds")
print("Algorithm 5: ", fifth, "seconds")


