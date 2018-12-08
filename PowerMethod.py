import numpy as np
import math

class PowerMethod(object):
    def __init__(self, input_matrix, k):
        # np.set_printoptions(precision=30)
        self.input = input_matrix
        self.result = []
        self.k = k
        self.sinvector = []
        self.leftsinvector = []
    
    @ staticmethod
    def eigenvalue(A, v):
        # v is a normalized vector. Since Av = lambda * v
        # Now, we left multiply each side of the equation by (v Transpose)
        # => vT * (Av) = vT * lambda * v
        # => vT * (Av) = lambda * (vT * v) = lambda * （1） = lambda
        # => The eigenvalue of matrix A is vT * (Av)
        Av = A.dot(v)
        result = (np.transpose(v)).dot(Av)
        return result

    @ staticmethod
    def getDominantEv(A):
        # The input of this function is actually AT * A
        # The output of this function is the dominant eigen value and its corresponding eigen vector
        # For a matrix A, we first get the length of its row and its column
        n, d = A.shape
        # Create a vector v that is normalized by a one vector with length d, which is the length of A's column
        v = np.ones(d) / np.sqrt(d)
        # Now we use the function eigenvalue() to calculate the eigenvalue given matrix A and random vector v
        prev_ev = PowerMethod.eigenvalue(A, v)
        # The following is a loop that calculates the dominate eigenvalue.
        while True:
            Av = A.dot(v)
            # Create another normalized vector x
            curr_evector = Av / np.linalg.norm(Av)
            # We calculate the eigen value for another time
            # Since when we raise the power of ATA to a very high value, the eigen value it gets will actually converge
            # So once the difference between previous and current eigen value we got is smaller than 0.001
            # We can know that the eigenvalue starts to converge and at this time, we return the eigen vector and value
            curr_ev = PowerMethod.eigenvalue(A, curr_evector)
            if np.abs(prev_ev - curr_ev) < 0.00001:
                break
            v = curr_evector # Replace the previous eigen vector and eigen value with the new ones, do this loop again
            # Until the eigenvalue converges
            prev_ev = curr_ev
        return (curr_ev, curr_evector)

    def power_method(self):
        while self.k > 0:
            ATransA = np.matmul(np.transpose(self.input), self.input)
            (DominantEv, self.sinvector) = self.getDominantEv(ATransA)
            singularvalue = math.sqrt(DominantEv)
            Av = np.matmul(self.input, self.sinvector)
            self.leftsinvector = (Av / singularvalue)
            templeft =np.array([[i] for i in list(self.leftsinvector)])
            tempright = np.array([list(self.sinvector)])
            self.input = self.input - singularvalue * (np.matmul(templeft, tempright))
            self.leftsinvector = list(self.leftsinvector)
            self.sinvector = list(self.sinvector)
            self.result.append([singularvalue, self.sinvector, self.leftsinvector])
            self.sinvector, self.leftsinvector = [], []
            self.k -= 1
        return self.result

# T = PowerMethod([[ 0.041,0.815,0.245,0.054,0.249,0.534,0.753,0.307,0.877,0.429],
#  [ 0.918,0.846,0.249,0.262,0.133,0.32, 0.446,0.122,0.164,0.711],
#  [ 0.139,0.701,0.726,0.094,0.036,0.695,0.325,0.29, 0.373,0.692],
#  [ 0.644,0.067,0.032,0.896,0.047,0.55, 0.062,0.568,0.204,0.275],
#  [ 0.631,0.412,0.232,0.415,0.335,0.508,0.393,0.549,0.076,0.698]]
# , 5)
#print(T.power_method())