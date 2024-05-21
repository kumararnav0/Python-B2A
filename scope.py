def drink_portion():
    potion_strength=2 #local variable having local scope
    print(potion_strength)
drink_portion()
print(potion_strength)    #will give an error