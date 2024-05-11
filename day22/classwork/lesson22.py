
def manual_pop( collection , delete_index ):
    new_collection = []

    for index in range(0, len(collection)):
        if index != delete_index:
            new_collection.append(collection[index])

    return new_collection


names = ["gio","vakho","mate"]

print(manual_pop(names , 0))

#davaleba 222


def manual_count(collection, item_to_count):
    count = 0

    for item in collection:
        if item == item_to_count:
            count = count + 1
    
    return count


names = [True, True, False, True]

print(manual_count(names, True))