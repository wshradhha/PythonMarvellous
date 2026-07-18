import threading
import time

shared_counter = 0

counter_lock = threading.Lock()

def increment_counter(thread_name, cycles):
    global shared_counter
    
    for i in range(cycles):
        # Acquire the lock before modifying the shared variable
        with counter_lock:
            current_value = shared_counter
            time.sleep(0.0001)  # Simulating a small delay/processing time
            shared_counter = current_value + 1
            print(f"[{thread_name}] Updated counter to: {shared_counter}")

def main():
    global shared_counter
    shared_counter = 0
    
    # Define how many times each thread will increment the counter
    increment_cycles = 5
    
    # Create two threads targeting the same shared variable
    thread1 = threading.Thread(target=increment_counter, args=("Thread-A", increment_cycles))
    thread2 = threading.Thread(target=increment_counter, args=("Thread-B", increment_cycles))
    
    # Start both threads
    thread1.start()
    thread2.start()
    
    # Wait for both threads to finish
    thread1.join()
    thread2.join()
    
    print("\n--- Final Results ---")
    print(f"Expected Final Counter Value: {increment_cycles * 2}")
    print(f"Actual Shared Counter Value  : {shared_counter}")

if __name__ == "__main__":
    main()
