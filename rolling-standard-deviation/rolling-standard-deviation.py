def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    # Write code here
    rollingsd=[]
    for i in range(len(values)-window_size+1):
        sublist=values[i:i+window_size]
        mean=sum(sublist)*1.0/window_size
        sd_num=0
        for j in range (len(sublist)):
            sd_num+=(sublist[j]-mean)**2
        sd=(sd_num/window_size)**0.5 #sqrt calculation

        rollingsd.append(sd)
    
    return rollingsd