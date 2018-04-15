def Smooth121(v, sdims, NSmooths= 1, perdims= []):
    """ Applies [1 2 1]/4 stencil in multiple dimensions
    
    Usage
    -----
    Smooth121(DataArray,list1,Nsmooths=int1,perdims=list2)
        name : xarray.DataArray - e.g., ds.var
        list1: list of dimensions over which to smooth - e.g., ['Y','X']
        int1 : integer number of smooths to apply - e.g., 1
        list2: list of dimension to be treated as period boundaries - e.g., ['X']
        
    Example
    -------
        smooth_var = Smooth121(ds.var, ['lon', 'lat], NSmooths = 2, perdims = ['lon'])
    """
    
    origdims = v.dims
    for smooth in range(0, NSmooths):
        for dim in sdims:
            #print('smoothing in ',dim)
            v = SM121_1d(v, dim, dim in perdims)
    return v.transpose(*origdims)

def SM121_1d(v, dim1, iper):
    import xarray as xr
    if iper:
        vPad = xr.concat([v.isel(**{dim1: -1}), v, v.isel(**{dim1: 0})], dim= dim1)
    else:
        vPad = xr.concat([v.isel(**{dim1:  0}), v, v.isel(**{dim1: -1})], dim= dim1)
    
    rollargs = {dim1: 2}
    # average from centers to edges
    vsm1 = (vPad.rolling(**rollargs).mean(dim = dim1))

    # average back to centers
    vsm2 = (vsm1.rolling(**rollargs).mean(dim = dim1)
                .shift(**{dim1: -1}))
     
    vUnPad = vsm2.isel(**{dim1: slice(1, -1, None)}) 
    return vUnPad 
