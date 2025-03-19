# Assignment 1
## 1)
1.a If there are no rules at all, then all 10 members can sit in any order. The number of ways to arrange 10 distinct individuals is simply:
$$ 10!=3,628,800 $$
1.b Now, consider Mycroft and his aide. They must sit together because they do not trust each other. We can treat them as a single unit, reducing the number of elements to arrange from 10 to 9: 9!=?
However, within this unit, Mycroft and his aide can switch places, which doubles the number of ways they can be arranged 
$$ 2*9! $$
1.c Here, we have 5 inspectors and 5 constables, and they must alternate in the seating arrangement. That means if we choose a starting group (either an inspector or a constable), the rest must follow an alternating pattern.
Arrange the 5 inspectors in their 5 spots=5!
Arrange the 5 constables in their 5 spots=5!
Choose whether the first seat is taken by an inspector or a constable (2 choices): $ 2*5!*5! $

1.d Finally, let’s consider the case where each informant is paired with a handler, and they must always sit together. We treat each pair as a single unit, meaning we now have 5 units instead of 10. 
Arrange the 5 units: 5!
Within each pair, the two individuals can swap places: $$ (2!)^5 $$
So, $ 5!*(2!)^5 $

## 2)
Irene Adler hides messages using k distinct numbers chosen from the set of numbers 1 to n. The numbers must be in increasing order. When we choose the numbers, it doesn’t matter in what order we pick them. Once picked, they will be sorted in increasing order automatically. The number of ways to make sorted arrays of k distinct numbers from n numbers is:

$\binom{n}{k} = \frac{n!}{k!(n-k)!}$

## 3)
A mechanical hound moves on an $n \times m$ grid from $(1,1)$ to $(n,m)$, only moving **right** or **down**.

3.a The total number of possible paths is given by the binomial coefficient: we have
$ {n+m-2} $ path, because we have $ m-1 $ moves to the right (R) and $ n-1 $ moves to down (D), so every path is a sequence of 
$ m-1+n-1 = n+m-2 $ moves. We have also $ n-1 $ ways to order D.

$$
\binom{n+m-2}{n-1} = \frac{(n+m-2)!}{(n-1)!(m-1)!}
$$

3.b If the hound **must move right first**, it will be at $(1,2)$. From there, it has **$(n-1)$ down moves** and **$(m-2)$ right moves** left:

$$
\binom{n+m-3}{n-1} = \frac{(n+m-3)!}{(n-1)!(m-2)!}
$$

3.c Exactly 3 Direction Changes
The hound **switches direction (right → down or down → right) exactly three times**. This means dividing its moves into two blocks of right moves and two blocks of down moves:

$$
\binom{m-1}{2} \binom{n-1}{2}
$$

## 10)



## 11)
The total number of ways to distribute 20 distinct letters to 12 informants is given by $12^{20}$

Calculate the Specific Distribution:
   - Choose Informants:
     - Choose 4 informants to receive 2 letters each: $\binom{12}{4}$.
     - Choose 3 informants to receive 4 letters each from the remaining 8: $\binom{8}{3}$.

   - Distributing Letters:
     - For the 4 informants receiving 2 letters each:
       $$
       \frac{20!}{(2!)^4 \cdot (4!)^3 }
       $$


   The final probability is given by the ratio of favorable outcomes to total outcomes:
   $$
   P = \frac{\text{Favorable Outcomes}}{\text{Total Outcomes}} = \frac{\binom{12}{4} \cdot \binom{8}{3} \cdot \frac{20!}{(2!)^4 \cdot (4!)^3}}{12^{20}}
   $$


## 12)
The probability of a single clue landing in the first bucket is $$ p = \frac{1}{n}$$ 
Otherwise, the probability of a single clue landing in others buckets is $ 1-p $.
Since the clues are assigned independently, the total number of clues that end up in the first bucket follows a binomial distribution:
$$
X \sim \text{Binom}(m, p)
$$

Chance exactly k land in the first bucket:
$$
P(X = k) = \binom{m}{k} p^k (1 - p)^{m-k}
$$

Replacing $ p = \frac{1}{N} $, we get:

$$
P(X = k) = \binom{m}{k} \left( \frac{1}{N} \right)^k \left( \frac{N-1}{N} \right)^{m-k}
$$
