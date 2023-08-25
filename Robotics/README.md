# About

This directory contains the challenges I solved for robotics, and a description on how they work and the maths behind it.

## Rocket

Problem: 
```
I have a rocket ship with a velocity-meter that samples data every 
0.2s and collects instantaneous velocity measurements in a set v. 
Compute the approximate distance traveled by the rocket using discrete 
integration and approximate instantaneous acceleration using 
the central differences algorithm or similar with python
```

This code performs two calculations using the set of instantaneous velocity measurements, `v`, taken at intervals `dt`:
1. **dist calc**: The approx distance `d` traveled by the rocket is calculated using discrete integration.
<br>
Formula:

$$ d = \sum_{i=0}^{n-1} v_i \times dt $$

2. **acceleration calcs**: The instantaneous acceleration `a` (derivative) is approximated. it cant be found normally cus its a discrete set of terms, and not a continues function. I used the central differences formula which can approx the derivative of a broken (discrete) line:

$$  a_i = \frac{v_{i+1} - v_{i-1}}{2 \times dt} $$

For edge cases:

$$ a_0 = \frac{v_1 - v_0}{dt} $$
$$ a_{n-1} = \frac{v_{n-1} - v_{n-2}}{dt} $$

A sample dataset `v` with values from `1` to `20` and `dt=0.2` is used to compute and display the results.

## Fib iteratively

The iterative method involves using a loop to compute the Fibonacci series, unlike the recursive method which repeatedly calls itself (sids idea).

1. **init** two variables, `a` and `b`, to represent the first two fib nums (`0`, `1`).
2. **loop** from `2` to `n`:
   - calc the next fib num as the sum of `a` and `b`.
   - mov the value of `b` to `a`, and the sum to `b`.
3. **return** the value of `b` after the loop ends, which is the `n-th` fib num.

## Mul 20 nat nums
Ummm so i litteraly just realized that this was a factorial, but my code uses a for loop.
1. **init** the `ans` variable
2. **loop** through all natural numbers up until `20`
3. **multiply ans** by itself

## Sumation
Expand this summation:

$$ \sum_{n=1}^{100}n $$ 

I used the basic summation formula. 

$$ \ \sum_{n=1}^{N} n = \frac{N(N + 1)}{2} \ $$
