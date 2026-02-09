def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here

    sma=[]
    for i in range(0,len(values)-len(weights)+1):
        num=0
        for j in range(0,len(weights)):
            num+= weights[j]*values[i+j]*1.0
        sma.append(num/sum(weights))
    
    return sma