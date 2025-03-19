# Assignment 1
## 1)
#### 1.a
If there are no rules at all, then all 10 members can sit in any order. The number of ways to arrange 10 distinct individuals is simply:
$$ 10!=3,628,800 $$
##### 1.b 
Now, consider Mycroft and his aide. They must sit together because they do not trust each other. We can treat them as a single unit, reducing the number of elements to arrange from 10 to 9: 9!=?
However, within this unit, Mycroft and his aide can switch places, which doubles the number of ways they can be arranged 
$$ 2*9! $$
#### 1.c 
Here, we have 5 inspectors and 5 constables, and they must alternate in the seating arrangement. That means if we choose a starting group (either an inspector or a constable), the rest must follow an alternating pattern.
Arrange the 5 inspectors in their 5 spots=5!
Arrange the 5 constables in their 5 spots=5!
Choose whether the first seat is taken by an inspector or a constable (2 choices): $ 2*5!*5! $

#### 1.d
Finally, let’s consider the case where each informant is paired with a handler, and they must always sit together. We treat each pair as a single unit, meaning we now have 5 units instead of 10. 
Arrange the 5 units: 5!
Within each pair, the two individuals can swap places: $$ (2!)^5 $$
So, $ 5!*(2!)^5 $

## 2)
Irene Adler hides messages using k distinct numbers chosen from the set of numbers 1 to n. The numbers must be in increasing order. When we choose the numbers, it doesn’t matter in what order we pick them. Once picked, they will be sorted in increasing order automatically. The number of ways to make sorted arrays of k distinct numbers from n numbers is:

$\binom{n}{k} = \frac{n!}{k!(n-k)!}$

## 3)
A mechanical hound moves on an $n \times m$ grid from $(1,1)$ to $(n,m)$, only moving **right** or **down**.

#### 3.a
The total number of possible paths is given by the binomial coefficient: we have
$ {n+m-2} $ path, because we have $ m-1 $ moves to the right (R) and $ n-1 $ moves to down (D), so every path is a sequence of 
$ m-1+n-1 = n+m-2 $ moves. We have also $ n-1 $ ways to order D.

$$
\binom{n+m-2}{n-1} = \frac{(n+m-2)!}{(n-1)!(m-1)!}
$$

#### 3.b
If the hound **must move right first**, it will be at $(1,2)$. From there, it has **$(n-1)$ down moves** and **$(m-2)$ right moves** left:

$$
\binom{n+m-3}{n-1} = \frac{(n+m-3)!}{(n-1)!(m-2)!}
$$

#### 3.c
Exactly 3 Direction Changes
The hound **switches direction (right → down or down → right) exactly three times**. This means dividing its moves into two blocks of right moves and two blocks of down moves:

$$
\binom{m-1}{2} \binom{n-1}{2}
$$

## 4)

The total number of ways to choose 5 cards from a 52-card deck is given by the combination formula:
$$\binom{52}{5} = \frac{52!}{5!(52-5)!} = 2,598,960$$

#### 4.a

A flush consists of 5 cards of the same suit. This includes both regular flushes and straight flushes.


-There are 4 suits in a deck, so we have to chose the suit. For each suit, the number of ways to choose 5 cards is:
   $$\binom{13}{5}$$
   Calculating this gives:
   $$\binom{13}{5} = \frac{13 \times 12 \times 11 \times 10 \times 9}{5 \times 4 \times 3 \times 2 \times 1} = 1,287$$
 The total number of flushes (including straight flushes) is:
   $$4 \times \binom{13}{5} = 4 \times 1,287 = 5,148$$

A straight flush is a special case of a flush where the 5 cards are in consecutive rank. There are 10 possible straight flushes for each suit (A-5, 2-6, ..., 10-A), so:
   $$4 \times 10 = 40 \text{ straight flushes}$$

The total number of flushes (including straight flushes) is:
$$5,148 + 40 = 5,188$$

Probability of a Flush:
$$P(\text{Flush}) = \frac{5,188}{2,598,960} \approx 0.00199 \text{ or } 0.199\%$$

#### 4.b. 
Choose 2 ranks from the 13 available ranks:
   $$\binom{13}{2} = 78$$
 
For each of the two ranks, choose 2 suits out of 4:
   $$\binom{4}{2} \times \binom{4}{2} = 6 \times 6 = 36$$

Choose a rank for the fifth card (which cannot be one of the ranks already chosen):
   $$\binom{11}{1} = 11$$
   Then choose a suit for this card:
   $$\binom{4}{1} = 4$$

The total number of two pair hands is:
   $$78 \times 36 \times 11 \times 4 = 123,552$$

Probability of Two Pairs:
$$P(\text{Two Pairs}) = \frac{123,552}{2,598,960} \approx 0.0475$$

#### 4.c

A hand with four of a kind consists of four cards of one rank and one card of a different rank.

Choose 1 rank from the 13 available ranks:
   $$\binom{13}{1} = 13$$

Choose a rank for the fifth card (which cannot be the same as the four of a kind):
   $$\binom{12}{1} = 12$$
   Then choose a suit for this card:
   $$\binom{4}{1} = 4$$
The total number of four of a kind hands is:
   $$13 \times 12 \times 4 = 624$$

Probability of Four of a Kind:
$$P(\text{Four of a Kind}) = \frac{624}{2,598,960} \approx 0.00024$$

## 5)

To find the probability that the first  r bits of a telegraph, which sends M  0's and  N 1's in random order, contain exactly k 1's, we can use combinatorial methods.

We need to choose k positions for the 1's from the first  r bits. The number of ways to choose k  positions from r  is given by:
   $\binom{r}{k}$

After placing  k 1's in the first  r bits, we need to fill the remaining r - k positions with 0's. The number of 0's available is  M, so we need to ensure $r - k \leq M$

We still have N - k  1's left to place in the remaining  (M + N - r)  positions. The number of ways to choose N - k  positions from  M + N - r is:
   $$\binom{M + N - r}{N - k}$$

The total ways to arrange  M  0's and  N 1's is:
$$\binom{M + N}{r}$$


The probability that the first  r bits contain exactly k 1's is given by the ratio of the successful arrangements to the total arrangements:

$$P(\text{exactly } k \text{ 1's in first } r \text{ bits}) = \frac{\binom{r}{k} \cdot \binom{M + N - r}{N - k}}{\binom{M + N}{r}}$$


## 6)

#### 6.a
To find the total number of exhibits, we need to calculate the combinations of selecting 3 birds from 8 and 3 reptiles from 6.

-Choosing Birds: The number of ways to choose 3 birds from 8 is given by the combination formula:
   $$\binom{n}{r} = \frac{n!}{r!(n-r)!}$$
   For birds:
   $$\binom{8}{3} = \frac{8!}{3!(8-3)!} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56$$

-Choosing Reptiles: The number of ways to choose 3 reptiles from 6 is:
   $$\binom{6}{3} = \frac{6!}{3!(6-3)!} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = 20$$

The total number of exhibits is the product of the two combinations:
   $$\text{Total Exhibits} = \binom{8}{3} \times \binom{6}{3} = 56 \times 20 = 1120$$

#### 6.b 

In this case, we need to exclude the combinations where both the hawk and the raven are selected.

Cases with Both Hawk and Raven: If both the hawk and the raven are included, we need to choose 1 additional bird from the remaining 6 birds:
   $$\binom{6}{1} = 6$$
   The number of ways to choose 3 reptiles remains:
   $$\binom{6}{3} = 20$$
 
The total exhibits including both the hawk and the raven is:
   $$\text{Exhibits with Hawk and Raven} = 6 \times 20 = 120$$

The total valid exhibits avoiding this chaos is:
   $$\text{Total Valid Exhibits} = \text{Total Exhibits} - \text{Exhibits with Hawk and Raven} = 1120 - 120 = 1000$$

#### 6.c

We need to exclude the combinations where both the venomous parrot and the cobra are selected.


Cases with Both Parrot and Cobra: If both the parrot and the cobra are included, we need to choose 1 additional bird from the remaining 7 birds and 2 additional reptiles from the remaining 5 reptiles:

- Choosing 1 more bird:
   $$\binom{7}{1} = 7$$
   - Choosing 2 more reptiles: $$\binom{5}{2} = 10$$

The total exhibits including both the parrot and the cobra is:
  $$\text{Exhibits with Parrot and Cobra} = 7 \times 10 = 70$$

The total valid exhibits avoiding this trap is:
   $$\text{Total Valid Exhibits} = \text{Total Exhibits} - \text{Exhibits with Parrot and Cobra} = 1120 - 70 = 1050$$


## 7)

#### 7.a

We need to distribute £20 million across 4 enterprises, with minimum investments of £1M, £2M, £3M, and £4M respectively.

Calculate the minimum total required investment.
£1M + £2M + £3M + £4M = £10M
 
After satisfying the minimum requirements, Holmes has £20M - £10M = £10M left to distribute.

his is a problem of distributing 10 additional units of £1M across 4 enterprises.
This is equivalent to placing 10 identical objects into 4 distinct groups, which can be solved using the formula for combinations with repetition allowed:
$$\binom{n+r-1}{r} = \binom{10+4-1}{10} = \binom{13}{10} = \binom{13}{3} = \frac{13!}{10! \cdot 3!} = \frac{13 \cdot 12 \cdot 11}{3 \cdot 2 \cdot 1} = 286$$

Therefore, Holmes has 286 different strategies to fund all 4 enterprises.

#### 7.b
- For funding exactly 3 enterprises, we first choose which 3 out of 4 to fund.
$$\binom{4}{3} = 4$$ ways

- For each combination of 3 enterprises, we need to calculate the investment strategies.

**Case 1: Exclude Enterprise 1 (minimum £1M)**
- Minimum investment for enterprises 2, 3, 4 is £2M + £3M + £4M = £9M
- Holmes has £20M - £9M = £11M left to distribute
- Number of ways = $$\binom{11+3-1}{11} = \binom{13}{11} = \binom{13}{2} = 78$$

**Case 2: Exclude Enterprise 2 (minimum £2M)**
- Minimum investment for enterprises 1, 3, 4 is £1M + £3M + £4M = £8M
- Holmes has £20M - £8M = £12M left to distribute
- Number of ways = $$\binom{12+3-1}{12} = \binom{14}{12} = \binom{14}{2} = 91$$

**Case 3: Exclude Enterprise 3 (minimum £3M)**
- Minimum investment for enterprises 1, 2, 4 is £1M + £2M + £4M = £7M
- Holmes has £20M - £7M = £13M left to distribute
- Number of ways = $$\binom{13+3-1}{13} = \binom{15}{13} = \binom{15}{2} = 105$$

**Case 4: Exclude Enterprise 4 (minimum £4M)**
- Minimum investment for enterprises 1, 2, 3 is £1M + £2M + £3M = £6M
- Holmes has £20M - £6M = £14M left to distribute
- Number of ways = $$\binom{14+3-1}{14} = \binom{16}{14} = \binom{16}{2} = 120$$

Total number of ways to fund exactly 3 enterprises = 78 + 91 + 105 + 120 = 394
Total number of ways to fund at least 3 enterprises = 286 + 394 = 680



## 8)
#### 8.a
We want to know how many agents are taking none of the courses. This requires finding the number of agents who are in the complement of the union of all three courses.

$$|J \cup C \cup P| = |J| + |C| + |P| - |J \cap C| - |J \cap P| - |C \cap P| + |J \cap C \cap P|$$

Substituting the numbers:

$$|J \cup C \cup P| = 27 + 28 + 20 - 12 - 5 - 8 + 2 = 52$$

So, 52 agents are taking at least one of the courses. The number of agents taking **none** of the courses is:

$$100 - 52 = 48$$

The probability that a randomly chosen agent is not taking any course is:
$$P(\text{no course}) = \frac{48}{100} = 0.48$$

#### 8.b
To find the probability that a randomly selected agent is studying exactly one course, we need to compute the number of agents who are in exactly one of the courses, and then divide by the total number of agents.

- Only Java: These are the agents in Java, but not in C++ or Python. This can be calculated as:
  $$|J \setminus (C \cup P)| = |J| - (|J \cap C| + |J \cap P| - |J \cap C \cap P|)
  $$
  Substituting the values:
  $$|J \setminus (C \cup P)| = 27 - (12 + 5 - 2) = 27 - 15 = 12$$

- Only C++: These are the agents in C++, but not in Java or Python:
  $$|C \setminus (J \cup P)| = |C| - (|J \cap C| + |C \cap P| - |J \cap C \cap P|)$$
  Substituting the values:
  $$|C \setminus (J \cup P)| = 28 - (12 + 8 - 2) = 28 - 18 = 10$$

- Only Python: These are the agents in Python, but not in Java or C++:
  $$|P \setminus (J \cup C)| = |P| - (|J \cap P| + |C \cap P| - |J \cap C \cap P|)$$
  Substituting the values:
  $$|P \setminus (J \cup C)| = 20 - (5 + 8 - 2) = 20 - 11 = 9$$
  

Now, we add the number of agents studying exactly one course:

$$12 (\text{Only Java}) + 10 (\text{Only C++}) + 9 (\text{Only Python}) = 31$$

The probability that an agent is studying exactly one course is:

$$P(\text{exactly one course}) = \frac{31}{100} = 0.31$$ 

#### 8.c

We want the probability that at least one of the two randomly chosen agents is studying at least one course.
The complementary event to this is that both agents are studying no course, so we can first calculate the probability that both agents are studying no course, and then subtract that from 1.

- The probability that one agent is studying no course is $$P(\text{no course}) = 0.48$$
- The probability that both agents are studying no course is:
  $$P(\text{both no course}) = 0.48 \times 0.48 = 0.2304$$
  
Therefore, the probability that at least one of the two agents is studying at least one course is:

$$P(\text{at least one has a course}) = 1 - 0.2304 = 0.7696$$


## 9)

#### 9.a
When the spy tries passwords randomly and discards those that don't work, the probability of success on the k-th attempt is not constant. This is because, after each failure, the number of remaining passwords decreases, and the probability of success adjusts accordingly.
If there are n passwords and  k-1 failed attempts, the probability of success on the k-th attempt is:  
$$P(k) = \frac{1}{n - (k-1)}$$
Where $n - (k-1)$ is the number of remaining passwords.


#### 9.b

For the k-th attempt to be successful, the first k-1 attempts must all be failures. However, in this scenario, the spy does not discard any passwords, meaning he can select the same incorrect passwords multiple times.


   - The probability of failing on any single attempt remains $$\frac{n-1}{n}$$
   - Therefore, the probability of failing \( k-1 \) times before succeeding on the k-th attempt is:
   $$\left(\frac{n-1}{n}\right)^{k-1}$$

- The probability that the k-th attempt is successful (after \( k-1 \) failures) is still:
   $$\frac{1}{n}$$

The total probability that the k-th attempt wins is:
   $$P(\text{k-th attempt wins}) = \left(\frac{n-1}{n}\right)^{k-1} \cdot \frac{1}{n}$$




## 10)
#### 10.a
We want to find the probability that two distinct numbers appear exactly three times each when rolling a die six times.

Choose the number that will appear thrice: 
$$\binom{6}{2} = 15 \text{ ways}$$
We need to choose 3 different numbers from the remaining 5 numbers (since one number is already chosen). This can be done in: $\frac{6!}{3!3!} = 20$

Total outcomes: $ 6^6 = 46656$

The probability of getting two numbers appearing thrice each is:
   $$\frac{15 \times 20}{46656} = \frac{300}{46656} \approx 0.00642$$

#### 10.b

-Choose which number appears three times:
$$\binom{6}{1} = 6 \text{ ways}$$

-Choose positions for the selected number:
we select which 3 positions out of 6 will contain our selected number:
$$\binom{6}{3} = 20 \text{ ways}$$

-Fill the remaining 3 positions:
for the remaining 3 positions, we need to ensure no other number appears three times. This means we can only use the other 5 numbers in configurations where none appears more than twice.
Two different numbers (one appears twice, one appears once)
- Choose which number appears twice: $\binom{5}{1} = 5$ ways
- Choose which number appears once from the remaining 4 numbers: $\binom{4}{1} = 4$ ways
- Choose which 2 positions (out of 3) will have the number that appears twice: $\binom{3}{2} = 3$ ways
- Total for Case 2: $5 \times 4 \times 3 = 60$ ways

Total favorable outcomes: $6 \times 20 \times (60 + 60) = 6 \times 20 \times 120 = 14,400$

Total possible outcomes: $6^6 = 46,656$

Final Probability:
$$P = \frac{14,400}{46,656} = \frac{25}{81} \approx 0.309 \text{ or about } 30.9\%$$

## 11)
The total number of ways to distribute 20 distinct letters to 12 informants is given by $12^{20}$

Calculate the Specific Distribution:
   - Choose Informants:
     - Choose 4 informants to receive 2 letters each: $\binom{12}{4}$.
     - Choose 3 informants to receive 4 letters each from the remaining 8: $\binom{8}{3}$.

   - Distributing Letters:
     - For the 4 informants receiving 2 letters each:
       $$\frac{20!}{(2!)^4 \cdot (4!)^3 }$$


   The final probability is given by the ratio of favorable outcomes to total outcomes:
   $$P = \frac{\text{Favorable Outcomes}}{\text{Total Outcomes}} = \frac{\binom{12}{4} \cdot \binom{8}{3} \cdot \frac{20!}{(2!)^4 \cdot (4!)^3}}{12^{20}}$$


## 12)
The probability of a single clue landing in the first bucket is $$p = \frac{1}{n}$$ 
Otherwise, the probability of a single clue landing in others buckets is $1-p$.  Since the clues are assigned independently, the total number of clues that end up in the first bucket follows a binomial distribution:
$$X \sim \text{Binom}(m, p)$$

Chance exactly k land in the first bucket:
$$P(X = k) = \binom{m}{k} p^k (1 - p)^{m-k}$$

Replacing $p = \frac{1}{N}$, we get:

$$P(X = k) = \binom{m}{k} \left( \frac{1}{N} \right)^k \left( \frac{N-1}{N} \right)^{m-k}$$

## 14) 
Run `Game14.py` with python3: 
```bash
python Game14.py