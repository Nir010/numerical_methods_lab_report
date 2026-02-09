def regula_falsi(f, a, b, n=6):
    print("Iter |    a     |    b     |    x     |   f(x)")
    print("------------------------------------------------")
    for i in range(1, n + 1):
        fa, fb = f(a), f(b)

        x = a - (fa * (b - a)) / (fb - fa)
        fx = f(x)

        print(f"{i:4d} | {a:8.4f} | {b:8.4f} | {x:8.4f} | {fx:8.4f}")

        if fa * fx < 0:
            b = x
        else:
            a = x

    return x

# Given function
f = lambda x: x**3 - x - 1

# Initial interval
root = regula_falsi(f, 1.0, 2.0, 6)

print(f"\nApproximate root after 6 iterations = {root:.4f}")

#PROBLEM: Use False position[regula-falsi] method to locate the root of f(x) = x^3-x-1=0 between x=1 and x=2 up to 6 iterations.