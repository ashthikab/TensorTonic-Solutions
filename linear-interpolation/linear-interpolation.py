def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here

    new_values = [float(x) if x is not None else None for x in values]

    none_index=[]
    for i in range (len(new_values)):
        if (new_values[i]==None):
            none_index.append(i)
    
    for i in none_index:
        
        left=i-1
        while (left in none_index):
            left-=1
        
        right=i+1
        while (right in none_index):
            right+=1

        new_values[i]= new_values[left] + (((i-left)*1.0/(right-left)) * (new_values[right]-new_values[left]))
    
    
    return new_values