def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here

    wfac=1
    ret=[]

    for i in range(0,len(returns)):
        wfac=wfac*(1+returns[i])
        ret.append(wfac-1)

    return ret
        