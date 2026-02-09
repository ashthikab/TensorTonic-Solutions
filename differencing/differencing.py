def recurrentfn(temp):
    ret=[]
    for i in range(len(temp)-1):
        ret.append(temp[i+1]-temp[i])
    return ret

def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    diff=series.copy()
    for i in range(order):
        #print(diff)
        diff=recurrentfn(diff).copy()

    return diff