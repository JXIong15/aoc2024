# https://adventofcode.com/2024/day/3
import re

def make_list():
    with open('input.txt', 'r') as file:
        content = file.read()
        matches = re.findall(r"mul\((\d+),(\d+)\)", content)

    mul_list = [(int(first), int(second)) for first, second in matches]
    return mul_list

# difference between nums is between 1-3
def check_rule_1(report):
    for i in range(len(report)-1):
        # check difference
        difference = abs(report[i] - report[i+1])
        if difference > 3 or difference < 1:
            return False
    return True

# lists are stricting increasing or decreasing
def check_rule_2(report):
    is_decreasing = False
    is_increasing = False
    for i in range(len(report) - 1):
        if report[i] < report[i + 1]:
            is_increasing = True
        elif report[i] > report[i + 1]:
            is_decreasing = True
    return not (is_increasing and is_decreasing)

# for part 1
def calculate_list(mul_list):
    count = 0
    for mul in mul_list:
        count = count + (mul[0]*mul[1])
    return count

# for part 2
def run_problem_dampener(reports_list):
    safe_reports_count = 0
    for report in reports_list:
        for i in range(len(report)):
            # Create a new report with the ith level removed
            modified_report = report[:i] + report[i+1:]
            # Check if the modified report is safe
            if check_rule_1(modified_report) and check_rule_2(modified_report):
                safe_reports_count += 1
                break
    return safe_reports_count


def main():
    mul_list = make_list()
    res = calculate_list(mul_list)
    # second_chance_safe_reports_count = run_problem_dampener(second_chance_lists)
    # total_safe_reports = safe_reports_count + second_chance_safe_reports_count
    print(f'The mul number is {res}')

main()