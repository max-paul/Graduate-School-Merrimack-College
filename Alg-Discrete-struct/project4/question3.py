"""
3) Given an integer n>=2 and two nxn matrices A and B of real numbers,
 find the product AB of the matrices. Your function should have three input parameters –
 a positive integer n and two nxn matrices of numbers– and should return the nxn product matrix using a return statement.


"""

def multiply_matrices(X, Y, n):

    Matrix = [[0 for x in range(n)] for y in range(n)]

    # iterate through rows of X
    for i in range(len(X)):
       # iterate through columns of Y
       for j in range(len(Y[0])):
           # iterate through rows of Y
           for k in range(len(Y)):
               Matrix[i][j] += X[i][k] * Y[k][j]


multiply_matrices([[2,7],[3,5]], [[8,-4],[6,6]], 2)