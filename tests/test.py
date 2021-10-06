def my_func(a, b):
    ''' returns multipllication
    Test-1: testing with numbers
    >>> my_func(3, 5)
    15

    Test-2: with strings
    >>> my_func('c', 4)
    'ccccc'
    '''
    return a*b

def out(obj):
    """unpredictable test
    Tests: doctesting unpredictable things

    >>> out(my_func) #doctest: +ELLIPSIS
    <function my_func at 0x...>
    """
    print(obj)