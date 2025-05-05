# Chapter 01 – What is a Matrix Transformation?

## 🎯 Objective
To understand a **matrix** as a **function** that transforms a vector into a new one—changing its direction, magnitude, or both.

---

## 📌 Key Concepts

### 1. Matrix as a Function
If $ \text{A} $ is a matrix and $ \vec{x} $ is a vector, then:

$ A \vec{x} = \vec{y} $

This operation maps input $ \vec{x} $ to output $ \vec{y} $. This is the essence of a transformation.

---

### 2. Standard Basis Interpretation
Each **column** of a 2×2 matrix tells us where the standard basis vectors $ \vec{e}_1 = [1, 0]^T $ and $ \vec{e}_2 = [0, 1]^T $ are sent.

- First column → where $ \vec{e}_1 $ ends up
- Second column → where $ \vec{e}_2 $ ends up

---

### 3. Identity Matrix: The Do-Nothing Transform
$$
I = \begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}
$$

Applying $ I \vec{x} $ yields $ \vec{x} $. No change: this helps contrast with more meaningful transformations.

---

### 4. Visualizing the Effect
Use a simple grid or square (like the unit square with vertices at (0,0), (1,0), (0,1), and (1,1)).

Apply a matrix $ A $ to each corner:
- Plot the original and transformed versions
- Observe how the space is stretched, skewed, or rotated

---

## 🧪 Suggested Exercise (Python/Geogebra)

Try applying the matrix:

```python
A = np.array([[2, 0],
              [1, 1]])