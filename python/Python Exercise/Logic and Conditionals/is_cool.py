

def is_cool_1(name):
    """Returns whether the person is cool."""
    
    return (name == "Joe") or (name == "John") or (name == "Stephen")

def is_cool(name):
    return name in ["Joe", "John", "Stephen"]
    
def test(name):
    
    print ''
    if is_cool(name):
        print name, 'is cool.'
    else:
        print name, 'is not cool.'
        
test("Joe")
test("John")
test("Stephen")
test("Scott")