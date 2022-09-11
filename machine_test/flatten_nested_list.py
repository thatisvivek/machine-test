def solution_one(mylist: list[list]) -> list:
    for item in mylist:
        if type(item) is list:
            solution_one(item)
        else:
            print(item)
