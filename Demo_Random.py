import random
from timeit import timeit
import statistics

value = random.randrange(-1,50,2)
#password
#Games
#OTP-
value1 = random.randint(-1,50)
print(value)
print(value1)

#genrating 10,000 random no
data = [random.random() for _ in range(10_000)]

t_mean = [timeit("statistics.mean(data)", number=100, globals=globals())
        for _ in range(30)]

print(t_mean)