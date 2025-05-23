# 📘 Lesson 1: Vectors and Vector Spaces

## ✅ Learning Goals
By the end of this lesson, you should be able to:
- Understand what a vector is (geometrically and algebraically)
- Perform vector addition and scalar multiplication
- Understand linear combinations and span
- Grasp the concept of a vector space
- Identify common vector subspaces like ℝ² and ℝ³

---

## 1️⃣ What is a Vector?

### Algebraic View:
A vector is an **ordered list of numbers** representing a position or direction in space.
- Example:
  $$
  \vec{v} = [3, -1, 2] \in \mathbb{R}^3
  $$
- Algebraically, a vector is like a coordinate list or a directional instruction — but it doesn’t necessarily point to a location unless you define it with respect to the origin. 
- It’s not “where you are”, but “how to move” — 3 units in x, -1 unit in y, 2 units in z.

  
### Geometric View:
A vector can be visualized as an **arrow** from the origin, indicating **magnitude and direction**.

---

## 2️⃣ Vector Operations

### ➕ Vector Addition:
$$
\vec{u} = [1, 2], \quad \vec{v} = [3, -1]
$$

$$
\vec{u} + \vec{v} = [1 + 3, 2 + (-1)] = [4, 1]
$$

### ✖️ Scalar Multiplication:
$$
2 \cdot \vec{v} = 2 \cdot [3, -1] = [6, -2]
$$

---

## 3️⃣ Linear Combinations and Span

- A **linear combination** is any expression like:
  $$
  a_1\vec{v}_1 + a_2\vec{v}_2 + \dots + a_n\vec{v}_n
  $$

- The **span** of a set of vectors is the set of all vectors that can be formed by linear combinations of them.

  Example:
  $$
  \text{Span}(\{[1, 0], [0, 1]\}) = \mathbb{R}^2
  $$

  $$
  \text{Span}(\{[1, 1]\}) = \text{Line through origin at 45°}
  $$
- Example of a vector that lies in a span. \
 $ \vec{v}_1 = [2,1], \vec{v}_2 = [-1,1], \vec{w} = [1,3] $ \
We need to show that $\vec{w} = [1,3] $ is in the span of $ \vec{v}_1 = [2,1], \vec{v}_2 = [-1,1]$ \
so we solve for $a\vec{v}_1 + b\vec{v}_2 = \vec{w}$ \
i.e \
$ a[2,1] + b[-1,1] = [1,3] \:\: which \: gives \: us  \: a=\frac{4}{3} \: and \: b=\frac{5}{3} $ \
this means that $\vec{w}$ is in the span of $\vec{v_1} \: and \: \vec{v_2}$ \
  You can think of it like this:
  If you were standing at the origin and could only walk in the directions of $\vec{v}_1$ and $\vec{v}_2$, then yes — you could reach the point [1, 3] by walking $\frac{4}{3}$ steps in direction $\vec{v}_1$ and $\frac{5}{3}$ in direction $\vec{v}_2.$

  ![Real-world applications of span and linear combinations](A_grid_of_six_squares_presents_practical_examples_.png)
  

---

## 4️⃣ What is a Vector Space?

A **vector space** is a set of vectors closed under:
- Vector addition
- Scalar multiplication

It must satisfy **8 axioms** (associativity, identity, distributivity, etc.) — these will be explored in a later lesson.

🔧 Analogy

Think of:
-	**Vector space** definition = rulebook (like the rules of chess)
-	**Span of vectors** = specific pieces following those rules to reach certain positions
-	The span lives inside the larger space defined by the rules

<font color="red">So you don’t use the span after the vector space is defined — rather, span is how you generate actual subsets that are vector spaces, within a broader space (like ℝ³).</font>

### Common Examples:
- $ ( \mathbb{R}^n ) (Euclidean spaces)$
- Set of all polynomials of degree ≤ n
- 2×2 matrices
- Continuous functions

---

## 5️⃣ Visual Intuition & Real-World Applications

![Real-world applications Vector Space](A_2D_digital_infographic_titled_Real-world_exampl.png)

---

# ✅ Summary Table: The 8 Vector Space Axioms

| # | Axiom Name                          | Operation             | Description                                                                                             |
|---|-------------------------------------|-----------------------|---------------------------------------------------------------------------------------------------------|
| 1 | Additive Closure                    | Vector Addition       | The sum of any two vectors in V is also in V                                                            |
| 2 | Additive Commutativity              | Vector Addition       | $  \vec{u} + \vec{v} = \vec{v} + \vec{u}  $                                                             | 
| 3 | Additive Associativity              | Vector Addition       | $  \vec{u} + (\vec{v} + \vec{w}) = (\vec{u} + \vec{v}) + \vec{w}  $                                     |
| 4 | Additive Identity                   | Vector Addition       | There exists a zero vector $ \vec{0} \in V $ such that $ \vec{v} + \vec{0} = \vec{v} $                  |
| 5 | Additive Inverse                    | Vector Addition       | For every $ \vec{v} \in V $, there is a $ -\vec{v} \in V $ such that $ \vec{v} + (-\vec{v}) = \vec{0} $ |
| 6 | Scalar Multiplicative Closure       | Scalar Multiplication | $ a \cdot \vec{v} \in V $ for any scalar $ a \in \mathbb{R} )$, $( \vec{v} \in V $                      |
| 7 | Distributivity over Vector Addition | Mixed                 | $ a(\vec{u} + \vec{v}) = a\vec{u} + a\vec{v} $                                                          |
| 8 | Distributivity over Scalar Addition | Mixed                 | $ (a + b)\vec{v} = a\vec{v} + b\vec{v} $                                                                |

---

# ✅ Summary: Vector Subspaces

## 🔹 What is a Subspace?

A **subspace** is a subset $ W \subseteq V $ of a vector space $ V $ that is **itself a vector space** under the same operations of addition and scalar multiplication.

---

## ✅ Subspace Test (3 Conditions)

To be a subspace, a set must:

1. **Contain the zero vector**:  
   $ \vec{0} \in W $

2. **Be closed under vector addition**:  
   $ \vec{u}, \vec{v} \in W \Rightarrow \vec{u} + \vec{v} \in W $

3. **Be closed under scalar multiplication**:  
   $ a \in \mathbb{R},\ \vec{v} \in W \Rightarrow a\vec{v} \in W $

---

## 🧪 Examples of Subspaces

| Subspace                                 | Parent Vector Space $ V $   | Notes                                      |
|------------------------------------------|-----------------------------|--------------------------------------------|
| Line through origin in $ \mathbb{R}^2 $  | $ \mathbb{R}^2 $            | Span of a single vector                    |
| Plane through origin in $ \mathbb{R}^3 $ | $ \mathbb{R}^3 $            | Span of two independent vectors            |
| Null space of a matrix $ A $             | $ \mathbb{R}^n $            | Set of solutions to $ A\vec{x} = \vec{0} $ |
| Set of symmetric 2×2 matrices            | $ \mathbb{R}^{2 \times 2} $ | Closed under matrix addition/scaling       |

---

## ❌ Not Subspaces — and Why

| Set Definition                                       | Why Not a Subspace                                    |
|------------------------------------------------------|-------------------------------------------------------|
| $ W = \{ [x, y] \in \mathbb{R}^2 \mid x > 0 \} $     | Doesn’t include zero vector; not closed under scaling |
| $ W = \{ [x, y] \in \mathbb{R}^2 \mid x + y = 1 \} $ | Violates scalar multiplication and lacks zero vector  |

---

## 🧠 Key Insight

> Every **span** of vectors is a subspace — and every subspace can be described as the **span of a set of vectors**.

Subspaces help us define solution spaces, transformations, and constraints in high-dimensional systems.

---

# ✅ Summary: Basis and Dimension

## 🔹 What is a Basis?

A **basis** of a vector space $ V $ is a set of vectors that:

1. **Span** the space — every vector in $ V $ can be written as a linear combination of them.
2. Are **linearly independent** — no vector in the set can be written as a linear combination of the others.

---

## 🔹 What is Dimension?

> The **dimension** of a vector space is the number of vectors in any basis for that space.

- It tells you the **degrees of freedom** or the **minimal number of directions** needed to describe the space.

---

## 🧠 Examples

| Vector Space         | Basis Example                                       | Dimension |
|----------------------|-----------------------------------------------------|-----------|
| $ \mathbb{R}^2 $     | $ \{ [1, 0], [0, 1] \} $                            | 2         |
| $ \mathbb{R}^3 $     | $ \{ [1, 0, 0], [0, 1, 0], [0, 0, 1] \} $           | 3         |
| Line through origin  | $ \{ [1, 2] \} $ (or any nonzero scalar multiple)   | 1         |
| Plane through origin | $ \{ [1, 0, 0], [0, 1, 0] \} \subset \mathbb{R}^3 $ | 2         |

---

## 🔁 Key Facts

- **All bases** for a given space have the **same number of vectors**
- **Span + independence** = basis
- **Dimension** is a property of the space, not the specific basis you choose

---

## ❌ Not a Basis If...

- The vectors are **linearly dependent**
- The vectors **don’t span** the whole space

---

## ✅ Practical Use

- Knowing the basis simplifies:
  - Representing vectors
  - Solving linear systems
  - Understanding the shape and constraints of data spaces

---

## 🧪 Suggested Practice

- Plot vectors using `matplotlib` in 2D and 3D
- Explore vector addition geometrically
- Write Python functions for:
    - Linear combination
    - Vector normalization
    - Span checker (linear dependence check)

---

## 📁 Resources

- `vector_visuals.py` – Python script for plotting
- `vector_visuals.png` – Sample plot images
- [Khan Academy - Vectors](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces)
- [3Blue1Brown: Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6)

---