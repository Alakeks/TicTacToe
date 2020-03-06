import arcade
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Kółko i Krzyżyk"
    
def Draw_cross1(positionX,positionY):
    addX=positionX*200
    addY=positionY*200
    shape=arcade.create_line(0+addX,0+addY,200+addX,200+addY,
                                arcade.color.RED, 8)
    return shape

def Draw_cross2(positionX,positionY):
    addX=positionX*200
    addY=positionY*200
    shape2=arcade.create_line(0+addX,200+addY,200+addX,0+addY,
                               arcade.color.RED, 8)
    return shape2

def Draw_circle(positionX,positionY):
    addX=positionX*200
    addY=positionY*200
    shape=arcade.create_ellipse_outline(100+addX, 100+addY, 95,95, arcade.color.BLUE,1)
    return shape


def Draw_frame():
    shape=arcade.create_rectangle_outline(100, 100, 195, 195,arcade.color.BRITISH_RACING_GREEN,10)
    shape_list = arcade.ShapeElementList()
    shape_list.append(shape)
    return shape_list

class MyGame(arcade.Window):
    def __init__(self, width, height, title):        
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.frame=None
        self.mycircle=None
        self.cross=None
        self.Text=None
    def setup(self):
        self.MiejsceX=0
        self.MiejsceY=0
        self.firecirecle=0
        self.fireCross=0
        self.InfoMatrix=[[0,0,0],[0,0,0],[0,0,0]] # each row and column are poles on the map 0 is empyt 1 is cross and 2 i circle
        self.mycircle=arcade.ShapeElementList()
        self.cross=arcade.ShapeElementList()
        self.Text=arcade.ShapeElementList()
        self.frame=Draw_frame()
    def on_draw(self):
        arcade.start_render()
        for x in range(0, 601, 200):
            arcade.draw_line(x, 0, x, 600, arcade.color.WHITE, 5)
        for y in range(0, 601, 200):
            arcade.draw_line(0, y, 800, y, arcade.color.WHITE, 5)
        self.frame.draw()
        self.cross.draw()
        self.mycircle.draw()
        self.Text.draw()
        arcade.draw_text("END",300, 300, arcade.color.RED, 80)
    def on_update(self, delta_time):
        self.frame.center_x = self.frame.change_x
        self.frame.center_y = self.frame.change_y
        if self.firecirecle==1 and self.InfoMatrix[self.MiejsceY][self.MiejsceX]==0 :
            self.mycircle.append(Draw_circle(self.MiejsceX,self.MiejsceY))
            self.firecirecle=0
            self.InfoMatrix[self.MiejsceY][self.MiejsceX]=1
        else: self.firecirecle=0
        if self.fireCross==1 and self.InfoMatrix[self.MiejsceY][self.MiejsceX]==0 :
            self.mycircle.append(Draw_cross1(self.MiejsceX,self.MiejsceY))
            self.mycircle.append(Draw_cross2(self.MiejsceX,self.MiejsceY))
            self.fireCross=0
            self.InfoMatrix[self.MiejsceY][self.MiejsceX]=2
        else :self.fireCross=0
        # kołko i krzyżyk zasady wygranej
        
        for v,k,j in self.InfoMatrix:
            if v==k and k==j and v!=0:
                arcade.draw_text("END",300, 300, arcade.color.RED, 20)
                #time.sleep(5)
                self.setup()
        for i in range(3):
            if self.InfoMatrix[0][i]==self.InfoMatrix[1][i] and self.InfoMatrix[0][i]==self.InfoMatrix[2][i] and self.InfoMatrix[0][i]!=0 :
                arcade.draw_text("END",300, 300, arcade.color.RED, 80)
                #time.sleep(5)
                self.setup()
        if  self.InfoMatrix[0][0]==self.InfoMatrix[1][1] and self.InfoMatrix[1][1]==self.InfoMatrix[2][2] and self.InfoMatrix[0][0]!=0:
                arcade.draw_text("END",300, 300, arcade.color.RED, 80)
                #time.sleep(5)
                self.setup()
        if  self.InfoMatrix[0][2]==self.InfoMatrix[1][1] and self.InfoMatrix[1][1]==self.InfoMatrix[2][0] and self.InfoMatrix[0][2]!=0:
                arcade.draw_text("END",300, 300, arcade.color.RED, 80)
                #time.sleep(5)
                self.setup()
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.frame.change_y += 200
            self.MiejsceY+=1
        elif key == arcade.key.DOWN:
            self.frame.change_y -= 200
            self.MiejsceY-=1
        elif key == arcade.key.LEFT:
            self.frame.change_x -= 200
            self.MiejsceX-=1
        elif key == arcade.key.RIGHT:
            self.frame.change_x += 200
            self.MiejsceX+=1
        elif key==arcade.key.SPACE:
            self.firecirecle=1
        elif key==arcade.key.ENTER:
            self.fireCross=1    

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()

