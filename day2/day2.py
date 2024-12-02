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
def find_safe_reports(reports_list):
    safe_reports_count = 0
    second_chance_lists = []
    for report in reports_list:
        if check_rule_1(report) and check_rule_2(report):
            safe_reports_count += 1
        else:
            second_chance_lists.append(report)
    return safe_reports_count, second_chance_lists

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
    reports_list = make_list()
    safe_reports_count, second_chance_lists = find_safe_reports(reports_list)
    second_chance_safe_reports_count = run_problem_dampener(second_chance_lists)
    total_safe_reports = safe_reports_count + second_chance_safe_reports_count
    print(f'The number of safe reports is {total_safe_reports}')

main()