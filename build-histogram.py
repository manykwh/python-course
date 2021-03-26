def build_histogram(values_dict):
    histogram_result = {}
    for k in values_dict.keys():
        histogram_result[k[0]] = int(values_dict[k]) * '$'
    return histogram_result

def print_histogram(values_dict):
    for k in values_dict.keys():
        print("{0}: {1}".format(k, values_dict[k]))

sales = { 'google': 20, 'facebook': 42, 'twitter': 10, 'offline': 12, }
print_histogram(build_histogram(sales))

