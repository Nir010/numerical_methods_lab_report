def g(x):
    return (x**2 + 6) / 5

x = 2.5


print("Iter |    x")
print("------------")

for i in range(10):
    print(f"{i:4d} | {x:6.4f}")
    x = g(x)

print("\nThe approximate root is", f"{x:.4f}")

#PROBLEM: Find a root of x^2-5x+6=0 by fixed point iteration method.