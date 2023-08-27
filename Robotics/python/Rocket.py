"""
I have a rocket ship with a velocity-meter that samples data every 
0.2s and collects instantaneous velocity measurements in a set v. 
Compute the approximate distance traveled by the rocket using discrete 
integration and approximate instantaneous acceleration using 
the central differences algorithm or similar with python
"""

def compute_distance(v, dt):
    return sum(v) * dt
def compute_acceleration(v, dt):
    n = len(v)
    a = [0] * n
    for i in range(1, n-1):
        a[i] = (v[i+1] - v[i-1]) / (2*dt)
        a[0] = (v[1] - v[0]) / dt
        a[n-1] = (v[n-1] - v[n-2]) / dt
    return a #fixed the indentation issue finally lmao
v = [_ for _ in range(1,21)]
dt = 0.2
distance = compute_distance(v, dt)
acceleration = compute_acceleration(v, dt)
print("aprox distance:", distance)
print("aprox acceleration:", acceleration)
