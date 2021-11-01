def mean(data):
    n = len(data)
    mean = sum(data) / n
    return mean


def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance


def stdev(data):
    import math
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev
