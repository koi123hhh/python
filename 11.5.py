class Heart:
    def init (self,x,y,size):
        self.size=size#心形大小
        self.spend=size #移动顺序根据大小决定
        t = Turtle(visible=False,shape='circle')
        t.shapesize(size,size)
        color=(1,1-size/4,1-size/4)
        t.pencolor(color)
        t.fillcolor(color)
        t.penup()
        self.circle1=t.clone()
        self.circle1.goto(x-sqrt(size*size*160)/2,y)
        self.circle2 = t.clone()
        self.circle2.goto(x+sqrt(size*size*160)/2,y)




























