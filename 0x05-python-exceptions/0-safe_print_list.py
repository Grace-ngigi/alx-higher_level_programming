def safe_print_list(my_list=[], x=0):
    num = 0
    for items in range(x):
        try:
            print(f'{my_list[items]}', end='')
        except (IndexError):
            continue
        num += 1
    print()
    return (num)
