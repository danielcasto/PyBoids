class TwoVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __init__(self):
        self.x = 0
        self.y = 0

    def vec_add(self, vec):
        self.x += vec.x
        self.y += vec.y
    
    def vec_mult(self, vec):
        self.x *= vec.x
        self.y *= vec.y

    def scal_add(self, scalar):
        self.x += scalar
        self.y += scalar
    
    def scal_mult(self, scalar):
        self.x *= scalar
        self.y *= scalar
    
    def scal_div(self, scalar):
        self.x /= scalar
        self.y /= scalar
    