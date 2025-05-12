# Chapter 01 – What is an Eigenvector?

## 🔍 Intuition

An **eigenvector** of a matrix is a non-zero vector that, when transformed by the matrix, does not change direction — only its magnitude may change. Formally:

$$
A \vec{v} = \lambda \vec{v}
$$

* $A$: a square matrix
* $\vec{v}$: the eigenvector (non-zero)
* $\lambda$: the eigenvalue (scalar multiplier)

This means that applying the matrix to $\vec{v}$ results in a new vector that is a **scaled version** of $\vec{v}$ — it lies on the same line (direction).

---

## 📈 Geometric Meaning

In 2D:

* Most vectors **rotate and scale** under matrix transformation
* **Eigenvectors** only **scale** — their **direction remains unchanged**

Think of eigenvectors as the **stable axes** of the transformation.

---

## 🧮 Basic Example

Let’s consider a simple matrix:

$$
A = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}
$$

Apply it to $\vec{v}_1 = [1, 0]$:

$$
A \vec{v}_1 = \begin{bmatrix} 3 \\ 0 \end{bmatrix} = 3 \cdot \vec{v}_1
$$

This confirms $\vec{v}_1$ is an eigenvector with eigenvalue $\lambda = 3$.

Apply to $\vec{v}_2 = [0, 1]$:

$$
A \vec{v}_2 = \begin{bmatrix} 0 \\ 2 \end{bmatrix} = 2 \cdot \vec{v}_2
$$

Another eigenvector, this time with $\lambda = 2$.

---

## 🧠 Key Takeaways

* An eigenvector is unchanged in **direction** under transformation
* The eigenvalue tells you **how much it scales**
* All scalar multiples of an eigenvector are also eigenvectors

---

## 🔁 Up Next

We’ll now explore what an **eigenvalue** is, how to interpret it, and how to compute it from a matrix.

➡️ Go to Chapter 02 – What is an Eigenvalue?
