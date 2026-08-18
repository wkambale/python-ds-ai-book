def get_data_recommendation(data_usage_gb: float) -> str:
    """
    Returns a data plan recommendation based on monthly usage.

    Args:
        data_usage_gb: Monthly data usage in gigabytes.

    Returns:
        A string containing the plan recommendation.
    """
    if data_usage_gb <= 0:
        return "Invalid input. Data usage must be a positive number."
    elif data_usage_gb < 2:
        return "The 'Daily Bundles' plan might be most cost-effective for you."
    elif data_usage_gb < 10:
        return "The 'Standard' plan is perfect for you."
    else:
        return "You should consider the 'Unlimited' plan."

def main():
    try:
        user_input = input("Enter your monthly data usage in GB: ")
        data_usage_gb = float(user_input)
        recommendation = get_data_recommendation(data_usage_gb)
        print(f"\nRecommendation: {recommendation}")
    except ValueError:
        print("\n" + "-" * 40)
        print("Error: Please enter a valid number for your data usage.")
        print("Example: 5 or 7.5")
        print("-" * 40)

# Run the program
if __name__ == "__main__":
    main()