def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    sma=[]
    for i in range(0,len(values)-window_size+1):

        sma.append(sum(values[i:i+window_size])/window_size*1.0)
    
    return sma
