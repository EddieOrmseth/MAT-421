import numpy as np


if __name__ == '__main__':
    # rotation matrices
    rotation_matrix_1 = np.array([[0, -1], [1, 0]])
    rotation_matrix_2 = np.array([[0, 1], [-1, 0]])

    vector1 = np.array([1, 0])
    vector2 = np.array([2, 1])
    vector3 = np.array([1, 5])
    vector4 = np.array([-1, 5])
    vector5 = np.array([4, -3])
    vectors = [vector1, vector2, vector3, vector4, vector5]

    for vector in vectors:
        rotated_vector_1 = rotation_matrix_1 @ vector
        rotated_vector_2 = rotation_matrix_2 @ vector

        print("Original Vector:", vector)
        print("Rotated 1 Vector:", rotated_vector_1)
        print("Rotated 2 Vector:", rotated_vector_2)
        print("Inner Product: rotated_vector_1 X vector:", + rotated_vector_1 @ vector)
        print("Inner Product: rotated_vector_2 X vector:", + rotated_vector_2 @ vector)
        print()


    vector = np.array([1, 3])
    matrix1 = np.array([[4, 2], 
                        [1, 3]])
    matrix2 = np.array([[2, 3], 
                         [1, 1]])
    matrix3 = np.array([[2, 2], 
                        [1, 5]])
    matrices = [matrix1, matrix2, matrix3]

    for matrix in matrices:
        eigenvalues, eigenvectors = np.linalg.eig(matrix)

        print("Original Matrix:\n", matrix)
        print("Eigenvalues:", eigenvalues)
        print("Eigenvectors:\n", eigenvectors)

        for i in range(len(eigenvalues)):
            eigenvalue = eigenvalues[i]
            eigenvector = eigenvectors[:, i]

            print("\tOriginal Vector:", vector)
            print("\tEigenvalue * Eigenvector:", eigenvalue * eigenvector)
            print("\tMatrix * Eigenvector:\t ", matrix @ eigenvector)
            print()
