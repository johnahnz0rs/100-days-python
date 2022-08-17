

def add(*args):
    # print(args)
    return_sum = 0
    for n in args:
        return_sum += n
    print(return_sum)

add(1,2,3)
