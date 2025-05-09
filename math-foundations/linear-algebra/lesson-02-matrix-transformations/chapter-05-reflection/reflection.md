# Chapter 05 – Reflection

## 🎯 Objective
Learn how reflection matrices flip vectors across axes or lines, reversing orientation but preserving length and angles.

---

## 📌 Key Concepts

### 1. Reflection Across x-axis
$$
A = \begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
$$
- Flips vectors vertically
- Preserves x-coordinates
- Reverses orientation (det = -1)

---

### 2. Reflection Across y-axis
$$
A = \begin{bmatrix}
-1 & 0 \\
0 & 1
\end{bmatrix}
$$
- Flips vectors horizontally
- Preserves y-coordinates

---

### 3. Reflection Across Line $ y = x $
$$
A = \begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}
$$
- Swaps x and y
- This is a common symmetry operation

---

### 4. Geometric Properties
- **Length is preserved**
- **Area is preserved** in magnitude but not orientation (det = -1)
- **Orientation is flipped** (clockwise → counterclockwise)

---

## 🧪 Suggested Exercises

1. Reflect the vector $ [2, 1] $ across:
    - x-axis
    - y-axis
    - line $ y = x $

2. Apply these reflections to the unit square

3. Try combinations like:
    - Reflect across x-axis, then y-axis
    - Compare with rotation by 180°

---

## 🔁 Next Steps
Advance to **Chapter 06 – Composition of Transformations**, where you’ll explore chaining multiple matrix transformations together and interpreting the result.