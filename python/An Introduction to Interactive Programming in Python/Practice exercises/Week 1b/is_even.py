
def is_even2(number):
    """ :5555 """
    _is_even = None
    if number % 2 == 0:
        _is_even = True
    else:
        _is_even = False
        
    return _is_even
    
def is_even(number):
    """ Returns whether the number is even. """
    return (number % 2) == 0
    
def test_even(number):
    """ Tests the is_even function. """
    print ''
    if is_even(number):
        print number, 'is even.'
    else:
        print number, 'is odd.'
    
test_even(3)
test_even(4)
test_even(5)
test_even(10)