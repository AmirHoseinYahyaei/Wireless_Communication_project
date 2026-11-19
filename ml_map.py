import numpy as np
import matplotlib.pyplot as plt

N = 100000

bits = np.random.randint(0, 2, N)
signal = 2 * bits - 1
snr_db = 6
snr = 10 ** (snr_db / 10)
sigma = np.sqrt(1 / (2 * snr))
noise = sigma * np.random.randn(N)
received = signal + noise

ml_bits = (received >= 0).astype(int)
ml_errors = np.sum(bits != ml_bits)
ml_ber = ml_errors / N

print("Original bits:", bits[:20])
print("Transmitted signal:", signal[:20])
print("Received signal:", received[:20])
print("\nML Receiver Results")
print("Number of errors:", ml_errors)
print("BER:", ml_ber)

p0 = 0.2
p1 = 0.8

bits_map = np.random.choice([0, 1], N, p=[p0, p1])
signal_map = 2 * bits_map - 1
noise_map = sigma * np.random.randn(N)
received_map = signal_map + noise_map

threshold = (sigma ** 2 / 2) * np.log(p0 / p1)

map_bits = (received_map > threshold).astype(int)
map_errors = np.sum(bits_map != map_bits)
map_ber = map_errors / N

ml_bits_map = (received_map >= 0).astype(int)
ml_errors_map = np.sum(bits_map != ml_bits_map)
ml_ber_map = ml_errors_map / N

print("\nMAP Receiver Results")
print("MAP Threshold:", threshold)
print("MAP Number of Errors:", map_errors)
print("MAP BER:", map_ber)

print("\nML Receiver Results (Unequal Probabilities)")
print("ML Number of Errors:", ml_errors_map)
print("ML BER:", ml_ber_map)

snr_values = np.arange(0, 14, 2)
ber_ml_values = []
ber_map_values = []

for snr_db in snr_values:
    snr = 10 ** (snr_db / 10)
    sigma = np.sqrt(1 / (2 * snr))

    bits = np.random.choice([0, 1], N, p=[p0, p1])
    signal = 2 * bits - 1
    received = signal + sigma * np.random.randn(N)

    ml_bits = (received >= 0).astype(int)
    threshold = (sigma ** 2 / 2) * np.log(p0 / p1)
    map_bits = (received > threshold).astype(int)

    ber_ml_values.append(np.mean(bits != ml_bits))
    ber_map_values.append(np.mean(bits != map_bits))

print("\nBER vs SNR Results")

for i in range(len(snr_values)):
    print("SNR:", snr_values[i],
          "ML BER:", ber_ml_values[i],
          "MAP BER:", ber_map_values[i])

plt.figure(figsize=(9, 5))
plt.semilogy(snr_values, ber_ml_values, 'o-', label='ML')
plt.semilogy(snr_values, ber_map_values, 's-', label='MAP')
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BER Comparison of ML and MAP Receivers")
plt.grid(True, which="both")
plt.legend()
plt.show()

N_vis = 30
bits_vis = np.random.choice([0, 1], N_vis, p=[p0, p1])
signal_vis = 2 * bits_vis - 1
snr_vis = 10 ** (6 / 10)
sigma_vis = np.sqrt(1 / (2 * snr_vis))
received_vis = signal_vis + sigma_vis * np.random.randn(N_vis)

ml_vis = (received_vis >= 0).astype(int)
threshold_vis = (sigma_vis ** 2 / 2) * np.log(p0 / p1)
map_vis = (received_vis > threshold_vis).astype(int)

x = np.arange(20)
fig, ax = plt.subplots(3, 1, figsize=(10, 9))

ax[0].step(x, bits_vis[:20], where='mid')
ax[0].set_title("Original Bits")
ax[0].set_ylabel("Bit")
ax[0].grid(True)

ax[1].plot(x, signal_vis[:20], 'o-', label='Transmitted')
ax[1].plot(x, received_vis[:20], 's-', label='Received')
ax[1].axhline(0, linestyle='--', label='ML Threshold')
ax[1].axhline(threshold_vis, linestyle=':', label='MAP Threshold')
ax[1].set_title("Transmitted and Received Signals")
ax[1].set_ylabel("Amplitude")
ax[1].legend()
ax[1].grid(True)

ax[2].step(x, bits_vis[:20], where='mid', label='Original')
ax[2].step(x, ml_vis[:20], where='mid', linestyle='--', label='ML')
ax[2].step(x, map_vis[:20], where='mid', linestyle=':', label='MAP')
ax[2].set_title("Receiver Decisions")
ax[2].set_xlabel("Bit Number")
ax[2].set_ylabel("Bit")
ax[2].legend()
ax[2].grid(True)

plt.tight_layout()
plt.show()