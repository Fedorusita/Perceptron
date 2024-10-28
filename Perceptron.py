import numpy as np
import matplotlib.pyplot as plt

N = 5

# ��������� ������ ��� ������� ������
x1 = np.random.random(N)
x2 = x1 + [np.random.randint(10) / 10 for _ in range(N)]
C1 = [x1, x2]

# ��������� ������ ��� ������� ������
x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10) / 10 for _ in range(N)] - 0.1
C2 = [x1, x2]

# ��������� ��� �����
f = [0, 1]

# ���� ��� �������� ����������
w = np.array([-0.3, 0.3])
for i in range(N):
    x = np.array([C2[0][i], C2[1][i]])
    y = np.dot(w, x)

# ���������� ��������
plt.scatter(C1[0], C1[1], s=10, c='red', label='Class 1')
plt.scatter(C2[0], C2[1], s=10, c='blue', label='Class 2')




# ��������� �������
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(f)
plt.grid(True)
plt.legend()

# ����������� �������
plt.show()