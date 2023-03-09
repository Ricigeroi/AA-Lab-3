

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


n = 10
print(algorithm_1(n))
print(algorithm_2(n))
print(algorithm_3(n))
print(algorithm_4(n))
print(algorithm_5(n))

print(algorithm_1(n) == algorithm_2(n) == algorithm_3(n) == algorithm_4(n) == algorithm_5(n))

