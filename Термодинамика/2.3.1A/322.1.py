import numpy as np
import matplotlib.pyplot as plt

time_2 = list(range(0, 71, 2))
pressure_2 = [660, 530, 360, 310, 230, 180, 160, 120, 100, 87, 71, 63, 57, 48, 41, 37, 34, 30, 27, 23, 19, 18, 17, 15, 14, 13, 11, 10, 9.4, 9.0, 8.4, 7.9, 7.4, 6.9, 6.8, 6.5]

time_3 = list(range(0, 69, 2))
pressure_3 = [630, 460, 360, 320, 210, 180, 160, 120, 100, 86, 73, 65, 58, 49, 42, 37, 34, 31, 27, 24, 20, 18, 17, 16, 14, 13, 11, 10, 9.5, 9.0, 8.4, 7.9, 7.5, 7.0, 6.8]

def analyze_series(time, pressure, series_name, color, marker):
    t = np.array(time, dtype=float)
    p = np.array(pressure, dtype=float)
    ln_p = np.log(p)
    coeffs = np.polyfit(t, ln_p, 1)
    slope, intercept = coeffs[0], coeffs[1]
    ln_p_fit = slope * t + intercept
    ss_res = np.sum((ln_p - ln_p_fit) ** 2)
    ss_tot = np.sum((ln_p - np.mean(ln_p)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    print(f"{series_name}: R² = {r2:.6f}")
    if r2 < 0.95:
        print(f"  ВНИМАНИЕ: зависимость НЕЛИНЕЙНА (R² = {r2:.4f})")
    else:
        print(f"  Зависимость близка к линейной.\n")
    plt.scatter(t, ln_p, label=f"{series_name} (данные)", color=color, s=20, marker=marker)
    t_fit = np.linspace(min(t), max(t), 100)
    ln_fit = slope * t_fit + intercept
    plt.plot(t_fit, ln_fit, '--', color=color, linewidth=2, label=f"{series_name} лин. регр. (k={slope:.4f})")
    return slope, intercept, r2

plt.figure(figsize=(12, 7))
plt.rcParams['font.size'] = 12

print("=" * 50)
print("РЕЗУЛЬТАТЫ АНАЛИЗА ЛИНЕЙНОСТИ ln(P) от t")
print("=" * 50)

analyze_series(time_2, pressure_2, "Серия 2", "red", "s")
analyze_series(time_3, pressure_3, "Серия 3", "green", "^")

plt.xlabel("Время t (с)", fontsize=14)
plt.ylabel("ln(P) [P в mbar]", fontsize=14)
plt.title("Зависимость ln(P) от времени для двух серий", fontsize=16)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()