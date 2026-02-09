def bisection(f, a, b, tol=0.005, n=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
    
    print("Iteration |    a     |    b     |   mid    |  f(mid)  |  Error  ")
    print("-------------------------------------------------------------")
    
    for i in range(n):
        mid = (a + b) / 2
        fmid = f(mid)
        error = abs(b - a) / 2
        
        print(f"{i+1:9d} | {a:8.5f} | {b:8.5f} | {mid:8.5f} | {fmid:8.5f} | {error:7.5f}")
        
        if abs(b - a) < tol:
            return mid
        
        if f(a) * fmid < 0:
            b = mid
        else:
            a = mid

    print("\nMaximum iterations reached.")
    return mid

def f(x):
    return x**3 - 4*x - 9

root = bisection(f, 2, 3)
print(f"\nApproximate root = {root:.5f}")

#PROBLEM: Find the root of the equation x^3-4x-9=0 using the Bisection method, correct upto 5 decimal places.