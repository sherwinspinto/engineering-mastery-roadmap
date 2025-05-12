## 🔢 Finding Eigenvalues and Eigenvectors of A

Given:

$$
A = \begin{bmatrix} 2 & 1 \\
0 & 3 \end{bmatrix}
$$

---

### ✅ Step 1: Characteristic Equation

We solve:

$$
\det(A - \lambda I) = 0
$$

$$
A - \lambda I = \begin{bmatrix}
2 - \lambda & 1 \\
0 & 3 - \lambda
\end{bmatrix}
$$

$$
\det(A - \lambda I) = (2 - \lambda)(3 - \lambda) - 0 = (2 - \lambda)(3 - \lambda)
$$

$$
\Rightarrow \lambda_1 = 2, \quad \lambda_2 = 3
$$

---

### ✅ Step 2: Eigenvectors

#### ◾ For $$ \lambda = 2 $$:

$$
A - 2I = \begin{bmatrix} 0 & 1 \\
0 & 1 \end{bmatrix}
$$

Solve:

$$
\begin{bmatrix} 0 & 1 \\
0 & 1 \end{bmatrix}
\begin{bmatrix} x \\
y \end{bmatrix}
=
\begin{bmatrix} 0 \\
0 \end{bmatrix}
\Rightarrow y = 0
$$

$$
\vec{v}_1 = \begin{bmatrix} x \\
0 \end{bmatrix} \Rightarrow
\text{Eigenvector: } \begin{bmatrix} 1 \\
0 \end{bmatrix}
$$

---

#### ◾ For $$ \lambda = 3 $$:

$$
A - 3I = \begin{bmatrix} -1 & 1 \\
0 & 0 \end{bmatrix}
$$

Solve:

$$
\begin{bmatrix} -1 & 1 \\
0 & 0 \end{bmatrix}
\begin{bmatrix} x \\
y \end{bmatrix}
=
\begin{bmatrix} 0 \\
0 \end{bmatrix}
\Rightarrow -x + y = 0 \Rightarrow y = x
$$

$$
\vec{v}_2 = \begin{bmatrix} x \\
x \end{bmatrix} \Rightarrow
\text{Eigenvector: } \begin{bmatrix} 1 \\
1 \end{bmatrix}
$$

---

### ✅ Final Summary:

- $$ \lambda = 2 $$ → $$ \vec{v}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix} $$
- $$ \lambda = 3 $$ → $$ \vec{v}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix} $$