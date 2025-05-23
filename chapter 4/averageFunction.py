def average(first, *args):
    return (first + sum(args)) / (1 + len(args))


print(average(2,3,20,5,7))