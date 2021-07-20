class Cell:
    def __init__(self, cell):
        self.cell = cell

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.cell / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.cell % cells_in_row)}'
        return f"Cells\n{row}"

    def __str__(self):
        return f"{self.cell}"

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)


cell_1 = Cell(14)
cell_2 = Cell(13)
print(f"Sum of cells:{cell_1 + cell_2}")
print(f"Substraction of cells: {cell_1 - cell_2}")
print(f"Multiplication of cells: {cell_1 * cell_2}")
print(f"Division of cells: {cell_1 / cell_2}")
print(cell_1.make_order(7))
print(cell_2.make_order(5))
