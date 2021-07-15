class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Launch drawing")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Launch drawing with {self.title}"

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Launch drawing with {self.title}"

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
       return f"Launch drawing with {self.title}"

pen = Pen("Pen")
pencil = Pencil("Pencil")
handle = Handle("Handle")
print(pen.draw())
print(pencil.draw())
print(handle.draw())