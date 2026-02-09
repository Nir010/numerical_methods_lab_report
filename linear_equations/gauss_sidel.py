def gauss_sidel(x0, y0, z0, tol=1e-4, max_iter=25):
    x, y, z = x0, y0, z0
    print("Iter |    x     |    y     |    z")
    print("--------------------------------------")
    for i in range(1, max_iter + 1):
        x_new = (6 - 2 * y + z) / 3
        y_new = (2 * x_new + 2 * z + 3) / 4
        z_new = (8 + 2 * x_new - y_new) / 4

        print(f"{i:4d} | {x_new:8.4f} | {y_new:8.4f} | {z_new:8.4f}")

        # Check for convergence
        if abs(x_new - x) < tol and abs(y_new - y) < tol and abs(z_new - z) < tol:
            break

        x, y, z = x_new, y_new, z_new

    print("\nThe approximate solution is:")
    print(f"x = {x_new:.3f}, y = {y_new:.3f}, z = {z_new:.3f}")


# Initial guess
gauss_seidel(0, 0, 0)
#b) Solve the following system of equations by applying Gauss-Seidel iteration.
#3x + 2y - z = 6  ,   2x - 4y + 2z = - 3   ,  - 2x + y + 4z = 8