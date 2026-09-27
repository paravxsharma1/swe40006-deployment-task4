import time
from datetime import datetime

print("SWE40006 Task 4.4 - Non-web CLI application")
print("Student: Parav Sharma (105321434)")
print("-" * 50)

data = [12, 45, 7, 89, 23, 56, 34, 91, 18, 67]

print(f"Processing dataset: {data}")
time.sleep(1)

total = sum(data)
average = total / len(data)
maximum = max(data)
minimum = min(data)

print(f"Sum: {total}")
print(f"Average: {average:.2f}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Timestamp: {datetime.now()}")
print("-" * 50)
print("Processing complete. Container will now exit.")