from scipy.stats.distributions import chi2


def variance(data, alfa, confidence, interval_range, min_limit, max_limit):
    data_cast = __cast_data_values(data)
    average = __average(data_cast)
    tolerance1 = __tolerance1(alfa)
    tolerance2 = __tolerance2(alfa)
    table_chi, table_chi2 = __chi2_table(tolerance1, tolerance2, data_cast)
    var_result = __variance_result(average, table_chi, table_chi2, data)

    return {
        "average": average,
        "tolerance1": tolerance1,
        "tolerance2": tolerance2,
        "result": bool(var_result)
    }


def __cast_data_values(data):
    return [float(x) for x in data]


def __average(data):
    return sum(data) / len(data)


def __tolerance1(alfa):
    return alfa / 2


def __tolerance2(alfa):
    return 1 - (alfa / 2)


def __chi2_table(tolerance1, tolerance2, data):
    table_chi = chi2.ppf((1 - tolerance1), len(data))
    table_chi2 = chi2.ppf((1 - tolerance2), len(data))
    return table_chi, table_chi2


def __variance_result(average, table_chi, table_chi2, data):
    li = table_chi / (12 * (len(data) - 1))
    ls = table_chi2 / (12 * (len(data) - 1))
    return li <= average <= ls
