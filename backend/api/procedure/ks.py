import numpy as np
from scipy.stats import ksone


def ks(data, alfa, confidence, interval_range, min_limit, max_limit):
    data_cast = __cast_data_values(data)
    max_data_num = max(data_cast)
    min_data_num = min(data_cast)
    intervals = __calculate_intervals(min_data_num, max_data_num, interval_range)
    frequency = __calculate_frequency_array(data_cast, intervals)
    accumulate_frequency = __cumulative_frequency(frequency)
    frequency_probability = __frequency_probability(accumulate_frequency, data_cast)
    expected_frequency = len(data_cast) / interval_range
    expected_accumulate_frequency = __expected_cumulative_frequency(expected_frequency, interval_range)
    expected_probability_frequency = __frequency_probability(expected_accumulate_frequency, data_cast)
    difference = np.absolute(np.array(frequency_probability) - np.array(expected_probability_frequency))
    max_difference = max(difference)
    ks_result = __ks_result(max_difference, data_cast, confidence)

    return {
        "intervals": intervals,
        "frequency": frequency,
        "expectedFrequency": frequency_probability,
        "expectedFrequencyProb": expected_frequency,
        "difference": max_difference,
        "result": bool(ks_result)
    }


def __cast_data_values(data):
    return [float(x) for x in data]


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
    print(f'fre {frequency}')
    return __frequency_error_correction(data, frequency)


def __frequency_error_correction(data, frequency):
    data_len = len(data)
    freq_sum = sum(frequency)
    last_frequency_val = frequency[len(frequency) - 1]
    if data_len > freq_sum:
        last_frequency_val += 1
    elif data_len < freq_sum:
        last_frequency_val -= 1

    return frequency


def __cumulative_frequency(frequency):
    return np.cumsum(frequency)


def __frequency_probability(cumulative_frequency, data):
    fp = []
    for x in cumulative_frequency:
        fp.append(x / len(data))
    return fp


def __expected_cumulative_frequency(expected_frequency, intervals):
    return np.cumsum(np.full(intervals, expected_frequency, dtype=int))


def __ks_result(max_difference, data, confidence):
    table_value = ksone.ppf(confidence, len(data))
    return max_difference < table_value

