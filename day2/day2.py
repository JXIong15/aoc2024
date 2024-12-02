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

# for part 1
def find_safe_reports(reports_list):
    safe_reports_count = 0
    for report in reports_list:
        rule1_safe = True
        for i in range(len(report)-1):
            # check difference
            difference = abs(report[i] - report[i+1])
            if difference > 3 or difference < 1:
                rule1_safe = False
                break
        # check increase/decrease
        is_decreasing = False
        is_increasing = False
        for i in range(len(report) - 1):
            if report[i] < report[i + 1]:
                is_increasing = True
            elif report[i] > report[i + 1]:
                is_decreasing = True
        rule2_safe = not (is_increasing and is_decreasing)
        if rule1_safe and rule2_safe:
            safe_reports_count += 1
    return safe_reports_count

# for part 2
# def find_similarity_between_lists(list1, list2):
#     similarity = 0
#     for i in range(len(list1)):
#         count = list2.count(list1[i])
#         sim = count*list1[i]
#         similarity += sim
#     return similarity

def main():
    reports_list = make_list()
    safe_reports_count = find_safe_reports(reports_list)
    print(f'The number of safe reports is {safe_reports_count}')
    # similarity = find_similarity_between_lists(list1, list2)
    # print(f'The similarity between both lists is {similarity}')

main()