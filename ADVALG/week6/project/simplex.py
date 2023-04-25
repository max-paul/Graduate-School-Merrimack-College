import numpy as np


def simplex(c, A, b):
    # Initialize the solution vector x
    x = np.zeros(A.shape[1])

    # Set the initial values of the basic variables in x to b[i]/A[i,i]
    x[:len(b)] = b / np.diag(A)

    # Define the initial basis (set of basic variables)
    B = np.arange(len(b))  # indices of basic variables
    N = np.arange(len(b), A.shape[1])  # indices of non-basic variables

    # Main loop of the simplex algorithm
    while True:
        # Compute the reduced costs of the non-basic variables
        # The reduced cost of a variable j is c[j] - c[B] * A[B,N[j]] * inv(A[B,B]) * A[B,j]
        # where B is the current basis and N[j] is the index of variable j in the non-basic variables
        cN = c[N] - np.dot(c[B], np.linalg.inv(A[:, B]).dot(A[:, N]))

        # If all reduced costs are non-negative, the current solution is optimal
        if np.all(cN >= 0):
            break

        # Select the most negative reduced cost variable
        j = np.argmin(cN)

        # Compute the direction of the variable with most negative reduced cost
        # The direction d is a vector such that A[:,B] * d[B] + A[:,N[j]] * d[N[j]] = 0 and d[B] <= 0
        d = np.zeros_like(x)
        Ad = np.linalg.inv(A[:, B]).dot(A[:, N[j]])
        d[B] = -np.linalg.inv(A[:, B]).dot(A[:, N[j]])
        d[N[j]] = 1

        # Compute the step length
        # The step length is the minimum value of x[B[i]]/d[B[i]] such that d[B[i]] < 0
        step_lengths = np.divide(x[B], d[B])
        step_lengths = np.where(step_lengths > 0, step_lengths, np.inf)
        i = np.argmin(step_lengths)
        theta = step_lengths[i]

        # Update the solution and the basis
        # The updated solution is x + theta * d
        # The updated basis is obtained by replacing the i-th basic variable with the j-th non-basic variable
        x = x + theta * d
        B[i] = N[j]
        N[j] = B[i - 1]

    # Return the optimal solution and the optimal objective value
    return x, np.dot(c, x)
