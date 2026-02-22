import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    unique_y=list(set(y))
    
    count_y=[]
    for i in unique_y:
        count_y.append(y.count(i))
    
    prob_y=[]
    for i in range(len(count_y)):
        prob_y.append(count_y[i]*1.0/len(y))
    
    entropy=0
    for i in range(len(unique_y)):
        entropy+= (prob_y[i] * (np.log2(prob_y[i])))
    
    return -1.0*entropy
    pass
