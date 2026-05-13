import numpy as np
import matplotlib.pyplot as plt

W = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
P = [3.35e-6, 1.9e-5, 3.2e-5, 3.95e-5, 5e-5, 5.85e-5, 6.4e-5, 6.9e-5, 7.55e-5, 8e-5]

coeffs = np.polyfit(W, P, 1)
k, b = coeffs
P_fit = k * np.array(W) + b

ss_res = np.sum((np.array(P) - P_fit)**2)
ss_tot = np.sum((np.array(P) - np.mean(P))**2)
r2 = 1 - (ss_res / ss_tot)

print("="*50)
print("РЕЗУЛЬТАТЫ АППРОКСИМАЦИИ")
print("="*50)
print(f"Уравнение: P(W) = {k:.4e} * W + {b:.4e}")
print(f"Коэффициент детерминации R² = {r2:.6f}")

plt.figure(figsize=(8, 6))
plt.plot(W, P, 'o', markersize=8, label='Экспериментальные данные')
plt.plot(W, P_fit, '-', color='red', linewidth=1.5, label=f'Аппроксимация: P = {k:.2e}·W + {b:.2e}')
plt.xlabel('Мощность W (Вт)')
plt.ylabel('Давление P (mbar)')
plt.title('Зависимость давления от мощности')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()