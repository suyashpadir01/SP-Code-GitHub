def perimeter_rectangle(length, width):
    return 2 * (length + width)
l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
perimeter = perimeter_rectangle(l, w)
print("Perimeter of Rectangle =", perimeter)
