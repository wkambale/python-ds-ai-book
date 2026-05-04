# range(stop): 0 to stop-1
print("range(5):", list(range(5)))

# range(start, stop): start to stop-1
print("range(2, 7):", list(range(2, 7)))

# range(start, stop, step): with custom step
print("range(0, 10, 2):", list(range(0, 10, 2)))

# Practical example: Print a countdown
print("\nCountdown:")
for i in range(5, 0, -1):
    print(i)
print("Liftoff!")