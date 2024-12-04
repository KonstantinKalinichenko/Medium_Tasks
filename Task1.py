def process_employee_data(input_string: str) -> str:
    updated_data = input_string.replace(';', ',').split(',')
    ages = [int(i) for i in updated_data if i.isdigit()]
    ages.sort()
    n = len(ages)
    m = n // 2
    if n % 2 > 0:
        mid_age = ages[m]
    else:
        mid_age = round(sum(ages[m - 1: m + 1]) / 2)
    return f'{ages[0]} {mid_age} {ages[n-1]}'


input_data = input()
output_data = process_employee_data(input_data)
print(output_data)
