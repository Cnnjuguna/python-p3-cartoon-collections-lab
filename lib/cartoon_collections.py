def roll_call_dwarves(dwarves=["Doc", "Dopey", "Bashful", "Grumpy"]):
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}")
    pass


def summon_captain_planet(planeteer_calls=["earth", "wind", "fire", "water", "heart"]):
    return [f"{a_call.title()}!" for a_call in planeteer_calls]
    pass


def long_planeteer_calls(assorted_words=["two", "go", "industrious", "bop"]):
    return any(len(a_call) > 4 for a_call in assorted_words)
    pass


def find_the_cheese(soups=["tomato soup", "cheddar", "oyster crackers", "gouda"]):
    # for item in soups:
    #     if item == "cheddar" or item == "gouda" or item == "camembert":
    #         return item

    cheese_options = {"cheddar", "gouda", "camembert"}
    common_cheeses = cheese_options & set(soups)
    if common_cheeses:
        return common_cheeses.pop()
    else:
        return None

    # cheese_options = {"cheddar", "gouda", "camembert"}
    # for item in soups:
    #     if item in cheese_options:
    #         return item

    pass
