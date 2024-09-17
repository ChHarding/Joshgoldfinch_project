# Function to process the inputs
def calculate_output(a, b, c, d):
    # Example: Summing the inputs as the output
    return a + b + c + d

# Main function to get input from the user
def main():
    try:
        # Gather input values from the user
        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))
        c = float(input("Enter the third value: "))
        d = float(input("Enter the fourth value: "))

        # Calculate the result
        result = calculate_output(a, b, c, d)

        # Display the result
        print(f"The calculated output is: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
