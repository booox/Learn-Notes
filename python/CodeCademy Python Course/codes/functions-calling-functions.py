def one_good_turn(n):
    print n + 1
    return n + 1
    
def deserves_another(n):
    n = one_good_turn(n) + 1
    print n
    return n
print deserves_another(1)