l = ["Varun", "Atharva", "Tanaya", "Aayush"]

def rem(l, word):
    for item in l:
        l.remove(word)
        return l
    
print(rem(l, "Aayush"))