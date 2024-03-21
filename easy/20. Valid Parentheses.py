#Input
s = "[(())[]]"

#Logic
def main(s):
    changes = True
    while changes: # Infinity loop, it stops when the last updated 's' equals to s
        temp = s.replace('()', '').replace('{}', '').replace('[]', '') # Remove
        if temp == s: changes = False # If nothing is removed, it works.
        s = temp # Assign the updated 's'
    return s=='' #-> empty or not empty. If it's empty, it's valid.
    
#Output
print(main(s))
