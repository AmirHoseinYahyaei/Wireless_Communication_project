import numpy as np
import matplotlib.pyplot as plt
import math

# -------------------------------
# 1. Project Parameters
# -------------------------------

N = 100000

P0 = 0.2
P1 = 0.8

SNR_dB = [0, 2, 4, 6, 8, 10, 12]

rng = np.random.default_rng()

BER_ML = []
BER_MAP = []

BER_ML_theory = []
BER_MAP_theory = []

saved_data = None


# -------------------------------
# 2. Q Function
# -------------------------------

def Q(x):
    return 0.5 * math.erfc(x / math.sqrt(2))


# -------------------------------
# 3. BER Simulation
# -------------------------------

for snr in SNR_dB:

    snr_linear = 10 ** (snr / 10)

    sigma = np.sqrt(1 / (2 * snr_linear))

    # Generate random bits
    bits = rng.choice([0, 1], size=N, p=[P0, P1])

    # BPSK Modulation
    transmitted = 2 * bits - 1

    # AWGN Channel
    noise = rng.normal(0, sigma, N)

    received = transmitted + noise

    # ML Receiver
    detected_ML = (received > 0).astype(int)

    # MAP Threshold
    threshold_MAP = (sigma ** 2 / 2) * np.log(P0 / P1)

    # MAP Receiver
    detected_MAP = (received > threshold_MAP).astype(int)

    # Calculate Errors
    errors_ML = np.sum(bits != detected_ML)
    errors_MAP = np.sum(bits != detected_MAP)

    # Calculate Experimental BER
    ber_ml = errors_ML / N
    ber_map = errors_MAP / N

    BER_ML.append(ber_ml)
    BER_MAP.append(ber_map)

    # Calculate Theoretical BER
    ber_ml_th = Q(1 / sigma)

    ber_map_th = (
        P0 * Q((threshold_MAP + 1) / sigma)
        +
        P1 * Q((1 - threshold_MAP) / sigma)
    )

    BER_ML_theory.append(ber_ml_th)
    BER_MAP_theory.append(ber_map_th)

    # Print Results
    print("--------------------------------")
    print("SNR =", snr, "dB")

    print("ML Errors =", errors_ML)
    print("ML Experimental BER =", ber_ml)
    print("ML Theoretical BER =", ber_ml_th)

    print("MAP Errors =", errors_MAP)
    print("MAP Experimental BER =", ber_map)
    print("MAP Theoretical BER =", ber_map_th)

    # Save data at SNR = 6 dB
    if snr == 6:

        saved_data = (
            bits[:20],
            transmitted[:20],
            received[:20],
            detected_ML[:20],
            detected_MAP[:20],
            threshold_MAP
        )


# -------------------------------
# 4. BER Comparison Plot
# -------------------------------

plot_floor = 0.5 / N

BER_ML_plot = np.maximum(BER_ML, plot_floor)
BER_MAP_plot = np.maximum(BER_MAP, plot_floor)

plt.figure(figsize=(10, 7))

plt.semilogy(
    SNR_dB,
    BER_ML_plot,
    'o-',
    label='ML Experimental'
)

plt.semilogy(
    SNR_dB,
    BER_MAP_plot,
    's-',
    label='MAP Experimental'
)

plt.semilogy(
    SNR_dB,
    BER_ML_theory,
    '--',
    label='ML Theoretical'
)

plt.semilogy(
    SNR_dB,
    BER_MAP_theory,
    '--',
    label='MAP Theoretical'
)

# Mark zero-error experimental points
for i in range(len(SNR_dB)):

    if BER_ML[i] == 0:
        plt.scatter(
            SNR_dB[i],
            plot_floor,
            marker='v',
            facecolors='none',
            edgecolors='blue'
        )

    if BER_MAP[i] == 0:
        plt.scatter(
            SNR_dB[i],
            plot_floor,
            marker='v',
            facecolors='none',
            edgecolors='orange'
        )

plt.xlabel('SNR (dB)')
plt.ylabel('Bit Error Rate (BER)')

plt.title('Experimental and Theoretical BER Comparison')

plt.grid(True, which='both')
plt.legend()
plt.tight_layout()
plt.show()


# -------------------------------
# 5. Signal Visualization
# -------------------------------

bits, transmitted, received, detected_ML, detected_MAP, threshold_MAP = saved_data

time = np.arange(20)

plt.figure(figsize=(12, 9))

# Original Bits
plt.subplot(2, 2, 1)

plt.step(time, bits, where='mid')

plt.title('Original Binary Data')
plt.xlabel('Sample')
plt.ylabel('Bit')
plt.yticks([0, 1])
plt.grid(True)


# Transmitted BPSK Signal
plt.subplot(2, 2, 2)

plt.stem(time, transmitted)

plt.title('Transmitted BPSK Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid(True)


# Received Signal
plt.subplot(2, 2, 3)

plt.stem(time, received)

plt.axhline(
    0,
    color='red',
    linestyle='--',
    label='ML Threshold'
)

plt.axhline(
    threshold_MAP,
    color='green',
    linestyle='--',
    label='MAP Threshold'
)

plt.title('Received Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)


# Receiver Decisions
plt.subplot(2, 2, 4)

plt.step(
    time,
    detected_ML,
    where='mid',
    label='ML Decisions'
)

plt.step(
    time,
    detected_MAP,
    where='mid',
    linestyle='--',
    label='MAP Decisions'
)

plt.title('Receiver Decisions')
plt.xlabel('Sample')
plt.ylabel('Detected Bit')
plt.yticks([0, 1])
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


# -------------------------------
# 6. Final Comparison at 6 dB
# -------------------------------

index = SNR_dB.index(6)

print("\n========== FINAL RESULTS ==========")

print("SNR = 6 dB")

print("ML Experimental BER =", BER_ML[index])
print("ML Theoretical BER =", BER_ML_theory[index])

print("MAP Experimental BER =", BER_MAP[index])
print("MAP Theoretical BER =", BER_MAP_theory[index])

print("ML Threshold = 0")

print("MAP Threshold =", saved_data[5])

print("===================================")
