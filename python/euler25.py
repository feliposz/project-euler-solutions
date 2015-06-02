def euler25():
    """Solves problem 25 of Project Euler."""
    a = 1
    b = 1
    n = 1
    while (len(str(a)) < 1000):
        a, b = b, a + b
        n += 1
    print(n)

if __name__ == "__main__":
    euler8()
