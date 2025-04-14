import queue
import time

request_queue = queue.Queue()

request_id = 1

def generate_request():
    global request_id
    request = f"Заявка №{request_id}"
    print(f"Створено: {request}")
    request_queue.put(request)
    request_id += 1

def process_request():
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"Обробка: {current_request}")
    else:
        print("Черга пуста.")

def main():
    try:
        while True:
            generate_request()
            time.sleep(1)
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Програма завершена.")

if __name__ == "__main__":
    main()
