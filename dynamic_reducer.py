def dynamic_reducer(collection, op):
    if op == "/" or op == "-":
        result = float(collection[0])
    elif op == "*":
        result = float(1)
    elif op == "+":
        result = float(0)
    else:
        print("error: operator {0} is not an operator ".format(op))
        return 0

    for element in collection:
        if op == "+":
            result += float(element)
        elif op == "-":
            result -= float(element)
        elif op == "/":
            result = result / float(element)
        elif op == "*":
            result *= float(element)
        else:
            print("error: operator {0} is not an operator ".format(op)) # unreachable
    return result

total = dynamic_reducer([1, 2, 3], "+")
print (total)

