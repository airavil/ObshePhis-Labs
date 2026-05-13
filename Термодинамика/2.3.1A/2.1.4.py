import numpy as np
import matplotlib.pyplot as plt

time = list(range(0, 19, 2))
pressure = [5.0, 4.9, 4.7, 4.5, 4.3, 3.9, 3.7, 3.4, 3.0, 2.7]

t = np.array(time, dtype=float)
p = np.array(pressure, dtype=float)
ln_p = np.log(p)

coeffs = np.polyfit(t, ln_p, 1)
slope, intercept = coeffs[0], coeffs[1]

ln_p_fit = slope * t + intercept
ss_res = np.sum((ln_p - ln_p_fit)**2)
ss_tot = np.sum((ln_p - np.mean(ln_p))**2)
r2 = 1 - (ss_res / ss_tot)

print("="*50)
print("РЕЗУЛЬТАТЫ АНАЛИЗА ln(P) от t")
print("="*50)
print(f"Уравнение: ln(P) = {slope:.6f} * t + {intercept:.6f}")
print(f"R² = {r2:.6f}")
if r2 < 0.95:
    print("ВНИМАНИЕ: зависимость НЕЛИНЕЙНА (R² < 0.95)")
else:
    print("Зависимость близка к линейной.")

plt.figure(figsize=(12, 7))
plt.scatter(t, ln_p, color='blue', s=20, label='Данные')
t_fit = np.linspace(min(t), max(t), 100)
ln_fit = slope * t_fit + intercept
plt.plot(t_fit, ln_fit, '--', color='red', linewidth=2, label=f'Линейная регрессия: k={slope:.4f}')
plt.xlabel("Время t (с)", fontsize=14)
plt.ylabel("ln(P) [P в mbar]", fontsize=14)
plt.title("Зависимость ln(P) от времени", fontsize=16)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()