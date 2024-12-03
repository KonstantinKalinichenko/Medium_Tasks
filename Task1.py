def process_employee_data(input_string: str) -> str:
    updated_data = input_string.replace(';', ',').split(',')
    ages = [int(i) for i in updated_data if i.isdigit()]
    ages.sort()
    n = len(ages)
    if n % 2 > 0:
        m = n // 2
        mid_age = ages[m]
    else:
        mid_age = round(sum(ages[n // 2 - 1: n // 2 + 1]) / 2)
    min_age = ages[0]
    max_age = ages[n - 1]
    result = f'{min_age} {mid_age} {max_age}'
    return result


input_data = input()
output_data = process_employee_data(input_data)
print(output_data)
