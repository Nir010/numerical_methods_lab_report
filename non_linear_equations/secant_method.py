import math

def f(x):
    return 3*x + math.sin(x) - math.exp(x)

x0 = 0.0
x1 = 1.0

print("Iter |   x0    |   x1    |   x2    |  f(x2)")
print("---------------------------------------------")

for i in range(1, 6):
    x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
    print(f"{i:4d} | {x0:7.4f} | {x1:7.4f} | {x2:7.4f} | {f(x2):7.4f}")
    x0, x1 = x1, x2

print("\nThe approximate root is", round(x2, 4))


#PROBLEM: Using secant method find a root of the equation 3x+sinx-e^x=0 correct to three decimal places.