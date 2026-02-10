def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here

    lag_ret=[]
    max_lag=max(lags)
    for t in range(max_lag,len(series)):
        row=[]
        for lag in lags:
            row.append(series[t-lag])
        lag_ret.append(row)
    return lag_ret


        


