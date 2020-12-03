---
title: Heute wieder Notizen machen, gar kein Bock.
---

# Basics

## modulo

Teilungsrest:
$$ 3 / 2 = 1R1 $$
&downarrow;
$$ 3 \textrm{mod} 2 = 1 $$

## Kongruenz

Einfachere Schreibweise für

$$ x\ \textrm{mod}\ n = y\ \textrm{mod}\ n $$

$$ x \equiv y\ (\textrm{mod}\ n) $$

## Summe

$$ \sum_{n=k}^{m} f(n) = f(k) + f(k + 1) + ... + f(m) $$

```c
for(int n = k; n <= m; n++)
```

$$ \sum_{n=1}^{3} n = 6 $$

$$ \sum_{n=1}^{\infty} 2^{-n} = 1 $$

# Peano-Axinome
Axinom: grundlegende Aussage, die als gegeben angesehen wird

Peano hat die natürlichen Zahlen so definiert:

1. $$ 0 \in \mathbb{N} $$

$$ \forall n (n \in \mathbb{N}) $$

2. $$ n' \in \mathbb{N} $$
3. $$ n' \ne 0 $$

$$ \forall n, m (n, m \in \mathbb{N}) $$

4. $$ m' = n' \Rightarrow m = n $$

$$ \forall \chi (0 \in \chi) $$ und
$$ (n \in \chi \Rightarrow n' \in \chi) $$

5. $$ \chi \subseteq \mathbb{N} $$

# Ordinalzahlen

„1 ist die **erste** &naturals;“  
&naturals; = {1, 2, …}  
&naturals;[1] = 1  
&naturals; ist schon unendlich  
jede n ist auch eine Ord  
„&omega; > &infin;“ (falsch, aber naja)  
&omega; = &naturals;  
&omega;: kleinste **transfinite** Ordinalzahl  
&DownArrow;  
größer als jede n &Element; &naturals;  

## Ord definieren

$$
ord(n) =
\begin{cases}
\{\}       & \quad \text{wenn } n = 0\\
ord(n - 1) \cup \{ord(n - 1)\}  & \quad \text{wenn } n > 0
\end{cases}
$$


0 = {}  
1 = {0} = {{}}  
2 = {0, 1} = {{}, {{}}}  
…  
n = {0, 1, …, n - 1}

```scm
(define (ord n)
  (if (= n 0) '()
    (append
      (ord (- n 1))
      (list (ord (- n 1)))
)))
```

## Rechnen mit Mengen

&sigma; = 0 = {}  
&tau;: irgendeine Menge  
&sigma; + &tau; = &tau;

&sigma; = 1 = {0}  
&tau; = 2 = {0, 1}  
&sigma; + &tau; = 3 = {0, 1, 2}

### Disjunkt machen
&tau; so *umschreiben* (?), dass für alle Elemente t &isin; &tau;'
gilt: t &notin; &sigma;

### Anhängen
&tau; hinten an &sigma; anhängen.

### Test 1

&sigma; = {0}  
&tau; = {0, 1}  
&tau;' = {1, 2} (?)  
&sigma; + &tau; = {0, 1, 2}  

### Test 2

&sigma; = {0, 1, 2, 3}  
&tau; = {0, 1}  
&sigma; + &tau; = {0, 1, 2, 3, 4, 5}  
&tau;' = {4, 5}

⇒ WTF?!

## Mengen addieren, aber wirklich

ich versteh des immer noch ned und find den englischen wikipedia
eintrag auch nimmer
