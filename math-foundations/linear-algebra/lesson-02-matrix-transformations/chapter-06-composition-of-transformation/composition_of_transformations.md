# Chapter 06 – Composition of Transformations

## 🎯 Objective

Understand how to **combine multiple matrix transformations** and interpret the resulting transformation as a single matrix.

---

## 📌 Key Concepts

### 1. Matrix Composition = Transformation Chaining

Given two matrices $A$ and $B$, the composition:

$$
C = B \cdot A
$$

means: apply $A$ **first**, then $B$.

* Matrix multiplication is **not commutative**:

  $$
  B \cdot A \ne A \cdot B
  $$
* The result $C$ is also a transformation matrix

---

### 2. Visual Interpretation

* Transform a shape with $A$, then take the result and apply $B$
* Compare the final result with directly applying $C = B \cdot A$
* This confirms the **composability** of linear transformations

---

### 3. Common Combinations

* **Scale then rotate** vs **rotate then scale**
* **Shear then reflect** vs **reflect then shear**
* Order impacts shape, direction, and orientation

---

### 4. Associativity of Matrix Multiplication

Although not commutative, matrix multiplication is **associative**:

$$
A \cdot (B \cdot C) = (A \cdot B) \cdot C
$$

This helps when chaining more than two transformations.

---

## 🧪 Suggested Exercises

1. Compose:

    * $A = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}$ (scale x by 2)
    * $B = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ (rotate 90°)
    * Compute $B \cdot A$ and apply it to a unit square

2. Try applying $A \cdot B$ instead — observe the difference

3. Combine a shear and a reflection:

    * Try both orders and compare results

4. Create a transformation that rotates then reflects — test on a triangle

---

## 🧭 Wrap-up

You've now seen how linear transformations behave individually and when chained.

Next up: we can begin applying these ideas to transformations in higher dimensions, eigendecomposition, or connect them to systems of equations and vector spaces.
