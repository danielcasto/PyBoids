class TwoVector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def to_tuple(self):
        return self.x, self.y
    
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

    def add(self, item):
        if type(item) == TwoVector:
            self.vec_add(item)
        else:
            self.scal_add(item)
    def mult(self, item):
        if type(item) == TwoVector:
            self.vec_mult(item)
        else:
            self.scal_mult(item)
    
    def norm(self):
        return (self.x**2 + self.y**2)**0.5
    