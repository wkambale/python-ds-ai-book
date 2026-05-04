# Imagine we have a list of daily rainfall amounts in millimeters
rainfall_mm = [10.2, 0.0, 5.5, 25.1, 1.3, 0.0, 8.8]
total_rainfall = 0.0

# For each 'daily_amount' in our 'rainfall_mm' list...
for daily_amount in rainfall_mm:
    # ...add it to our running total
    total_rainfall = total_rainfall + daily_amount

print(f"The total rainfall for the week was {total_rainfall:.2f} mm.")