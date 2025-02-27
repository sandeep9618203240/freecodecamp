import numpy as np

def calculate(numbers):
    mat = np.array(numbers).reshape(3, 3)
    ans={
        'mean': [np.mean(mat, axis=0).tolist(), np.mean(mat, axis=1).tolist(), np.mean(mat)],
        'variance': [np.var(mat, axis=0).tolist(), np.var(mat, axis=1).tolist(), np.var(mat)],
        'standard deviation': [np.std(mat, axis=0).tolist(), np.std(mat, axis=1).tolist(), np.std(mat)],
        'max': [np.max(mat, axis=0).tolist(), np.max(mat, axis=1).tolist(), np.max(mat)],
        'min': [np.min(mat, axis=0).tolist(), np.min(mat, axis=1).tolist(), np.min(mat)],
        'sum': [np.sum(mat, axis=0).tolist(), np.sum(mat, axis=1).tolist(), np.sum(mat)]
    }

res = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(res)