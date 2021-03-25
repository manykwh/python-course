def dynamic_reducer(collection, op):
    result = float(collection[0])
    for element in collection[1:]:
        if op == "+":
            result += float(element)
        elif op == "-":
            result -= float(element)
        elif op == "/":
            result = result / float(element)
        elif op == "*":
            result *= float(element)
        else:
            print("error: operator {0} is not an operator ".format(op))
    return result

total = dynamic_reducer([1, 2, 3], "+")
print (total)
total = dynamic_reducer([1, 2, 3], "/")
print (total)

print(dynamic_reducer([1, 2, 250], '+'))
print(dynamic_reducer([1, 2, 3], '-'))
print(dynamic_reducer([1, 2, 55], '*'))
print(dynamic_reducer([100, 2, 3], '/'))


