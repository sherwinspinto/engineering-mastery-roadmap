# Chapter 03 – Rotation

## 🎯 Objective
Understand how matrices can **rotate vectors** in 2D space, how they relate to trigonometry, and how they preserve length and orientation.

---

## 📌 Key Concepts

### 1. The Rotation Matrix
The 2D rotation matrix for an angle $ \theta $ is:

$$
R(\theta) = \begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
$$

- Rotates vectors counterclockwise by angle $ \theta $
- Preserves **length** and **area** (determinant = 1)

---

### 2. Example: 90° Rotation
Use $ \theta = \frac{\pi}{2} $:

$$
R(\pi/2) = \begin{bmatrix} 0 & -1 \\
1 &  0 \end{bmatrix}
$$

Apply it to $ [1, 0] $:

$$
\begin{bmatrix} 0 & -1 \\
1 &  0 \end{bmatrix}
\begin{bmatrix} 1 \\
0 \end{bmatrix}
= \begin{bmatrix} 0 \\
1 \end{bmatrix}
$$

The vector rotates from the x-axis to the y-axis.

---

### 3. Composition of Rotations
Rotating by $ \theta_1 $ then $ \theta_2 $ is equivalent to:

$$
R(\theta_2) \cdot R(\theta_1) = R(\theta_1 + \theta_2)
$$

Matrix multiplication of two rotation matrices is still a rotation.

---

### 4. Visualization Tips
- Plot the original vector and the rotated one
- Use different angles: 45°, 90°, 180°
- Observe that **lengths remain the same**, only **direction changes**

---

## 🧪 Suggested Exercises

1. Apply $ R(\pi/4) $ to the vector $ [1, 0] $
2. Try rotating a square (4 points) by 90° and 180°
3. Combine two rotations and compare to a single one with the summed angle
4. Animate a vector rotating through $ 0 \rightarrow 2\pi $

---

## 🔁 Next Steps
Proceed to **Chapter 04 – Shearing** to learn how matrices can slant space without scaling or rotating it.