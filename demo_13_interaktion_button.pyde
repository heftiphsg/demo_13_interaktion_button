x = 200
y = 200
def setup():
    size(600, 600)
    background(255, 255, 255)
    
def draw():
    if mouseX >= x and mouseX <= x + 200 and mouseY >= y and mouseY <= y + 50 and mousePressed == True:
        fill(0, 255, 0)
    else:
        fill (60, 60, 60)
        
    rect(x, y, 200, 100)
