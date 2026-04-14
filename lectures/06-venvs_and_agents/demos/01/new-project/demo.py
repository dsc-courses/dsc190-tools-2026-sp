import numpy as np

print("New Project")
print("-----------")
print(f"We are using numpy version {np.__version__}")
print()

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(np.vstack((x, y)))
