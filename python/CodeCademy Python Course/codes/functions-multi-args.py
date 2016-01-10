def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

numbers = []
while True:
    num = raw_input('Enter a number or Quit for quit:')
    if num == 'Quit' or num == 'quit' : break
    if len(num) < 1:continue
    # if num.is_integer
    numbers.append(int(num))
    
biggest_number(*numbers)