def number_of_frogs(year):
    if year == 1:
        return int(120)
    else:
        return 2 * (int(number_of_frogs(year - 1)) - 50)
