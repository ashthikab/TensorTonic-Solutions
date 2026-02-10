def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    # Write code here
    seasonal_average=[]
    for i in range(period):
        # period is 2
        avg=[]
        avg_num=0
        avg_count=0
        j=i
        while (j<len(series)):
            avg_num+=series[j]
            avg_count+=1
            j+=period

        seasonal_average.append(avg_num*1.0/avg_count)

    return seasonal_average
    
        

            