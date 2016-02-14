

def split_lists_half(thelist):
    return thelist[0 : len(thelist) // 2], thelist[len(thelist) // 2 : len(thelist)]
    # return thelist[: len(thelist) // 2], thelist[len(thelist) // 2 :]
    
    
    # return thelist[0 : len(thelist) // 2], thelist[len(thelist) // 2 + 1 :]
    # return thelist[0 : len(thelist) // 2 - 1], thelist[len(thelist) // 2 :]
    
    
lst1 = ["This", "course", "is", "great"]
lst2 = ["This", "course", "is", "great", '!']

print split_lists_half(lst1)
print split_lists_half(lst2)