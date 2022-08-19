class Complex:
    def __init__(self, real, img) -> None:
        self.real = real
        self.img = img

    def displayComplex(self):
        print(f"Complex Number: {self.real} + {self.img}j")

    def __add__(self, obj):
        return (f"{self.real +obj.real} + {self.img + obj.img}j")
    def __mul__(self, obj):
        return (f"{(self.real *obj.real) - (self.img * obj.img)} + {(self.real * obj.img) + (self.img * obj.real)}j")


c1 = Complex(9, 7)
c2 = Complex(2, 11)
c1.displayComplex()
c2.displayComplex()
print(c1 + c2)
print(c1 * c2)