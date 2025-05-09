# Chapter 04 – Shearing

## 🎯 Objective

Understand how shear matrices deform shapes by sliding them along one axis while keeping the other axis fixed.

---

## 📌 Key Concepts

### 1. What Is Shearing?

A shear transformation **slants** the shape:

- It **preserves area** (if determinant = 1)
- It **distorts angles**
- Vectors no longer remain orthogonal

---

### 2. Shear Matrices

#### Horizontal Shear (x-axis shear):

$$
A = \begin{bmatrix}
1 & k \\
0 & 1
\end{bmatrix}
$$

#### Vertical Shear (y-axis shear):

$$
A = \begin{bmatrix}
1 & 0 \\
k & 1
\end{bmatrix}
$$

- $ k $ is the **shear factor**
- If $ k = 0 $, the matrix becomes the identity

---

### 3. Example: Horizontal Shear with $ k = 1 $

Apply to unit square points:

- (0,0) → (0,0)
- (1,0) → (1,0)
- (0,1) → (1,1)
- (1,1) → (2,1)

The square becomes a **parallelogram**.

---

### 4. Determinant and Area

$$
\det\left(\begin{bmatrix}1 & k \\ 0 & 1\end{bmatrix}\right) = 1
$$

So the **area is preserved**, but the shape and angles change.

---

## 🧪 Suggested Exercises

1. Apply $ A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} $ to:

   - [1, 0]
   - [0, 1]
   - [1, 1]

2. Apply to the unit square and plot the transformation

3. Try different values of $ k $: e.g., -1, 0.5, 2

4. Compare shear to rotation and scaling visually

---

## 🔁 Next Steps

Move on to **Chapter 05 – Reflection** to explore how matrices can flip vectors over axes or lines.

