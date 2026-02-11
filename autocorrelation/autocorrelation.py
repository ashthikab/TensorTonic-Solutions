def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    autocorrelation=[1]

    mean=sum(series)*1.0/len(series)

    var=0
    for i in range (len(series)):
        var+=(series[i]-mean)**2

    for i in range (1,max_lag+1):
        if var==0:
            autocorrelation.append(0)
        
        else:
            autocorrelation_num=0
            for j in range (len(series)-i):
                autocorrelation_num+=(series[j]-mean)*(series[j+i]-mean)*1.0
            autocorrelation.append(autocorrelation_num/var)
    
    return autocorrelation