def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        recurs = get_multiplied_digits(int(str_number[1:]))
        if first == 0:
            return recurs
        else:
            return first * recurs

    if str_number != 0:
        return int(str_number)
    else:
        1

print(get_multiplied_digits(40203))