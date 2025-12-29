# Solutions to Practice Problems

## Problem 1
**Given:** \(I = 0.650\ \text{A}\), \(t = 30.0\ \text{min} = 1800\ \text{s}\), \(m_{\text{exp}} = 0.385\ \text{g}\)

### a) Total charge
\[
Q = I \cdot t = 0.650 \times 1800 = 1170\ \text{C}
\]

### b) Theoretical mass (Faraday’s law)
\[
m_{\text{theor}} = \frac{Q \cdot M}{n F}
= \frac{1170 \times 63.546}{2 \times 96485.3}
\]
First compute numerator: \(1170 \times 63.546 = 74 348.82\)
Denominator: \(2 \times 96485.3 = 192 970.6\)
\[
m_{\text{theor}} = \frac{74 348.82}{192 970.6} \approx 0.3853\ \text{g}
\]

### c) Percent efficiency
\[
\text{Efficiency} = \frac{m_{\text{exp}}}{m_{\text{theor}}} \times 100
= \frac{0.385}{0.3853} \times 100 \approx 99.9\%
\]

**Answer:**  
a) \(1170\ \text{C}\)  
b) \(0.385\ \text{g}\) (rounded to three significant figures)  
c) \(99.9\%\)

---

## Problem 2
**Given:** cathode gain = \(0.124\ \text{g}\), anode loss = \(0.118\ \text{g}\)

### a) Moles of copper deposited
\[
n_{\text{cathode}} = \frac{0.124}{63.546} \approx 0.001951\ \text{mol}
\]

### b) Moles of copper dissolved
\[
n_{\text{anode}} = \frac{0.118}{63.546} \approx 0.001857\ \text{mol}
\]

### c) Discrepancy explanation
The cathode gained slightly more copper than the anode lost (difference ≈ 0.006 g). Possible reasons:
- Measurement uncertainty in weighing (balances have finite precision).
- Some of the anode mass loss could be due to formation of copper oxide (CuO or Cu₂O) that adheres to the electrode or falls off as a solid, not entering the solution as Cu²⁺.
- Small side reactions at the cathode (e.g., hydrogen evolution) would not affect the cathode mass but would reduce the current efficiency for copper deposition, making the cathode gain less than expected—opposite to what is observed. Hence, the most likely cause is a combination of weighing errors and possible partial oxidation of the anode to solid products that are not fully accounted for.

**Answer:**  
a) \(1.95 \times 10^{-3}\ \text{mol}\)  
b) \(1.86 \times 10^{-3}\ \text{mol}\)  
c) See explanation above.

---

## Problem 3
**Given:** \(t = 2.00\ \text{h} = 7200\ \text{s}\), \(m_{\text{dep}} = 1.52\ \text{g}\)

### a) Total charge required
From Faraday’s law rearranged:
\[
Q = \frac{m \cdot n F}{M}
= \frac{1.52 \times 2 \times 96485.3}{63.546}
\]
Compute stepwise:  
\(1.52 \times 2 = 3.04\)  
\(3.04 \times 96485.3 = 293 338.3\)  
\(293 338.3 / 63.546 \approx 4615.6\ \text{C}\)

### b) Current magnitude
\[
I = \frac{Q}{t} = \frac{4615.6}{7200} \approx 0.641\ \text{A}
\]

### c) Moles of H₂ from same charge
For water electrolysis, \(2\ \text{e}^{-}\) per H₂ molecule ⇒ \(n = 2\).  
Faraday’s law for hydrogen: \(m_{\text{H₂}} = \frac{Q \cdot M_{\text{H₂}}}{n F}\), but we can directly compute moles:
\[
\text{moles of H₂} = \frac{Q}{n F} = \frac{4615.6}{2 \times 96485.3} \approx 0.0239\ \text{mol}
\]
At STP (0 °C, 1 atm), 1 mole of gas occupies 22.4 L, so volume ≈ \(0.0239 \times 22.4 = 0.535\ \text{L}\).

**Answer:**  
a) \(4.62 \times 10^{3}\ \text{C}\)  
b) \(0.641\ \text{A}\)  
c) \(0.0239\ \text{mol}\) (≈ 0.536 L at STP)

---

## Problem 4
**Given:** average current \(I_{\text{avg}} = 0.785\ \text{A}\), \(t = 45.0\ \text{min} = 2700\ \text{s}\)

### Charge passed
\[
Q = I_{\text{avg}} \cdot t = 0.785 \times 2700 = 2119.5\ \text{C}
\]

### Theoretical mass of copper
\[
m = \frac{Q \cdot M}{n F}
= \frac{2119.5 \times 63.546}{2 \times 96485.3}
\]
Numerator: \(2119.5 \times 63.546 \approx 134 684.5\)  
Denominator: \(192 970.6\)  
\[
m \approx \frac{134 684.5}{192 970.6} \approx 0.698\ \text{g}
\]

**Answer:** \(0.698\ \text{g}\) (rounded to three significant figures)

---

## Problem 5 (Challenge)
**Given:** reversed connections, \(I = 0.500\ \text{A}\), \(t = 20.0\ \text{min} = 1200\ \text{s}\), initial masses = \(5.000\ \text{g}\) each.

### a) Half‑reactions with reversed polarity
- **New anode (formerly cathode):** Copper oxidation  
  \(\mathrm{Cu_{(s)} \rightarrow Cu^{2+}_{(aq)} + 2 e^{-}}\)
- **New cathode (formerly anode):** Copper reduction  
  \(\mathrm{Cu^{2+}_{(aq)} + 2 e^{-} \rightarrow Cu_{(s)}}\)

The reactions are *identical* to the normal case, but the electrodes swap roles. The electrode that was originally the cathode (already coated with copper) will now dissolve, and the electrode that was originally the anode (already partially dissolved) will now receive a deposit.

### b) Mass changes
The amount of copper transferred is determined by the charge passed:
\[
Q = I \cdot t = 0.500 \times 1200 = 600\ \text{C}
\]
Mass transferred:
\[
\Delta m = \frac{Q \cdot M}{n F}
= \frac{600 \times 63.546}{2 \times 96485.3}
\approx \frac{38 127.6}{192 970.6} \approx 0.1976\ \text{g}
\]

Therefore:
- The **new anode** (original cathode) loses \(0.1976\ \text{g}\).
- The **new cathode** (original anode) gains \(0.1976\ \text{g}\).

### c) Final masses
- **Electrode that started as cathode (now anode):**  
  Initial \(5.000\ \text{g}\) – loss \(0.1976\ \text{g}\) = \(4.802\ \text{g}\)
- **Electrode that started as anode (now cathode):**  
  Initial \(5.000\ \text{g}\) + gain \(0.1976\ \text{g}\) = \(5.198\ \text{g}\)

**Answer:**  
a) Same half‑reactions as normal, but electrodes swapped.  
b) Each electrode changes mass by \(0.198\ \text{g}\) (one loses, one gains).  
c) Final masses: \(4.80\ \text{g}\) and \(5.20\ \text{g}\) (rounded to three significant figures).

---

**Note:** All calculations use the values of constants as given. Slight variations may arise from rounding at intermediate steps.