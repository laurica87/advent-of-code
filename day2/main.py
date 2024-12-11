with open('day2/input.txt', 'r') as file:
    # lines = []
    # for line in file:
    #     lines.append([list(map(int, line.split()))])
    reports = [list(map(int, line.split())) for line in file]

def is_safe(report):
    # Check if all elements are increasing or decreasing
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    # Check if differences between adjacent elements are between 1 and 3
    valid_differences = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    
    # Satisfy both conditions
    return (increasing or decreasing) and valid_differences

# Count lines that satisfy the conditions
count = sum(1 for report in reports if is_safe(report))

print("Number of valid lines:", count)

# Function to count lines that satisfy the conditions after removing one element
def count_valid_lines_after_removal(reports):
    valid_count = 0

    for report in reports:
        # Generate all possible lines by removing one element
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]  # Remove the i-th element
            
            # Check if the modified line satisfies the conditions
            if is_safe(modified_report):
                valid_count += 1
                break  # Stop checking once a valid modified line is found

    return valid_count

# Count lines that satisfy the conditions after removing one element
valid_reports_count = count_valid_lines_after_removal(reports)

print("Number of valid lines after removing one element:", valid_reports_count)