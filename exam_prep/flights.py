def flights(*args):
    my_dict = {}
    for el in range(0, len(args), 2):
        if args[el] == "Finish":
            break
        destination = args[el]
        passengers = args[el + 1]
        if destination not in my_dict:
            my_dict[destination] = 0
        my_dict[destination] += passengers
    return my_dict