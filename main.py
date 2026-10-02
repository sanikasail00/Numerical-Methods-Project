# ============================================================
#          NUMERICAL METHODS AND APPLICATIONS
# ============================================================

import math


# ============================================================
# COMMON FUNCTION
# ============================================================

def evaluate_function(expression, x, y=None):

    functions = {
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "asin": math.asin,
        "acos": math.acos,
        "atan": math.atan,
        "exp": math.exp,
        "log": math.log,
        "log10": math.log10,
        "pi": math.pi,
        "e": math.e,
        "abs": abs
    }

    variables = {
        "x": x,
        "y": y
    }

    try:
        return float(
            eval(
                expression,
                {"__builtins__": {}},
                {**functions, **variables}
            )
        )
    except Exception:
        raise ValueError("Invalid mathematical expression.")


# ============================================================
# WELCOME SCREEN
# ============================================================

def welcome_screen():

    print("\n" + "=" * 60)
    print("           NUMERICAL METHODS APPLICATION")
    print("=" * 60)
    print("Student Name : Sanika Sunil Sail")
    print("USN          : 4SF23CS189")
    print("Subject      : Numerical Methods and Applications")
    print("=" * 60)

    input("\nPress Enter to continue...")


# ============================================================
# MODULE 1
# ============================================================

def fixed_point_iteration():

    print("\n" + "=" * 60)
    print("             FIXED POINT ITERATION METHOD")
    print("=" * 60)

    expression = input("\nEnter g(x): ")

    try:
        x = float(input("Enter initial value: "))
        tolerance = float(input("Enter tolerance: "))
        max_iterations = int(input("Enter maximum iterations: "))

        if tolerance <= 0 or max_iterations <= 0:
            raise ValueError

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    print("\n" + "-" * 65)
    print(f"{'Iteration':<12}{'x':<18}{'g(x)':<18}{'Error':<15}")
    print("-" * 65)

    converged = False

    for i in range(1, max_iterations + 1):

        try:
            new_x = evaluate_function(expression, x)
        except ValueError:
            print("\nInvalid g(x) expression.")
            input("\nPress Enter to continue...")
            return

        error = abs(new_x - x)

        print(
            f"{i:<12}"
            f"{x:<18.10f}"
            f"{new_x:<18.10f}"
            f"{error:<15.10f}"
        )

        if error < tolerance:
            converged = True
            x = new_x
            break

        x = new_x

    print("-" * 65)

    if converged:
        print("\nConvergence achieved.")
    else:
        print("\nMaximum iterations reached.")

    print(f"Approximate root = {x:.10f}")
    print(f"Iterations completed = {i}")

    input("\nPress Enter to continue...")


def gauss_jacobi():

    print("\n" + "=" * 60)
    print("                  GAUSS-JACOBI")
    print("=" * 60)

    try:
        n = int(input("\nEnter number of equations: "))

        matrix = []

        print("\nEnter the augmented matrix:")

        for i in range(n):

            row = list(map(float, input(f"Row {i + 1}: ").split()))

            if len(row) != n + 1:
                print("Each row must contain n+1 values.")
                input("\nPress Enter to continue...")
                return

            matrix.append(row)

        x = []

        print("\nEnter initial values:")

        for i in range(n):
            x.append(float(input(f"x{i + 1} = ")))

        tolerance = float(input("Enter tolerance: "))
        max_iterations = int(input("Enter maximum iterations: "))

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    print("\n" + "-" * 65)

    converged = False

    for iteration in range(1, max_iterations + 1):

        new_x = [0.0] * n

        for i in range(n):

            if matrix[i][i] == 0:
                print("\nZero diagonal element.")
                input("\nPress Enter to continue...")
                return

            value = matrix[i][n]

            for j in range(n):

                if i != j:
                    value -= matrix[i][j] * x[j]

            new_x[i] = value / matrix[i][i]

        print(
            f"Iteration {iteration}: ",
            " ".join(f"{value:.8f}" for value in new_x)
        )

        error = max(
            abs(new_x[i] - x[i])
            for i in range(n)
        )

        x = new_x

        if error < tolerance:
            converged = True
            break

    print("-" * 65)

    if converged:
        print("\nConvergence achieved.")
    else:
        print("\nMaximum iterations reached.")

    print("\nSolution:")

    for i in range(n):
        print(f"x{i + 1} = {x[i]:.8f}")

    input("\nPress Enter to continue...")


def gauss_jordan():

    print("\n" + "=" * 60)
    print("                 GAUSS-JORDAN")
    print("=" * 60)

    try:
        n = int(input("\nEnter number of equations: "))

        matrix = []

        print("\nEnter the augmented matrix:")

        for i in range(n):

            row = list(map(float, input(f"Row {i + 1}: ").split()))

            if len(row) != n + 1:
                print("Each row must contain n+1 values.")
                input("\nPress Enter to continue...")
                return

            matrix.append(row)

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    for i in range(n):

        pivot = i

        for j in range(i + 1, n):

            if abs(matrix[j][i]) > abs(matrix[pivot][i]):
                pivot = j

        if abs(matrix[pivot][i]) < 1e-12:
            print("\nNo unique solution.")
            input("\nPress Enter to continue...")
            return

        matrix[i], matrix[pivot] = matrix[pivot], matrix[i]

        divisor = matrix[i][i]

        for j in range(n + 1):
            matrix[i][j] /= divisor

        for k in range(n):

            if k != i:

                factor = matrix[k][i]

                for j in range(n + 1):
                    matrix[k][j] -= factor * matrix[i][j]

    print("\nReduced matrix:")

    for row in matrix:
        print(" ".join(f"{value:.6f}" for value in row))

    print("\nSolution:")

    for i in range(n):
        print(f"x{i + 1} = {matrix[i][n]:.8f}")

    input("\nPress Enter to continue...")


def module1_menu():

    while True:

        print("\n" + "=" * 60)
        print("                     MODULE 1")
        print("=" * 60)

        print("1. Fixed Point Iteration Method")
        print("2. Gauss-Jacobi")
        print("3. Gauss-Jordan")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        match choice:

            case "1":
                fixed_point_iteration()

            case "2":
                gauss_jacobi()

            case "3":
                gauss_jordan()

            case "4":
                return

            case _:
                print("\nInvalid choice.")
                input("\nPress Enter to continue...")


# ============================================================
# MODULE 2
# ============================================================

def lagrange_interpolation():

    print("\n" + "=" * 60)
    print("             LAGRANGE'S INTERPOLATION METHOD")
    print("=" * 60)

    try:
        n = int(input("\nEnter number of data points: "))

        x = list(map(float, input("Enter x values: ").split()))
        y = list(map(float, input("Enter y values: ").split()))

        if len(x) != n or len(y) != n:
            print("Number of values does not match.")
            input("\nPress Enter to continue...")
            return

        value = float(input("Enter x value: "))

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    result = 0.0

    for i in range(n):

        term = y[i]

        for j in range(n):

            if i != j:
                term *= (value - x[j]) / (x[i] - x[j])

        result += term

    print(f"\nInterpolated value = {result:.10f}")

    input("\nPress Enter to continue...")


def linear_curve_fitting():

    print("\n" + "=" * 60)
    print("        LINEAR FITTING OF CURVE (STRAIGHT LINE)")
    print("=" * 60)

    try:
        n = int(input("\nEnter number of data points: "))

        x = list(map(float, input("Enter x values: ").split()))
        y = list(map(float, input("Enter y values: ").split()))

        if len(x) != n or len(y) != n:
            print("Number of values does not match.")
            input("\nPress Enter to continue...")
            return

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_x2 = sum(value ** 2 for value in x)

    denominator = n * sum_x2 - sum_x ** 2

    if denominator == 0:
        print("\nCannot fit a straight line.")
        input("\nPress Enter to continue...")
        return

    a = (sum_y * sum_x2 - sum_x * sum_xy) / denominator
    b = (n * sum_xy - sum_x * sum_y) / denominator

    print("\nFitted equation:")
    print(f"y = {a:.8f} + {b:.8f}x")

    input("\nPress Enter to continue...")


def lagrange_inverse_interpolation():

    print("\n" + "=" * 60)
    print("       LAGRANGE'S INVERSE INTERPOLATION METHOD")
    print("=" * 60)

    try:
        n = int(input("\nEnter number of data points: "))

        x = list(map(float, input("Enter x values: ").split()))
        y = list(map(float, input("Enter y values: ").split()))

        if len(x) != n or len(y) != n:
            print("Number of values does not match.")
            input("\nPress Enter to continue...")
            return

        target = float(input("Enter y value: "))

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    result = 0.0

    for i in range(n):

        term = x[i]

        for j in range(n):

            if i != j:
                term *= (target - y[j]) / (y[i] - y[j])

        result += term

    print(f"\nCorresponding x value = {result:.10f}")

    input("\nPress Enter to continue...")


def module2_menu():

    while True:

        print("\n" + "=" * 60)
        print("                     MODULE 2")
        print("=" * 60)

        print("1. Lagrange's Interpolation Method")
        print("2. Linear Fitting of Curve (Straight Line)")
        print("3. Lagrange's Inverse Interpolation Method")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        match choice:

            case "1":
                lagrange_interpolation()

            case "2":
                linear_curve_fitting()

            case "3":
                lagrange_inverse_interpolation()

            case "4":
                return

            case _:
                print("\nInvalid choice.")
                input("\nPress Enter to continue...")


# ============================================================
# MODULE 3
# ============================================================

def simpsons_one_third():

    print("\n" + "=" * 60)
    print("                  SIMPSON'S 1/3 RULE")
    print("=" * 60)

    try:
        expression = input("\nEnter f(x): ")
        a = float(input("Enter lower limit: "))
        b = float(input("Enter upper limit: "))
        n = int(input("Enter number of intervals: "))

        if n <= 0 or n % 2 != 0:
            print("\nNumber of intervals must be even.")
            input("\nPress Enter to continue...")
            return

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    h = (b - a) / n

    result = (
        evaluate_function(expression, a)
        + evaluate_function(expression, b)
    )

    for i in range(1, n):

        value = evaluate_function(
            expression,
            a + i * h
        )

        if i % 2 == 0:
            result += 2 * value
        else:
            result += 4 * value

    result *= h / 3

    print(f"\nIntegral value = {result:.10f}")

    input("\nPress Enter to continue...")


def romberg_integration():

    print("\n" + "=" * 60)
    print("                  ROMBERG'S INTEGRATION")
    print("=" * 60)

    try:
        expression = input("\nEnter f(x): ")
        a = float(input("Enter lower limit: "))
        b = float(input("Enter upper limit: "))
        levels = int(input("Enter number of levels: "))

        if levels <= 0:
            raise ValueError

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    R = [[0.0] * levels for _ in range(levels)]

    for i in range(levels):

        n = 2 ** i
        h = (b - a) / n

        total = (
            evaluate_function(expression, a)
            + evaluate_function(expression, b)
        )

        for j in range(1, n):
            total += 2 * evaluate_function(
                expression,
                a + j * h
            )

        R[i][0] = h * total / 2

        for j in range(1, i + 1):

            R[i][j] = (
                4 ** j * R[i][j - 1]
                - R[i - 1][j - 1]
            ) / (4 ** j - 1)

    print("\nRomberg Table:")

    for i in range(levels):
        print(
            " ".join(
                f"{R[i][j]:12.8f}"
                for j in range(i + 1)
            )
        )

    print(
        f"\nIntegral value = "
        f"{R[levels - 1][levels - 1]:.10f}"
    )

    input("\nPress Enter to continue...")


def newton_backward():

    print("\n" + "=" * 60)
    print("       NEWTON'S BACKWARD INTERPOLATION FORMULA")
    print("=" * 60)

    try:
        n = int(input("\nEnter number of data points: "))

        x = list(map(float, input("Enter x values: ").split()))
        y = list(map(float, input("Enter y values: ").split()))

        if len(x) != n or len(y) != n:
            print("Number of values does not match.")
            input("\nPress Enter to continue...")
            return

        value = float(input("Enter x value: "))

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    h = x[1] - x[0]

    differences = [y[:]]

    for i in range(1, n):

        previous = differences[-1]

        current = []

        for j in range(len(previous) - 1):
            current.append(
                previous[j + 1] - previous[j]
            )

        differences.append(current)

    p = (value - x[-1]) / h

    result = differences[0][-1]
    term = 1.0

    for i in range(1, n):

        term *= (p + i - 1) / i

        result += term * differences[i][-1]

    print(f"\nInterpolated value = {result:.10f}")

    input("\nPress Enter to continue...")


def module3_menu():

    while True:

        print("\n" + "=" * 60)
        print("                     MODULE 3")
        print("=" * 60)

        print("1. Simpson's 1/3 Rule")
        print("2. Romberg's Integration")
        print("3. Newton's Backward Interpolation Formula")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        match choice:

            case "1":
                simpsons_one_third()

            case "2":
                romberg_integration()

            case "3":
                newton_backward()

            case "4":
                return

            case _:
                print("\nInvalid choice.")
                input("\nPress Enter to continue...")


# ============================================================
# MODULE 4
# ============================================================

def adams_bashforth():

    print("\n" + "=" * 60)
    print("                 ADAMS-BASHFORTH METHOD")
    print("=" * 60)

    try:
        expression = input("\nEnter dy/dx = f(x,y): ")

        x0 = float(input("Enter x0: "))
        y0 = float(input("Enter y0: "))
        h = float(input("Enter step size: "))
        steps = int(input("Enter number of steps: "))

        if steps < 4:
            print("\nEnter at least 4 steps.")
            input("\nPress Enter to continue...")
            return

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    x_values = [x0]
    y_values = [y0]

    # First three points using RK4
    for _ in range(3):

        x = x_values[-1]
        y = y_values[-1]

        k1 = evaluate_function(expression, x, y)

        k2 = evaluate_function(
            expression,
            x + h / 2,
            y + h * k1 / 2
        )

        k3 = evaluate_function(
            expression,
            x + h / 2,
            y + h * k2 / 2
        )

        k4 = evaluate_function(
            expression,
            x + h,
            y + h * k3
        )

        new_y = y + h * (
            k1 + 2 * k2 + 2 * k3 + k4
        ) / 6

        x_values.append(x + h)
        y_values.append(new_y)

    while len(x_values) <= steps:

        n = len(x_values) - 1

        f0 = evaluate_function(
            expression,
            x_values[n],
            y_values[n]
        )

        f1 = evaluate_function(
            expression,
            x_values[n - 1],
            y_values[n - 1]
        )

        f2 = evaluate_function(
            expression,
            x_values[n - 2],
            y_values[n - 2]
        )

        f3 = evaluate_function(
            expression,
            x_values[n - 3],
            y_values[n - 3]
        )

        new_y = y_values[n] + h / 24 * (
            55 * f0
            - 59 * f1
            + 37 * f2
            - 9 * f3
        )

        x_values.append(x_values[n] + h)
        y_values.append(new_y)

    print("\n" + "-" * 45)
    print(f"{'x':<20}{'y':<20}")
    print("-" * 45)

    for x, y in zip(x_values, y_values):
        print(f"{x:<20.8f}{y:<20.8f}")

    input("\nPress Enter to continue...")


def modified_euler():

    print("\n" + "=" * 60)
    print("              MODIFIED EULER'S METHOD (HEUN)")
    print("=" * 60)

    try:
        expression = input("\nEnter dy/dx = f(x,y): ")

        x = float(input("Enter x0: "))
        y = float(input("Enter y0: "))
        h = float(input("Enter step size: "))
        steps = int(input("Enter number of steps: "))

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    print("\n" + "-" * 45)
    print(f"{'x':<20}{'y':<20}")
    print("-" * 45)

    print(f"{x:<20.8f}{y:<20.8f}")

    for _ in range(steps):

        f1 = evaluate_function(expression, x, y)

        predictor = y + h * f1

        f2 = evaluate_function(
            expression,
            x + h,
            predictor
        )

        y = y + h * (f1 + f2) / 2
        x = x + h

        print(f"{x:<20.8f}{y:<20.8f}")

    input("\nPress Enter to continue...")


def runge_kutta():

    print("\n" + "=" * 60)
    print("                FOURTH-ORDER RUNGE-KUTTA")
    print("=" * 60)

    try:
        expression = input("\nEnter dy/dx = f(x,y): ")

        x = float(input("Enter x0: "))
        y = float(input("Enter y0: "))
        h = float(input("Enter step size: "))
        steps = int(input("Enter number of steps: "))

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    print("\n" + "-" * 45)
    print(f"{'x':<20}{'y':<20}")
    print("-" * 45)

    print(f"{x:<20.8f}{y:<20.8f}")

    for _ in range(steps):

        k1 = evaluate_function(expression, x, y)

        k2 = evaluate_function(
            expression,
            x + h / 2,
            y + h * k1 / 2
        )

        k3 = evaluate_function(
            expression,
            x + h / 2,
            y + h * k2 / 2
        )

        k4 = evaluate_function(
            expression,
            x + h,
            y + h * k3
        )

        y = y + h * (
            k1 + 2 * k2 + 2 * k3 + k4
        ) / 6

        x = x + h

        print(f"{x:<20.8f}{y:<20.8f}")

    input("\nPress Enter to continue...")


def module4_menu():

    while True:

        print("\n" + "=" * 60)
        print("                     MODULE 4")
        print("=" * 60)

        print("1. Adams-Bashforth Method")
        print("2. Modified Euler's Method (Heun)")
        print("3. Fourth-Order Runge-Kutta")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        match choice:

            case "1":
                adams_bashforth()

            case "2":
                modified_euler()

            case "3":
                runge_kutta()

            case "4":
                return

            case _:
                print("\nInvalid choice.")
                input("\nPress Enter to continue...")


# ============================================================
# MODULE 5
# ============================================================

def heat_equation():

    print("\n" + "=" * 60)
    print("                 HEAT EQUATION - EXPLICIT")
    print("=" * 60)

    try:
        length = float(input("\nEnter length: "))
        alpha = float(input("Enter thermal diffusivity: "))
        dx = float(input("Enter dx: "))
        dt = float(input("Enter dt: "))
        time_steps = int(input("Enter number of time steps: "))

        left = float(input("Enter left boundary temperature: "))
        right = float(input("Enter right boundary temperature: "))
        initial = float(input("Enter initial interior temperature: "))

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    nx = int(round(length / dx))

    if nx < 2:
        print("\nInvalid dx.")
        input("\nPress Enter to continue...")
        return

    r = alpha * dt / dx ** 2

    print(f"\nr = {r:.6f}")

    if r > 0.5:
        print("Warning: Stability condition r <= 0.5 is not satisfied.")

    temperature = [initial] * (nx + 1)

    temperature[0] = left
    temperature[nx] = right

    print("\nTemperature values:")

    for step in range(time_steps + 1):

        print(
            f"Step {step}: ",
            " ".join(
                f"{value:.4f}"
                for value in temperature
            )
        )

        new_temperature = temperature[:]

        for i in range(1, nx):

            new_temperature[i] = (
                temperature[i]
                + r * (
                    temperature[i + 1]
                    - 2 * temperature[i]
                    + temperature[i - 1]
                )
            )

        new_temperature[0] = left
        new_temperature[nx] = right

        temperature = new_temperature

    input("\nPress Enter to continue...")


def two_point_bvp():

    print("\n" + "=" * 60)
    print("                   TWO-POINT LINEAR BVP")
    print("=" * 60)

    print("\nEquation form: y'' = p(x)y' + q(x)y + r(x)")

    try:
        p_expr = input("\nEnter p(x): ")
        q_expr = input("Enter q(x): ")
        r_expr = input("Enter r(x): ")

        a = float(input("Enter a: "))
        b = float(input("Enter b: "))

        ya = float(input("Enter y(a): "))
        yb = float(input("Enter y(b): "))

        n = int(input("Enter number of intervals: "))

        if n < 2:
            raise ValueError

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    h = (b - a) / n
    size = n - 1

    matrix = [
        [0.0] * (size + 1)
        for _ in range(size)
    ]

    for i in range(1, n):

        x = a + i * h

        p = evaluate_function(p_expr, x)
        q = evaluate_function(q_expr, x)
        r = evaluate_function(r_expr, x)

        lower = 1 + h * p / 2
        diagonal = -2 - h ** 2 * q
        upper = 1 - h * p / 2

        row = i - 1

        if row > 0:
            matrix[row][row - 1] = lower

        matrix[row][row] = diagonal

        if row < size - 1:
            matrix[row][row + 1] = upper

        matrix[row][size] = -h ** 2 * r

        if i == 1:
            matrix[row][size] -= lower * ya

        if i == n - 1:
            matrix[row][size] -= upper * yb

    # Gaussian elimination
    for i in range(size):

        pivot = i

        for j in range(i + 1, size):

            if abs(matrix[j][i]) > abs(matrix[pivot][i]):
                pivot = j

        matrix[i], matrix[pivot] = matrix[pivot], matrix[i]

        for j in range(i + 1, size):

            factor = matrix[j][i] / matrix[i][i]

            for k in range(i, size + 1):
                matrix[j][k] -= factor * matrix[i][k]

    solution = [0.0] * size

    for i in range(size - 1, -1, -1):

        value = matrix[i][size]

        for j in range(i + 1, size):
            value -= matrix[i][j] * solution[j]

        solution[i] = value / matrix[i][i]

    print("\n" + "-" * 40)
    print(f"{'x':<15}{'y':<15}")
    print("-" * 40)

    print(f"{a:<15.6f}{ya:<15.6f}")

    for i in range(size):

        x = a + (i + 1) * h

        print(
            f"{x:<15.6f}"
            f"{solution[i]:<15.6f}"
        )

    print(f"{b:<15.6f}{yb:<15.6f}")

    input("\nPress Enter to continue...")


def poisson_solver():

    print("\n" + "=" * 60)
    print("                    POISSON SOLVER")
    print("=" * 60)

    print("\nEquation: u_xx + u_yy = f(x,y)")

    try:
        nx = int(input("\nEnter number of x intervals: "))
        ny = int(input("Enter number of y intervals: "))

        width = float(input("Enter width: "))
        height = float(input("Enter height: "))

        f_expr = input("Enter f(x,y): ")

        left = float(input("Enter left boundary value: "))
        right = float(input("Enter right boundary value: "))
        bottom = float(input("Enter bottom boundary value: "))
        top = float(input("Enter top boundary value: "))

        iterations = int(input("Enter number of iterations: "))

        if nx < 2 or ny < 2:
            raise ValueError

    except ValueError:
        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    hx = width / nx
    hy = height / ny

    u = [
        [0.0] * (ny + 1)
        for _ in range(nx + 1)
    ]

    for j in range(ny + 1):
        u[0][j] = left
        u[nx][j] = right

    for i in range(nx + 1):
        u[i][0] = bottom
        u[i][ny] = top

    denominator = (
        2 / hx ** 2
        + 2 / hy ** 2
    )

    for _ in range(iterations):

        for i in range(1, nx):

            x = i * hx

            for j in range(1, ny):

                y = j * hy

                f_value = evaluate_function(
                    f_expr,
                    x,
                    y
                )

                u[i][j] = (
                    (
                        (u[i + 1][j] + u[i - 1][j]) / hx ** 2
                        + (u[i][j + 1] + u[i][j - 1]) / hy ** 2
                        - f_value
                    )
                    / denominator
                )

    print("\nSolution:")

    for j in range(ny, -1, -1):

        print(
            " ".join(
                f"{u[i][j]:10.5f}"
                for i in range(nx + 1)
            )
        )

    input("\nPress Enter to continue...")


def module5_menu():

    while True:

        print("\n" + "=" * 60)
        print("                     MODULE 5")
        print("=" * 60)

        print("1. Heat Equation – Explicit")
        print("2. Two-Point Linear BVP")
        print("3. Poisson Solver")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        match choice:

            case "1":
                heat_equation()

            case "2":
                two_point_bvp()

            case "3":
                poisson_solver()

            case "4":
                return

            case _:
                print("\nInvalid choice.")
                input("\nPress Enter to continue...")


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():

    while True:

        print("\n" + "=" * 60)
        print("                    MAIN MENU")
        print("=" * 60)

        print("1. Module 1")
        print("2. Module 2")
        print("3. Module 3")
        print("4. Module 4")
        print("5. Module 5")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        match choice:

            case "1":
                module1_menu()

            case "2":
                module2_menu()

            case "3":
                module3_menu()

            case "4":
                module4_menu()

            case "5":
                module5_menu()

            case "6":
                print("\nProgram ended.")
                break

            case _:
                print("\nInvalid choice. Please enter 1 to 6.")
                input("\nPress Enter to continue...")


# ============================================================
# PROGRAM START
# ============================================================

welcome_screen()
main_menu()