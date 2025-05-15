def calculate_average(input):
    sum_of_numbers = 0
    for e in input:
        # e+=sum_of_numbers
        sum_of_numbers+=e
    average = sum_of_numbers/len(input)
    return average

def main():
    print("Invoking Average Calculation")
    numbers = [10,20,30]
    result = calculate_average(numbers)
    print(f"Average= {result}")

if __name__ == '__main__':
    main()
