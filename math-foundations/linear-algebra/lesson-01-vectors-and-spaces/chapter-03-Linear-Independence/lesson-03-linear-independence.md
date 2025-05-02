# Chapter 03 – Linear Independence

This chapter covers the concept of **linear independence**, how to test for it algebraically and visually, and why it is foundational to basis and dimensionality.

---

## 1️⃣ What is Linear Independence?

A set of vectors is **linearly independent** if no vector in the set can be written as a linear combination of the others.

If:
$$
a_1 \vec{v}_1 + a_2 \vec{v}_2 + \dots + a_n \vec{v}_n = \vec{0}
$$
only has the **trivial solution** $ a_1 = a_2 = \dots = a_n = 0 $, then the set is independent.

---

## 2️⃣ Visual and Algebraic Interpretation

- In ℝ² or ℝ³, visualize vectors forming a “V” or lying in different directions.
- In algebra, solve the linear dependence equation above.

---

## 3️⃣ Testing for Independence

- For small sets: manually solve the zero-vector equation.
- For large sets: use matrix rank or row reduction techniques.

---

## 4️⃣ Redundant Sets and Basis Pruning

- If a vector in a spanning set is a combination of others, it can be removed.
- Pruning down to a minimal independent set gives a **basis**.

---

## 5️⃣ Summary Table

| Concept               | Definition / Key Idea                                                                |
|-----------------------|--------------------------------------------------------------------------------------|
| Linear Independence   | No vector in the set is a linear combination of the others                           |
| Linear Dependence     | At least one vector **can** be expressed as a combination of the others              |
| Trivial Solution      | $ a_1 = a_2 = \dots = a_n = 0 $; required for independence                         |
| Redundant Vectors     | Vectors that do not add new span; can be removed                                     |
| Basis                 | Minimal spanning set — linearly independent and spanning the space                   |
| Algebraic Test        | Solve $ a_1 \vec{v}_1 + \dots + a_n \vec{v}_n = \vec{0} $; check for trivial only  |
| Visual Test (2D/3D)   | Vectors form a “V” or spread in 3D ⇒ independent; lie on same line/plane ⇒ dependent |
| Matrix Test (row ops) | If all columns have pivots → independent; missing pivot → dependent                  |