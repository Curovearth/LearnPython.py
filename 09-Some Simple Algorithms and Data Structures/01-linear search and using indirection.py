# Linear Search and Using Indirection to Access Elements

def search(L,e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        
    return False

print(search([1,2,3],4))