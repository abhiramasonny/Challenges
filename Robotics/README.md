# About

This directory contains the challenges I solved for robotics, and a description on how they work and the maths behind it.
<br>
Organized into the directories

 - Python
 - Java

## Rocket

Problem: 
```
I have a rocket ship with a velocity-meter that samples data every 
0.2s and collects instantaneous velocity measurements in a set v. 
Compute the approximate distance traveled by the rocket using discrete 
integration and approximate instantaneous acceleration using 
the central differences algorithm or similar with python
```

This code performs two calculations using the set of instantaneous velocity measurements, `v`, taken at intervals `dt` *the setp*:

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
<br>
Credit to this video and khanacademy for teaching this to me:
<a>https://www.youtube.com/watch?v=Jqa-aFE9-GI</a>


### Expansion of the formula
So apprently i got to expand so...

- **Distance calcs:**
  - the problem is: Given a set of discrete sequence of velocities at time intervals, how can u estimate the total distance traveled by the rocket?
  - solution: when u mul each velocity value with the time interval of `dt` and do a summation of it, u are essentially aprox the areas of several rectangles *integration*, each is representing a small segment of the journey. Summing these areas gives the total distance. The formula for this is: $$ d = \sum_{i=0}^{n-1} v_i \times dt $$ as stated above. This is also known as the reimann sum.
- **Acc calcs:**
  - problem is: how can u estimate how fast the velocity is changing *accleration*? This one was a lot harder for me...
  - my solution: i used the central differences method to approximate this rate of change *derivitive*. For most velocity measurements besides the first and last *edge cases*, the acceleration is calculated by taking the difference between the subsequent and preceding velocities, and then dividing by twice the time interval, essentially calculating the slope or the rate of change over this period. this is what the central diffrences is calculating with the formula $$  a_i = \frac{v_{i+1} - v_{i-1}}{2 \times dt} $$
 but for the first and last velocities, i had to use the forward/backwards methods.

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

## Pi with random digits (derivation)

**exactly what i couldn't do on spot...**
1. Setup: look at the part of a unit circle on the first quadrant with radius *r* inside a square of side *r*. 
   The area of the **quarter** circle is 

$$ \ \frac{\pi r^2}{4} \ $$

2. random part: 
    gen *N* random points inside the square. 
   Let *M* be the number of points that are inside the circle. *only first quadrant*.

3. Ratios:
   The ratio of the area of the circle to area of square is

$$ \ \frac{\frac{\pi r^2}{4}}{r^2} = \frac{\pi}{4} \ $$

4. guess pi:
The ratio of the number of points inside the circle to the 
total num of points is:

$$ \ \frac{M}{N} \ $$

So u can write  

$$ \ \frac{M}{N} \approx \frac{\pi}{4} \ $$

5. guess n:
u can derive the value of pi:

$$ \ \pi \approx 4 \times \frac{M}{N} \ $$

## Prime

1. **init**:
   just basic init func, getting the answer and the variable

2. **check**:
   - if `n` is less than 2, it's not a prime.
   - If it's even and not 2, it's not a prime.
   - if `n` is divisible by 3 and not 3 itself, it's not a prime`.
   - then some big boi formula found online.

## Hello world

The most complex program of them all.