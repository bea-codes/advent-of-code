""" 
ADVENT OF CODE - 2023
DAY 01
"""

input = "./input.txt"
TOTAL_SUM = 0


def find_calibration_value(line):
    all_numbers = []
    for char in line:
        try:
            isNumber = int(char)
            all_numbers.append(isNumber)
        except:
            pass
    
    test = [str(all_numbers[0]), str(all_numbers[-1])]
    calibration_value = ''.join(test)
    return calibration_value

def sum_of_values(file):
    total_sum = 0
    for line in file:
        total_sum = total_sum + int(find_calibration_value(line))
    return total_sum


with open("./input.txt", "r") as file:
    TOTAL_SUM = sum_of_values(file)
    print(f"Total sum of calibration values: {TOTAL_SUM}")
