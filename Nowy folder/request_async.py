from pprint import pprint
import requests
from threading import Thread
from timeit import timeit


url = "https://swapi.dev/api/planets"


def get_person(id):
    res = requests.get(f"{url}/{id}")
    pprint(res.json())


def get_people_sync():
    for i in range(1, 5):
        get_person


def get_people_async():
    threads = [Thread(target=get_person, args=(i,)) for i in range(1, 5)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


print("Sync time: ", timeit(get_people_sync, number=1))
print("Async time: ", timeit(get_people_async, number=1))
