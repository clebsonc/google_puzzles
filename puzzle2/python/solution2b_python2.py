#coding=utf-8

def qt_negative_numbers(xs):
    count_negative = 0
    for value in xs:
        if value < 0:
            count_negative += 1
        else:
            break;
    return(count_negative)



def answer(xs):
    if len(xs) == 1:
        return str(xs[0])

    xs.sort()
    valid_numbers = qt_negative_numbers(xs) if xs[0] < 0 else 0
    product = 0
    if valid_numbers > 1:  # there are negative numbers
        valid_numbers = valid_numbers if valid_numbers%2 == 0 else valid_numbers-1
        product = xs[0]
        for value in xs[1:valid_numbers]:  # compute the product of negative numbers
            product *= value
    while valid_numbers < len(xs) and xs[valid_numbers] <= 0:
        valid_numbers += 1
    product = product if product != 0 else 1 if valid_numbers < len(xs) else 0
    for values in xs[valid_numbers:]:
        product *= values
    return str(product)





if __name__ == "__main__":
    values = input()
    values = values.strip()
    values = values.split(" ")
    values = [int(x) for x in values]
    print(answer(values))

