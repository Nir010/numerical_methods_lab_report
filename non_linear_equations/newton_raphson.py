def newton_raphson(f, df, x, tol=0.001, n=100):
    print("Iter |   x(n)   |   f(x)   |  f'(x)  |  x(n+1) |  Error")
    print("-------------------------------------------------------")
    
    for i in range(n):
        fx, dfx = f(x), df(x)
        x_new = x - fx/dfx
        error = abs(x_new - x)
        
        print(f"{i+1:4d} | {x:8.4f} | {fx:8.4f} | {dfx:8.4f} | {x_new:8.4f} | {error:7.4f}")
        
        if error < tol:
            return x_new
        x = x_new
    
    return x

f  = lambda x: x**3 - 2*x - 5
df = lambda x: 3*x**2 - 2

root = newton_raphson(f, df, 2.0)
print(f"\nApproximate root = {root:.3f}")

#PROBLEM: Find the root of the equation x^3 - 2x - 5 = 0 using the Newton-Raphson method, correct upto 3 decimal places.