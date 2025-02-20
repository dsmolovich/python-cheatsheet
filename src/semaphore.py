import threading
import time
import random

# Create a semaphore with a count of 3.  This means up to 3 threads
# can access the shared resource at any given time.
semaphore = threading.Semaphore(2)

# Shared resource (a list in this example)
shared_resource = []

def worker_thread(thread_id):
    while True:  # Simulate doing work repeatedly
        # Acquire the semaphore. If the count is greater than 0, the thread
        # proceeds. If the count is 0, the thread blocks until another thread
        # releases the semaphore.
        semaphore.acquire()
        try:
            # Critical section: Access and modify the shared resource
            print(f"Thread {thread_id} acquired the semaphore. Accessing shared resource...")
            time.sleep(random.uniform(0.5, 1.5)) # Simulate some work

            item = random.randint(1, 100) #Generate a random number
            shared_resource.append(item)
            print(f"Thread {thread_id} added {item} to the shared resource: {shared_resource}")
            time.sleep(random.uniform(0.2, 0.8)) # Simulate more work

        finally:
            # VERY IMPORTANT: Release the semaphore in a 'finally' block to ensure
            # it's always released, even if exceptions occur in the critical section.
            semaphore.release()
            print(f"Thread {thread_id} released the semaphore.")
            time.sleep(random.uniform(1, 2))  # Simulate doing other work outside the critical section


# Create multiple worker threads
threads = []
for i in range(5):  # Create 5 worker threads
    thread = threading.Thread(target=worker_thread, args=(i,))
    threads.append(thread)
    thread.start()

# Keep the main thread alive (optional)
for thread in threads:
    thread.join()  # Wait for all threads to finish (if you don't want the main thread to exit prematurely)

print("All threads finished (or main thread exited).")