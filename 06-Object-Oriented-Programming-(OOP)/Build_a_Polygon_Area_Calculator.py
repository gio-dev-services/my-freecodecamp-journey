import math

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
    def set_width(self, value):
        self.width = value
        
    def set_height(self, value):
        self.height = value
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)
    
    def get_picture(self):
        if hasattr(self, "width") and hasattr(self, "height"):
            if self.width > 50 or self.height > 50:
                return "Too big for picture."
            stringa = ""
            for h in range(self.height):
                for w in range(self.width):
                    stringa += "*"
                stringa += "\n"
            return(stringa)
        if hasattr(self, "side"):
            stringa = ""
            if self.side > 50:
                return "Too big for picture."
            for s in range(self.side):
                for i in range(self.side):
                    stringa += "*"
                stringa += "\n"
            return stringa
        
    def get_amount_inside(self,obj):
        if isinstance(obj, Square): 
            return self.get_area() / obj.get_area()
        else: 
            return int((self.width / obj.width) * (self.height / obj.height))
   
            
            

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        
    def __str__(self):
        return f"Square(side={self.side})"
    
    def get_area(self):
        return self.side * self.side
    
    def get_perimeter(self):
        return 4 * self.side
    
    def get_diagonal(self):
        return math.sqrt(self.side**2 + self.side**2)
    
    def set_width(self, value):
        self.side = value
    
    def set_height(self, value):
        self.side = value
        
    def set_side(self, value):
        self.side = value




rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
