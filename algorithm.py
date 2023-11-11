import time
import numpy as np

array = [1, 3, 5, 7]

def algorithm(array):
    n = len(array)
      
    for i in range(n):
        omgedraaid = False  
        for j in range(0, n-i-1):
              if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                omgedraaid = True
        if (omgedraaid == False):
            break
  

if __name__ == "__main__":
    start = time.perf_counter_ns()
    invoer = np.random.randint(0, 200000, 5120)
    algorithm(invoer)
    stop = time.perf_counter_ns()
    
    print(f"Elapsed: {(stop-start) / 1000} µs", "Length:", len(invoer))
#    print("Sorted array:")
#    for i in range(len(invoer)):
#        print("%d" % invoer[i], end=" ")
  