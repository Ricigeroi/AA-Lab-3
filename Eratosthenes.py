import time
import matplotlib.pyplot as plt

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


number = []
for i in range(5000, 70001, 2500):
    number.append(i)

print(number)

g1 = []
g2 = []
g3 = []
g4 = []
g5 = []

for item in number:
    g1.append(exec_time(algorithm_1, item))
    g2.append(exec_time(algorithm_2, item))
    g3.append(exec_time(algorithm_3, item))
    g4.append(exec_time(algorithm_4, item))
    g5.append(exec_time(algorithm_5, item))



print("Algorithm 1: ", g1, "seconds")
print("Algorithm 2: ", g2, "seconds")
print("Algorithm 3: ", g3, "seconds")
print("Algorithm 4: ", g4, "seconds")
print("Algorithm 5: ", g5, "seconds")

# Graph
# define grid of plots

#define grid of plots
fig, axs = plt.subplots(nrows=2, ncols=3)

#add title
fig.suptitle('Empirical analysis of algorithms for obtaining Eratosthenes Sieve')

axs[0][0].plot(number, g1)
axs[0][0].set_title('Algorithm 1')
axs[0][0].set_xlabel('Number')
axs[0][0].set_ylabel('Time')
axs[0][0].grid(True)

axs[0][1].plot(number, g2)
axs[0][1].set_title('Algorithm 2')
axs[0][1].set_xlabel('Number')
axs[0][1].set_ylabel('Time')
axs[0][1].grid(True)

axs[0][2].plot(number, g3)
axs[0][2].set_title('Algorithm 3')
axs[0][2].set_xlabel('Number')
axs[0][2].set_ylabel('Time')
axs[0][2].grid(True)

axs[1][0].plot(number, g4)
axs[1][0].set_title('Algorithm 4')
axs[1][0].set_xlabel('Number')
axs[1][0].set_ylabel('Time')
axs[1][0].grid(True)

axs[1][1].plot(number, g5)
axs[1][1].set_title('Algorithm 5')
axs[1][1].set_xlabel('Number')
axs[1][1].set_ylabel('Time')
axs[1][1].grid(True)

axs[1][2].remove()





fig1 = plt.figure()
plt.grid()
plt.plot(number, g1)
plt.plot(number, g2)
plt.plot(number, g3)
plt.plot(number, g4)
plt.plot(number, g5)
plt.legend(['Algorithm 1', 'Algorithm 2', 'Algorithm 3', 'Algorithm 4', 'Algorithm 5'])
plt.title('Empirical analysis of algorithms for obtaining Eratosthenes Sieve')
plt.xlabel('n')
plt.ylabel('Execution time, sec')
plt.show()

