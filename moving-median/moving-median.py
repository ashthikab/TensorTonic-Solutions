def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here

    mm=[]
    mid = int(window_size/2)
    if window_size%2==0: 

        for i in range(0, len(values)-window_size+1):
            wind=values[i:i+window_size]
            wind.sort()
            mm.append((wind[mid]+wind[mid-1])*1.0/2)
    
    else:

        for i in range(0, len(values)-window_size+1):
            wind=values[i:i+window_size]
            wind.sort()
            mm.append(float(wind[mid]))
    
    return mm
    
