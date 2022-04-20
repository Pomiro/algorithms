def search(A, u):
    for i in range(len(A)):
        if A[i] == u:
            return i
    return null
print(search([1,2,3], 3))
