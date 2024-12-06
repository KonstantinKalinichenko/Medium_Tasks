def solve(input_string: str) -> str:
    str_list = input_string.split(' ')
    int_list = [int(i) for i in str_list]
    res = [str(max(int_list[:i+1])) for i in range(len(int_list))]
    return ' '.join(res)


input_string = input()
result = solve(input_string)
print(result)
