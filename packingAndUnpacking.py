dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]
string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(dicts):
    result_list = []
    for item in dicts:
        result_list.append(string.format(**item))
        print(string.format(**item))
        print(item)
    return result_list


string_factory(dicts)

print(string_factory(dicts))

