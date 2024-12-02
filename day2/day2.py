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
        safe = False
        is_decreasing = False
        is_increasing = False
        for i in report:
            # check difference
            difference = report[i] - report[i+1]
            if difference < 0:
                difference = difference*-1
            if difference > 3 or difference < 1:
                break



        diff = list1[i] - list2[i]
        if diff < 0:
            diff = diff*-1
        difference += diff
    return difference

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
    difference = find_safe_reports(list1, list2)
    print(f'The distance between both lists is {difference}')
    # similarity = find_similarity_between_lists(list1, list2)
    # print(f'The similarity between both lists is {similarity}')

main()