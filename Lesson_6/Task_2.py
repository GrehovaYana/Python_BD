class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class AsphaltMass(Road):
    def __init__(self, _length, _width, as_mass_per_sm, thickness):
        super().__init__(_length, _width)
        self.as_mass_per_sm = as_mass_per_sm
        self.thickness = thickness

    def mass(self):
        return self._length * self._width * self.as_mass_per_sm * self.thickness


n = AsphaltMass(25, 10000, 30, 5)
print(f"{n.mass() / 1000} tons")
