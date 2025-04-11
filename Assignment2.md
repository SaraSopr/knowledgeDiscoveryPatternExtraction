# Assignment 2

## 1)

#### 1.a  
The prior belief is a normal distribution:  
$$D \sim \mathcal{N}(98, 16)$$  
So the PDF is:  
$$f_D(d) = \frac{1}{\sqrt{2\pi \cdot 16}} \exp\left(-\frac{(d - 98)^2}{2 \cdot 16}\right)$$

#### 1.b  
The reading is the true distance plus Gaussian noise, so:  
$$\text{Reading} \sim \mathcal{N}(t, 4)$$  
Then:  
$$P(\text{Reading}=100 \mid \text{True distance}=t) = \frac{1}{\sqrt{2\pi \cdot 4}} \exp\left(-\frac{(100 - t)^2}{2 \cdot 4}\right)$$

#### 1.c  
Posterior is proportional to prior × likelihood:  
$$\text{Posterior}(d) \propto \exp\left(-\frac{(d - 98)^2}{32}\right) \cdot \exp\left(-\frac{(d - 100)^2}{8}\right)$$

---

## 2)

Poisson distribution is used here:  
$$X \sim \text{Poisson}(\lambda)$$

#### 2.a  
In 1 minute: $\lambda = 5.5$  
Want:  
$$P(X > 7) = 1 - P(X \leq 7)$$

#### 2.b  
In 2 minutes: $\lambda = 11$  
Want:  
$$P(X > 13) = 1 - P(X \leq 13)$$

#### 2.c  
In 3 minutes: $\lambda = 16.5$  
Want:  
$$P(X > 15) = 1 - P(X \leq 15)$$

---

## 3)

#### 3.a  
If $X \sim \text{Uniform}(a, b)$, the CDF is:  
$$F(x) = \frac{x - a}{b - a}$$  
Set $F(m) = 0.5$:  
$$m = \frac{a + b}{2}$$

#### 3.b  
If $X \sim \mathcal{N}(\mu, \sigma^2)$, then:  
$$\text{Median} = \mu$$

---

## 4)

Let $X_i \sim \mathcal{N}(2200, 52900)$

#### 4.a  
Total over 2 weeks:  
- Mean = $2 \cdot 2200 = 4400$  
- Variance = $2 \cdot 52900 = 105800$  
Then:  
$$Z = \frac{5000 - 4400}{\sqrt{105800}}$$  
Use standard normal table.

#### 4.b  
Find $p = P(X > 2000)$, then use binomial:  
Want:  
$$P(\text{at least 2 of 3 weeks exceed 2000}) = 1 - P(0) - P(1)$$  
Where:  
$$P(k) = \binom{3}{k} p^k (1 - p)^{3-k}$$

---

## 5)

#### 5.a  
If $X \sim \mathcal{N}(\mu_1, \sigma_1^2)$, $Y \sim \mathcal{N}(\mu_2, \sigma_2^2)$, and they are independent:  
$$A = X + Y \sim \mathcal{N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$$

#### 5.b  
$B = 5X + 2$  
Then:  
$$B \sim \mathcal{N}(5\mu_1 + 2, 25\sigma_1^2)$$

#### 5.c  
Let $C = aX - bY + c^2Z$, with independent $X, Y, Z$:  
- Mean:  
  $$a\mu_1 - b\mu_2 + c^2\mu_3$$  
- Variance:  
  $$a^2\sigma_1^2 + b^2\sigma_2^2 + c^4\sigma_3^2$$  
So:  
$$C \sim \mathcal{N}(a\mu_1 - b\mu_2 + c^2\mu_3, a^2\sigma_1^2 + b^2\sigma_2^2 + c^4\sigma_3^2)$$

---

## 6)

Given:  
$$f_{X,Y}(x, y) = c \cdot \frac{y}{x}, \quad 0 < y < x < 1$$

#### 6.a  
Normalize the PDF:  
$$\int_0^1 \int_0^x c \cdot \frac{y}{x} \,dy\,dx = 1$$  
Result:  
$$c = 6$$

#### 6.b  
The function is not separable into $f_X(x)f_Y(y)$, so:  
**Not independent**

#### 6.c  
Marginal of X:  
$$f_X(x) = \int_0^x 6 \cdot \frac{y}{x} dy = 3x$$

#### 6.d  
Marginal of Y:  
$$f_Y(y) = \int_y^1 6 \cdot \frac{y}{x} dx = -6y \ln y$$

---

## 7)

Choose $X \in \{1,2,3,4,5,6\}$, then $Y \in \{1,...,X\}$

#### 7.a  
- $P(X = x) = \frac{1}{6}$  
- $P(Y = y \mid X = x) = \frac{1}{x}$  
Then:  
$$P(X = x, Y = y) = \frac{1}{6x}, \text{ for } y \leq x$$

#### 7.b  
Conditional:  
$$P(X = j \mid Y = i) = \frac{P(X = j, Y = i)}{P(Y = i)}$$  
Where:  
$$P(Y = i) = \sum_{j = i}^6 \frac{1}{6j}$$

#### 7.c  
They are **not independent**, because:  
$$P(X = j \mid Y = i) \ne P(X = j)$$
