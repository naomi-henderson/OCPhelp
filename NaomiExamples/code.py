def callIngrid(ingridcode):
    """ Call ingrid from python.

    Example
    -------
        import sys
        sys.path.append("/net/carney/home/naomi/mymodules")
        from ingrid.code import callIngrid

        ingridcode = \"\"\"
        \\\\begin{ingrid}
        %% comments need double percent
        SOURCES .WORLDBATH432 .bath
        (bath.nc)writeCDF 
        \\\\end{ingrid} 
        \"\"\"
    
        callIngrid(ingridcode)
    
    Parameters
    ----------
        ingridcode : str
        A multiline string starting with \\\\begin{ingrid} and 
        ending with \\\\end{ingrid}
    """
    from subprocess import Popen, PIPE
    p = Popen(['/usr/local/bin/ingrid'], stdin=PIPE, stdout=PIPE) 
    ingridout, ingriderr = p.communicate(input=bytes(ingridcode, 'utf-8'))
    print (ingridout.decode())
    return ingriderr
