import numpy as np
from scipy import linalg

A = np.array([
    [1, 9, 2, 1, 1],
    [10, 1, 2, 1, 1],
    [16, 2, 3, 1, 1],
    [17, 5, 4, 1, 1],
    [19, 2, 2, 3, 1]
])
b=print('hi')
b = np.array([170, 180, 130, 140, 185]).reshape((5, 1))

A_inv = linalg.inv(A)
x = A_inv.dot(b)

print("Solution vector x:")
print(x)

# Define the coefficient matrix
A = np.array([[1, 1, 1], [1, 2, 4], [1, 2, 4]])

# Define the constant vector
b = np.array([5, 13, 25]).reshape((3, 1))

# Solve the system of linear equations using the least squares method
p, *_ = linalg.lstsq(A, b)


# Print the solution vector
print("Solution vector p:")
print(p)

# Generate data points
x = np.linspace(0, 3, 1000)

# Calculate y-values for the quadratic curve
y = p[0] + p[1] * x + p[2] * x ** 2

# Plot the curve
plt.plot(x, y)

# Plot the data points
plt.plot(1, 5, "ro")
plt.plot(2, 13, "ro")
plt.plot(2, 25, "ro")

# Display the plot
plt.show()
 
