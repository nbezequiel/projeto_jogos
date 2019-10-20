import random

class Generator(self):
    
    @classmethod
    def randomic_color(cls):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)

    @classmethod
    def randomic_pos(cls, width, height):
        x = random.randint(0,width)
        y = random.randint(0,height)
        return (x,y)
    
    @classmethod
    def randomic_size_square(cls, width, height):
        x = random.randint(0,(width*0.7))
        y = random.randint(0,(height*0.7))
        return (x,y)

    @classmethod
    def randomic_time(cls, width, height):
        x = random.randint(0,width)
        y = random.randint(0,height)
        return (x,y)   


    def __init__(self):
        pass
    

