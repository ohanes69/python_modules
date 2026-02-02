def ft_helper_recursive(i, days):
    if i > days:
        print("Harvest time!")
        return
    else:
        print("Day", i)
        ft_helper_recursive(i + 1, days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_helper_recursive(1, days)
