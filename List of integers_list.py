def main():
    # Prompting the user to input a list of integers separated by spaces
    input_list = input("Enter a list of integers separated by spaces: ")

    # Splitting the input string into a list of integers
    integers = [int(x) for x in input_list.split()]

    # Calculating the sum of all integers in the list
    total_sum = sum(integers)

    # Displaying the sum to the user
    print("Sum of the integers:", total_sum)

if __name__ == "__main__":
    main()
1