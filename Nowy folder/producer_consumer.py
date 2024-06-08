from threading import Event, Thread
from queue import Queue
import time


total_tickets = 10
customer_queue = Queue()
customers = [("Tomek", 2), ("Adam", 4), ("Robert", 1), ("Karol", 3), ("Ewelina", 1)]


def book_ticket(customer_name, ticket_quantity):
    global total_tickets

    if total_tickets >= ticket_quantity:
        print(
            f"Zamówienie zrealizowane! {customer_name}, kupił/-a {ticket_quantity} biletów!"
        )
    else:
        print("Niestety, nie ma wystarczającej liczby  biletów.")

    print(f"Zostało łącznie {total_tickets} biletów")


def consumer():
    while True:
        next_order = customer_queue.get()
        if not next_order:
            break
        customer_name, ticket_quantity = next_order
        book_ticket(customer_name, ticket_quantity)
        customer_queue.task_done()


def producer():
    for customer in customers:
        print("Do kolejki dołącza klient")
        customer_queue.put(customer)
        time.sleep(2)


producer_thread = Thread(target=producer)
consumer_thread = Thread(target=consumer)

producer_thread.start()
consumer_thread.start()


producer_thread.join()
customer_queue.join()
consumer_thread.join()
