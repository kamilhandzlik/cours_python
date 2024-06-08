import time
import random
from multiprocessing import Pool
from timeit import timeit


def generate_data_chunks():
    data = [random.randint(1, 100) for _ in range(10000)]
    chunk_size = len(data) // 4
    return [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]


def process_data(data_chunk: list[int]):
    result = sum(data_chunk)
    # time.sleep(random.uniform(0.5, 1.5))
    return result


def sync_process():
    data_chunks = generate_data_chunks()
    results = [process_data(chunk) for chunk in data_chunks]
    total_sum = sum(results)
    print(f"Suma liczb to: {total_sum}")


def async_process():
    data_chunks = generate_data_chunks()

    with Pool(processes=4) as pool:
        results = pool.map(process_data, data_chunks)
        total_sum = sum(results)
        print(f"Suma liczb to: {total_sum}")


if __name__ == "__main__":
    print("Sync: ", timeit(sync_process, number=1))
    print("Async: ", timeit(async_process, number=1))
