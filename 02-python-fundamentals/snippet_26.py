# Find the first number divisible by 7 in a list
numbers = [12, 25, 33, 49, 52, 63, 70]

for num in numbers:
    if num % 7 == 0:
        print(f"Found it! {num} is divisible by 7.")
        break
    print(f"Checking {num}...")

print("\nUsing continue")

# Print only odd numbers, skip even ones
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")