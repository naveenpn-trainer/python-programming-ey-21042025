
def calculate_percentage(obtained_marks, total_marks=100):
    print(f"Calculating percentage for the marks:{obtained_marks} with total marks: {total_marks}")
    return (obtained_marks * 100)/total_marks


# Positional argument
# percentage = calculate_percentage(60,100)
# print(f"Percentage= {percentage}")

# Named Arguments
# percentage = calculate_percentage(total_marks=100, obtained_marks=70)
# print("Percentage= {:.2f}".format(percentage))

print(calculate_percentage(80))
print(calculate_percentage(80,200))
