# -*- coding: utf-8 -*-

from sklearn.model_selection import TimeSeriesSplit


def build_validation_dataset(y, strategy, n_lags, n_rounds):
    if strategy == 'holdout':
        holdout = n_lags
        training_y = [y[:-n_lags]]
        test_y = [y[-n_lags:]]
    elif strategy == 'rolling':
        training_y = []
        test_y = []
        holdout = int(n_lags / n_rounds)
        for i in range(n_rounds):        
            test_start = int(-n_lags + holdout * i)
            test_end = test_start + holdout                
            training_y.append(y[:test_start])
            if test_end != 0:
                test_y.append(y[test_start:test_end])
            else:
                test_y.append(y[test_start:])
    return training_y, test_y




