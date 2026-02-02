def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    titled_seed_type = seed_type.title()
    if unit == "packets":
        print(titled_seed_type, "seeds:", quantity, unit, "available")
    elif unit == "grams":
        print(titled_seed_type, "seeds:", quantity, unit, "total")
    elif unit == "area":
        print(titled_seed_type, "seeds:", "covers", quantity, "square meters")
    else:
        print(titled_seed_type, "seeds:", quantity, "Unknown unit type")
