from scipy.stats import chi2


def chi(data, alfa, confidence, interval_range, min_limit, max_limit):
    l_norm = __calculate_ni(data, min_limit, max_limit)
    max_data_num = max(l_norm)
    min_data_num = min(l_norm)
    intervals = __calculate_intervals(min_data_num, max_data_num, interval_range)
    frequency = __calculate_frequency_array(l_norm, intervals)
    expected_frequency = len(data) / interval_range
    chi_value = __calculate_chi2(frequency, expected_frequency)
    chi_result = __chi2_result(interval_range, chi_value, confidence)

    return {
        "intervals": intervals,
        "frequency": frequency,
        "expectedFrequency": expected_frequency,
        "value": chi_value,
        "result": bool(chi_result)
    }


def __calculate_ni(data, lower, upper):
    return [lower + (upper - lower) * float(x) for x in data]


def __calculate_intervals(min_data_num, max_data_num, num_intervals):
    intervals_array = []
    for x in range(num_intervals):
        if x == 0:
            interval_init = min_data_num
        else:
            interval_init = intervals_array[x - 1][1]

        interval_final = interval_init + (max_data_num - min_data_num) / num_intervals
        intervals_array.append([interval_init, interval_final])

    return intervals_array


def __calculate_frequency_array(data, array):
    frequency = []
    for x in range(len(array)):
        counter = 0
        for j in data:
            if array[x][0] <= j <= array[x][1]:
                counter += 1
        frequency.append(counter)
    return frequency


def __calculate_chi2(frequency, expected_frequency):
    chi_array = []
    for x in frequency:
        chi_value = ((x - expected_frequency) ** 2) / expected_frequency
        chi_array.append(chi_value)
    return sum(chi_array)


def __chi2_result(interval_range, chi_value, confidence):
    gl = (2 - 1) * (interval_range - 1)
    table_chi = chi2.ppf(confidence, gl)
    return chi_value < table_chi
