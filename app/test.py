def addition():
    return 1 + 3


a: int = addition()


def print_addition(param1):
    print(param1)
    return param1


# print_addition(a)

d = {"na": "me", "surname": "none of your business", "sex": "yes please"}
print(**d)