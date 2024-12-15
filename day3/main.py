import re

# Read input from a file
with open('day3/input1.txt', 'r') as file:
    input_text = file.read()

# Define a regex pattern to match only mul(num1,num2)
pattern = r"mul\((\d+),(\d+)\)"

# Find all matches in the input text
matches = re.findall(pattern, input_text)

# Perform multiplication and calculate the sum
multiplications = [int(num1) * int(num2) for num1, num2 in matches]
total_sum = sum(multiplications)

# Output the results
print("Matches and results:", [(int(num1), int(num2), int(num1) * int(num2)) for num1, num2 in matches])
print("Sum of multiplications:", total_sum)

### part 2

# Read input from a file
with open('day3/input2.txt', 'r') as file:
    input_text = file.read()

# Define regex patterns
mul_pattern = r"mul\((\d+),(\d+)\)"  # Matches mul(num1,num2)
control_pattern = r"(do\(\)|don't\(\))"  # Matches do() or don't()

# Initialize variables
enabled = True  # mul instructions are enabled by default
total_sum = 0  # Sum of valid multiplications

# Process the input text
for match in re.finditer(f"{control_pattern}|{mul_pattern}", input_text):
    if match.group(1):  # If it's a control instruction (do() or don't())
        if match.group(1) == "do()":
            enabled = True
        elif match.group(1) == "don't()":
            enabled = False
    elif match.group(2):  # If it's a mul(num1,num2)
        if enabled:  # Only process if enabled
            num1, num2 = int(match.group(2)), int(match.group(3))
            total_sum += num1 * num2

# Output the result
print("Sum of valid multiplications:", total_sum)