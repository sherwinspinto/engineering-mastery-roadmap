# Chapter 02 – Scaling and Stretching

## 🎯 Objective
Understand how **diagonal matrices** scale vectors and stretch or compress space along specific axes.

---

## 📌 Key Concepts

### 1. Diagonal Matrices and Axis-Aligned Scaling
A matrix like:

$$
A = \begin{bmatrix} 2 & 0 \\
0 & 3 \end{bmatrix}
$$

- Scales \( x \)-coordinates by 2
- Scales \( y \)-coordinates by 3

This stretches the space **horizontally** by 2 and **vertically** by 3.

---

### 2. Uniform vs Non-uniform Scaling
- **Uniform scaling**: Same factor in all directions  
  Example:  
  $$
  \begin{bmatrix}2 & 0 \\
  0 & 2\end{bmatrix}
  $$

- **Non-uniform scaling**: Different factors per axis  
  Example:  
  $$
  \begin{bmatrix}2 & 0 \\
  0 & 1\end{bmatrix}
  $$

This distinction is key for understanding anisotropic behavior in physical systems.

---

### 3. Effect on Unit Square
Take the unit square with vertices: (0,0), (1,0), (1,1), (0,1)  
Apply the matrix \( A \) to each vertex:

- (1,0) → (2,0)
- (1,1) → (2,3)
- (0,1) → (0,3)

The square becomes a **rectangle** or **parallelogram**, scaled along the coordinate axes.

---

### 4. Determinant as Area Scale
The **determinant** of a 2×2 matrix tells us **how much the area scales** under the transformation:

$$
\text{Area Scale} = \det(A)
$$

Example:
$$
\det\left(\begin{bmatrix}2 & 0 \\
0 & 3\end{bmatrix}\right) = 6
$$

The transformed square has **6× the area** of the original.

---

## 🧪 Suggested Exercises

1. Apply  
   $$
   A = \begin{bmatrix}2 & 0 \\
   0 & 3\end{bmatrix}
   $$  
   to the following vectors:
    - [1, 0]
    - [0, 1]
    - [1, 1]
    - [-1, 1]

2. Plot the unit square before and after applying the matrix. Observe how it stretches.

3. Try a **shrinking matrix**:  
   $$
   A = \begin{bmatrix}0.5 & 0 \\
   0 & 0.5\end{bmatrix}
   $$  
   What happens to vector lengths and the area?

---

## 🔁 Next Steps
Continue to **Chapter 03 – Rotation** to explore how matrices rotate space using trigonometry.