user_profile = {
    "user_id": "USR-007",
    "full_name": "Adanna Chukwu",
    "balance_ngn": 65200.5,
    "is_verified": True
}

# Loop through keys only
print("Keys:", end=" ")
for key in user_profile:
    print(key, end=" ")
print()

# Loop through key-value pairs using .items()
print("\nUser Profile")
for key, value in user_profile.items():
    formatted_key = key.replace("_", " ").title()
    print(f"{formatted_key}: {value}")