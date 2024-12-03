# https://adventofcode.com/2024/day/3
import re

def make_list():
    with open('input.txt', 'r') as file:
        content = file.read()
        mul_list = re.finditer(r"mul\((\d+),(\d+)\)", content)
    return mul_list, content

def filter_list(mul_list, content):
    count = 0
    enabled = True
    for mul in mul_list:
        start = mul.start()
        before_text = content[:start]
        if "don't()" in before_text:
            enabled = False
        elif "do()" in before_text:
            enabled = True
        if enabled:
            count += calculate(mul.group(0))
    return count

def calculate(mul):
    match = re.search(r"mul\((\d+),(\d+)\)", mul)
    num1 = int(match.group(1))
    num2 = int(match.group(2))
    return num1 * num2

def main():
    mul_list, content = make_list()
    res = filter_list(mul_list, content)
    print(f'The mul number is {res}')

main()
