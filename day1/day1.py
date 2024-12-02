import open

def make_sorted_lists():
    # Open the file for reading
    with open('input.txt', 'r') as file:
        # Initialize empty lists for the two columns
        list1 = []
        list2 = []

        # Read each line in the file
        for line in file:
            # Split the line into two numbers
            first, second = map(int, line.split())
            # Append the numbers to the respective lists
            list1.append(first)
            list2.append(second)
    return sorted(list1), sorted(list2)

def find_difference_between_lists(list1, list2):
    diff = sum(list1) - sum(list2)
    if diff < 0:
        diff = diff * -1
    return diff

def main():
    list1, list2 = make_sorted_lists()
    difference = find_difference_between_lists(list1, list2)
    print(f'The distance between both lists is {difference}')


main()