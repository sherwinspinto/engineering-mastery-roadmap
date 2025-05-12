# Chapter 02 – What is an Eigenvalue?

## 🎯 Objective

To understand what an **eigenvalue** represents in a matrix transformation and how it relates to the behavior of eigenvectors.

---

## 🔍 Definition

If $$$vec{v}$ is an eigenvector of matrix $A$, then its eigenvalue $$$lambda$ satisfies:

$$
A $$vec{v} = $$lambda $$vec{v}
$$

This means $$$vec{v}$ maintains its direction, and $$$lambda$ tells you **how much it stretches or compresses**.

---

## 📈 Geometric Meaning

* $$$lambda > 1$: vector is stretched (longer)
* $0 < $$lambda < 1$: vector is shrunk (shorter)
* $$$lambda = 1$: vector is unchanged in length
* $$$lambda = 0$: vector collapses to zero (nullspace)
* $$$lambda < 0$: vector flips direction (reflection)

The **sign and magnitude** of $$$lambda$ encode transformation behavior.

---

## 🧮 Example

Let:

$$
A = $$begin{bmatrix} 4 & 0 $$$$ 0 & 2 $$end{bmatrix},$$quad $$vec{v}_1 = $$begin{bmatrix}1 $$$$ 0$$end{bmatrix},$$quad $$vec{v}_2 = $$begin{bmatrix}0 $$$$ 1$$end{bmatrix}
$$

Then:

$$
A $$vec{v}_1 = $$begin{bmatrix}4 $$$$ 0$$end{bmatrix} = 4 $$cdot $$vec{v}_1 $$Rightarrow $$lambda_1 = 4
$$

$$
A $$vec{v}_2 = $$begin{bmatrix}0 $$$$ 2$$end{bmatrix} = 2 $$cdot $$vec{v}_2 $$Rightarrow $$lambda_2 = 2
$$

So $$$vec{v}_1$ and $$$vec{v}_2$ are eigenvectors with eigenvalues 4 and 2, respectively.

---

## 🧠 Key Takeaways

* Eigenvalues describe **how eigenvectors scale** under a transformation
* They are specific to a matrix and its structure
* Each matrix has zero or more real eigenvalues (sometimes complex)

---

## 🧪 Exercises

1. For $A = $$begin{bmatrix} 2 & 0 $$$$ 0 & 3 $$end{bmatrix}$, what are the eigenvalues?
2. Try computing the effect of negative eigenvalues on vectors
3. Experiment with plotting $A $$vec{v}$ vs $$$lambda $$vec{v}$
