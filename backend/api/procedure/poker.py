from scipy.stats import chi2

PROBABILITY = {'TD': 0.30240, '1P': 0.50400, '2P': 0.10800, 'T': 0.07200, 'full': 0.00900, 'P': 0.00450, 'Q': 0.00010}


def poker(data, alfa, confidence, interval_range, min_limit, max_limit):
    formatted_data = __format_data_values(data)
    classified_data = __classify_data(formatted_data)
    frequency = __classify(classified_data)
    expected_frequency = __frequency__expected(formatted_data)
    chi_value = __calculate_chi2(frequency, expected_frequency)
    chi_result = __chi2_result(interval_range, chi_value, confidence)

    return {
        "classifiedData": classified_data,
        "frequency": frequency,
        "expectedFrequency": expected_frequency,
        "value": chi_value,
        "result": bool(chi_result)
    }


def __format_data_values(data):
    return [x.replace('0.', '') for x in data]


def __classify(number):
    frequencies = {}
    for i in number:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies


def __classify_word(frequencies: dict):
    new_dict = dict()
    classifier = ''

    for (key, value) in frequencies.items():
        if value > 1:
            new_dict[key] = value

    if len(new_dict) == 0:
        classifier = 'TD'
    elif len(new_dict) == 1:
        value_dict = list(new_dict.values())[0]
        if value_dict == 2:
            classifier = '1P'
        if value_dict == 3:
            classifier = 'T'
        if value_dict == 4:
            classifier = 'P'
        if value_dict == 5:
            classifier = 'Q'
    else:
        counter = 0
        for (k, v) in new_dict.items():
            if v == 2:
                counter += 1
        if counter == 1:
            classifier = 'TP'
        if counter == 2:
            classifier = '2P'

    return classifier


def __classify_data(data):
    data_classified = []
    for x in data:
        data_classified.append(__classify_word(__classify(x)))
    return data_classified


def __frequency__expected(data):
    fe = []
    for (key, value) in PROBABILITY.items():
        fe.append(value * len(data))
    return fe


def __calculate_chi2(frequency, expected_frequency):
    chi_array = []
    index = 0
    for k, v in frequency.items():
        chi_value = ((v - expected_frequency[index]) ** 2) / expected_frequency[index]
        chi_array.append(chi_value)
        index += 1
    return sum(chi_array)


def __chi2_result(interval_range, chi_value, confidence):
    gl = (2 - 1) * (interval_range - 1)
    table_chi = chi2.ppf(confidence, gl)
    return chi_value < table_chi



