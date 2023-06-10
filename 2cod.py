import random
import time
from multiprocessing import Pool
def sum_random_numbers(n):
    total_sum = 0
    for i in range(n):
        total_sum += random.randint(1, 100)
    return total_sum
def sequential_execution():
    start_time = time.time()
    result = sum_random_numbers(10000000)# Генерация случайные чисела
    end_time = time.time()
    print(f"Результаты последовательного: {result}")
    print(f"Результаты последовательного time: {end_time - start_time}s")
def parallel_execution():
    start_time = time.time()
    with Pool(processes=4) as pool:
        result = pool.map(sum_random_numbers, [2500000] * 4)# Генерация случайные чисела
    end_time = time.time()
    print(f"Результаты параллельного: {sum(result)}")
    print(f"Результаты параллельного time: {end_time - start_time}s")
if __name__ == '__main__':
    sequential_execution()
    parallel_execution()
