import time

try:
    import numpy as np
except ImportError:
    np = None

# (a) Measuring Python List Appending
start_time = time.time()
py_list = []
for i in range(100000):
    py_list.append(i)
end_time = time.time()
list_duration = end_time - start_time
print(f"Python List append time: {list_duration:.6f} seconds")

# (b) Measuring NumPy Array Creation
start_time = time.time()
np_array = np.arange(100000)
end_time = time.time()
numpy_duration = end_time - start_time
print(f"NumPy Array creation time: {numpy_duration:.6f} seconds")

print(f"NumPy was roughly {list_duration / numpy_duration:.1f}x faster.")