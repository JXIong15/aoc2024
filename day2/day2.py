# https://adventofcode.com/2024/day/2

def make_list():
    # Open the file for reading
    with open('input.txt', 'r') as file:
        # Initialize empty lists for the two columns
        reports_list = []

        # Read each line in the file
        for line in file:
            reports_list.append(list(map(int, line.split())))
    return reports_list

def check_rule_1(report):
    for i in range(len(report)-1):
        # check difference
        difference = abs(report[i] - report[i+1])
        if difference > 3 or difference < 1:
            return False
    return True

def check_rule_2(report):
    is_decreasing = False
    is_increasing = False
    for i in range(len(report) - 1):
        if report[i] < report[i + 1]:
            is_increasing = True
        elif report[i] > report[i + 1]:
            is_decreasing = True
    return not (is_increasing and is_decreasing)

def find_safe_reports(reports_list):
    safe_reports_count = 0
    for report in reports_list:
        if check_rule_1(report) and check_rule_2(report):
            safe_reports_count += 1
    return safe_reports_count

def main():
    reports_list = make_list()
    safe_reports_count = find_safe_reports(reports_list)
    print(f'The number of safe reports is {safe_reports_count}')

main()