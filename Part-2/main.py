import threading
import subprocess

def run_producer():
    subprocess.run(["python", "producer.py"])

def run_consumer():
    subprocess.run(["python", "consumer.py"])

if __name__ == "__main__":
   
    producer_thread = threading.Thread(target=run_producer)
    consumer_thread = threading.Thread(target=run_consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
