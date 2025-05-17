final_output = [] # (output, iterations)
failed_number = []
failures = []
num_dont_work = 0

def machine(number):

    n_list = []
    for n in f'{number:04d}':
        n_list.append(n)
    s_n_list = sorted(n_list)
    sorted_str = f'{s_n_list[0]}{s_n_list[1]}{s_n_list[2]}{s_n_list[3]}'
    sorted_str_prime = f'{s_n_list[3]}{s_n_list[2]}{s_n_list[1]}{s_n_list[0]}'
    sorted_number = int(sorted_str)
    number_prime = int(sorted_str_prime)

    return number_prime - sorted_number

for i in range(1000, 10000):
    n = i
    iterations = 0
    while n != 6174 and iterations < 8:
        n = machine(n)
        iterations += 1
    final_output.append([n, iterations])
    if iterations == 8:
        failures.append(i)

for i in final_output:
    if i[0] != 6174:
        num_dont_work += 1

print(f'Total Failures: {num_dont_work}')
print(f'Failures: {failures}')
