def build_histogram(values_dict):
    histogram_result = {}
    for k in values_dict.keys():
        histogram_result[k] = int(values_dict[k]) * '$'
    return histogram_result

