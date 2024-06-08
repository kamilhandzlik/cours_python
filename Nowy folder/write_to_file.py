from threading import Thread, Lock
import time


file_name = "output.txt"
# lock = Lock()


def write_to_file(thread_id):
    for _ in range(5):
        # with lock:
        with open(file_name, "a") as file:
            file.write(f"Wątek o id: {thread_id} \n")
            time.sleep(0.1)


def write_to_file_async():
    threads = [Thread(target=write_to_file, args=(i,)) for i in range(1, 5)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


write_to_file_async()
