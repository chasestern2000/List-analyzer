# Chapter 7 homework
# Making a main function
def main():
    # Opens the file
    infile = open('CH7numbers.txt', 'r')

    # Reading lines and converting the numbers as integers (Fixes max and min)
    # Sorting the file in ascending order

    numbers = infile.readlines()
    numbers_int = [int(item) for item in numbers]
    numbers.sort()

    infile.close()

    # Variable for total sum
    sumit = 0

    # Variable for average
    avg = 0


    # Loop for all variables
    for index in range(len(numbers)):
        # Makes the numbers into a list
        numbers[index] = int(numbers[index])
        # Sum, number of numbers, and average
        sumit += int(numbers[index])
        total_numbers = len(numbers)
        avg = sumit/total_numbers
        # Finds maxmimum and minimum
        low = min(numbers_int)
        high = max(numbers_int)

    # Prints data
    print('Statistics for the following numbers in ascending order:', sorted(numbers))
    print()
    print('Amount of numbers in the list:', total_numbers)
    print('Sum of all numbers:', sumit)
    print('Average of numbers:', f'{avg:.2f}')
    print('Highest number:', high)
    print('Lowest number:', low)

# Calls main function
if __name__ == '__main__':
    main()
    


