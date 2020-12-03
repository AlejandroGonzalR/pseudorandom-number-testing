import scipy.stats as st
import math


def mean(data, alfa, confidence, interval_range, min_limit, max_limit):
    data_cast = __cast_data_values(data)
    average = __average(data_cast)
    tolerance = __tolerance(alfa)
    z = __calculate_z(tolerance)
    mean_result = __mean_result(average, data_cast, z)

    return {
        "average": average,
        "tolerance": tolerance,
        "z": z,
        "result": bool(mean_result)
    }


def __cast_data_values(data):
    return [float(x) for x in data]


def __average(data):
    return sum(data) / len(data)


def __tolerance(alfa):
    return 1 - (alfa / 2)


def __calculate_z(tolerance):
    return st.norm.ppf(tolerance)


def __mean_result(average, data, z):
    li = 0.5 - z * (1 / (math.sqrt(12 * len(data))))
    ls = 0.5 + z * (1 / (math.sqrt(12 * len(data))))
    return li <= average <= ls
