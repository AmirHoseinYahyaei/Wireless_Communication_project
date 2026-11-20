ML and MAP Receiver Simulation

Project Description

This project simulates and compares two digital communication detection methods:

- Maximum Likelihood (ML)
- Maximum A Posteriori (MAP)

The simulation uses BPSK modulation over an Additive White Gaussian Noise (AWGN) channel.

The main objective is to evaluate the performance of ML and MAP receivers by comparing their Bit Error Rate (BER) under different Signal-to-Noise Ratio (SNR) conditions.

Project Features

- Random binary data generation
- BPSK modulation
- AWGN channel simulation
- ML receiver implementation
- MAP receiver implementation
- Experimental BER calculation
- Theoretical BER calculation
- Comparison of experimental and theoretical results
- Signal visualization and decision diagrams
- Random results in each execution

Simulation Parameters

Parameter| Value
Number of bits| 100,000
Probability of bit 0| 0.2
Probability of bit 1| 0.8
Modulation| BPSK
Channel model| AWGN
SNR range| 0 to 12 dB
SNR step| 2 dB

Receiver Methods

1. Maximum Likelihood (ML)

The ML receiver makes its decision based on the received signal and selects the most likely transmitted symbol.

The decision threshold is:

Threshold = 0

2. Maximum A Posteriori (MAP)

The MAP receiver considers both the received signal and the prior probabilities of transmitted bits.

Its decision threshold is:

Threshold = (σ² / 2) × ln(P(0) / P(1))

Since the probabilities of bits 0 and 1 are different, the MAP receiver can achieve a lower error rate than the ML receiver.

Theoretical BER

The theoretical BER is calculated for both receivers and compared with the experimental simulation results.

The comparison helps evaluate the accuracy of the simulation and the performance of each detection method.

Project Structure

Wireless_Communication_project/
│
├── ml_map.py
├── requirements.txt
└── README.md

Requirements

The project requires Python and the following libraries:

- NumPy
- Matplotlib

Install the required libraries using:

pip install -r requirements.txt

How to Run

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Install the required libraries.
4. Run the following command:

python ml_map.py

Simulation Outputs

The program generates two main figures.

Figure 1: BER Comparison

This figure compares four curves:

- ML Experimental BER
- MAP Experimental BER
- ML Theoretical BER
- MAP Theoretical BER

Figure 2: Signal Visualization

This figure contains four subplots:

- Original Binary Data
- Transmitted BPSK Signal
- Received Signal
- Receiver Decisions

Conclusion

The simulation demonstrates that both ML and MAP receivers improve their performance as the SNR increases.

The MAP receiver generally achieves a lower BER because it takes the prior probabilities of transmitted bits into account.

The experimental results show good agreement with the theoretical calculations.

Author

Amir Hosein Yahyaei

Project: Wireless Communication
Topic: ML and MAP Receiver Simulation
