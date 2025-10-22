
def print_ladder(height):
    """Prints a ladder pattern of stars up and down to the given height."""
    # Ascending
    for i in range(1, height + 1):
        print("* " * i)
    
    # Descending
    for i in range(height - 1, 0, -1):
        print("* " * i)

def main():
    try:
        height = int(input("Enter maximum height: "))
        if height < 1:
            print("Height must be a positive integer.")
        else:
            print_ladder(height)
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
