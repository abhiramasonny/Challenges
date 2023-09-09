import numpy as np

def foo(x):
    return x**5

def numerical_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)

def main():
    x_value = 2.0
    derivative = numerical_derivative(foo, x_value)
    
    print("Original function at point:", foo(x_value))
    print("Numerical derivative point:", derivative)

if __name__ == "__main__":
    main()
