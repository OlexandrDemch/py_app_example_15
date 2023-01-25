end = int(input('x->'))
def print_table(n, i=1):
    if (i == 11):
        return
    print(end, "*", i, "=", n * i)
    i += 1
    print_table(n, i)


print_table(end)


