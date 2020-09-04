class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, newWidth):
    self.width = newWidth

  def set_height(self, newHeight):
    self.height = newHeight  

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2) + (self.height ** 2)) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'

    return ('*' * self.width + '\n') * self.height

  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()

  def __str__(self):
    return ('Rectangle(width={0}, height={1})').format(self.width, self.height)


class Square(Rectangle):

  def __init__(self, side):
    Rectangle.width = side
    Rectangle.height = side

  def set_side(self, newSide):
    Rectangle.set_width(self, newSide)
    Rectangle.set_height(self, newSide)

  def __str__(self):
    return ('Square(side={0})').format(self.width)
