# About

This directory contains the challenges I solved for robotics.

## Rocket.py

Problem: 
```
I have a rocket ship with a velocity-meter that samples data every 
0.2s and collects instantaneous velocity measurements in a set v. 
Compute the approximate distance traveled by the rocket using discrete 
integration and approximate instantaneous acceleration using 
the central differences algorithm or similar with python
```

This code performs two calculations using the set of instantaneous velocity measurements, `v`, taken at intervals `dt`:
1. **dist calc**: The approx distance `d` traveled by the rocket is calculated using discrete integration:
formula:

$$ d = \sum_{i=0}^{n-1} v_i \times dt $$

1. **acceleration calcs**: The instantaneous acceleration `a` (derivative) is approximated. it cant be found normally cus its a discrete set of terms, and not a continues function. I used the central differences formula which can approx the derivative of a broken (discrete) line:

$$  a_i = \frac{v_{i+1} - v_{i-1}}{2 \times dt} $$
For edge cases:

$$ a_0 = \frac{v_1 - v_0}{dt} $$
$$ a_{n-1} = \frac{v_{n-1} - v_{n-2}}{dt} $$

A sample dataset `v` with values from `1` to `20` and `dt=0.2` is used to compute and display the results.
