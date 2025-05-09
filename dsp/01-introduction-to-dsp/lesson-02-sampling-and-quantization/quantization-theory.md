# 📘 Quantization Theory – Derivations

This document contains the mathematical derivation of key formulas related to quantization noise power and SQNR (Signal-to-Quantization-Noise Ratio).

---

## 📐 1. Quantization Noise Power

### Assumptions:
- Uniform quantizer with step size $ \Delta $
- Quantization error $ e_q \in [-\Delta/2, \Delta/2] $
- Error is uniformly distributed and uncorrelated with the signal

### Derivation:
The variance of a uniform distribution over an interval of width $ \Delta $ is:

$$
\sigma^2 = \frac{\Delta^2}{12}
$$

Since the quantization error has zero mean, the average **power** of the error is:

$$
P_q = \frac{\Delta^2}{12}
$$

---

## 📊 2. Signal-to-Quantization-Noise Ratio (SQNR)

### For a full-scale sinusoidal input:
Let the signal be $ x(t) = A \cdot \sin(2\pi f t) $

Its average power is:

$$
P_{\text{signal}} = \frac{A^2}{2}
$$

Step size for a uniform quantizer with $ 2^B $ levels across $ [-A, +A] $:

$$
\Delta = \frac{2A}{2^B} = \frac{A}{2^{B-1}}
$$

So, quantization noise power is:

$$
P_q = \frac{\Delta^2}{12} = \frac{A^2}{3 \cdot 2^{2B}}
$$

### SQNR expression:
$$
\text{SQNR} = \frac{P_{\text{signal}}}{P_q} = \frac{\frac{A^2}{2}}{\frac{A^2}{3 \cdot 2^{2B}}} = \frac{3 \cdot 2^{2B}}{2}
$$

Convert to dB:

$$
\text{SQNR}_{\text{dB}} = 10 \log_{10}\left(\frac{3 \cdot 2^{2B}}{2}\right)
= 10 \log_{10}(1.5) + 20B \log_{10}(2)
$$

$$
\approx 1.76 + 6.02B
$$

---

### ✅ Final Result:
$$
\boxed{\text{SQNR}_{\text{dB}} \approx 6.02B + 1.76}
$$

This relationship shows why each additional bit improves SQNR by approximately 6 dB.

---

