import matplotlib.pyplot as plt
import numpy as np

# Defining the x values (n: input size in terms of log scale, e.g., 10^2 to 10^7)
n = np.logspace(2, 7, 500)  # from 10^2 to 10^7

# Defining the time complexities for each algorithm
sqrt_n = np.sqrt(n)  # O(sqrt(n))
log2_n = np.log(n)**2  # O(log^2 n) for Fermat
log3_n = np.log(n)**3  # O(log^3 n) for Miller-Rabin
log6_n = np.log(n)**6  # O(log^6 n) for AKS


# Plotting the time complexities
plt.figure(figsize=(10, 6))

plt.plot(n, sqrt_n, label=r"$O(\sqrt{n})$", color='blue')
plt.plot(n, log2_n, label=r"$O(\log^2 n)$ (Fermat)", color='red')
plt.plot(n, log3_n, label=r"$O(\log^3 n)$ (Miller-Rabin)", color='purple')
plt.plot(n, log6_n, label=r"$O(\log^6 n)$ (AKS)", color='orange')

# Adding labels and title
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Input Size (n)")
plt.ylabel("Time Complexity (log scale)")
plt.title("Vergleich von Laufzeiten der Primzahltests")
plt.legend()

plt.grid(True, which="both", ls="--")
plt.show()