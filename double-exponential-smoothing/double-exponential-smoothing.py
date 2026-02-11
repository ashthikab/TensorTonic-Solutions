def double_exponential_smoothing(series, alpha, beta):
    """
    Apply Holt's linear trend method and return the level values.
    """
    # Write code here

    level=[]
    level.append(series[0]*1.0)
    trend=[]
    trend.append((series[1]-series[0])*1.0)

    for i in range(1,len(series)):
        level_val=(alpha*series[i])+((1-alpha)*(level[i-1]+trend[i-1]))
        level.append(level_val*1.0)
        trend_val=(beta*(level[i]-level[i-1]))+((1-beta)*trend[i-1])
        trend.append(trend_val*1.0)
    return level



