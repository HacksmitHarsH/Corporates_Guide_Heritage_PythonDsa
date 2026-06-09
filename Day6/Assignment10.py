def triangle_type(a, b, c):
    a, b, c = float(a), float(b), float(c)
    valid = a + b > c and a + c > b and b + c > a
    if not valid:
        return "Not a valid triangle"

    if a == b == c:
        kind = "Equilateral"
    elif a == b or b == c or a == c:
        kind = "Isosceles"
    else:
        kind = "Scalene"

    sides = sorted([a, b, c])
    right = sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
    return kind + (" and Right-angled" if right else "")


if __name__ == "__main__":
    try:
        sides = input("Enter three side lengths separated by spaces: ").split()
        if len(sides) != 3:
            raise ValueError
        print(triangle_type(*sides))
    except ValueError:
        print("Please enter three numeric side lengths.")
