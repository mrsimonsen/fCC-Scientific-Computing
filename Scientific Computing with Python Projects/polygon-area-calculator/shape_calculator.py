class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, new):
    self.width = new

  def set_height(self, new):
    self.height = new

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width **2 + self.height **2)**0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    rep = ''
    for h in range(self.height):
      rep += "*"*self.width+"\n"
    return rep

  def get_amount_inside(self, other):
    return self.get_area() // other.get_area()

  
class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def __str__(self):
    return f"Square(side={self.width})"

  def set_side(self, new):
    self.width = new
    self.height = new

  def set_width(self, new):
    super().set_width(new)
    super().set_height(new)

  def set_height(self, new):
    super().set_width(new)
    super().set_height(new)
  
