
def rem(l, word):
    n = [] 
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


l = ["Prannay", "Rohan", "Sanyam", "an"]

print(rem(l, "an"))