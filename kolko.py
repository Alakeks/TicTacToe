import arcade
import time
from shape import Draw_cross1,Draw_cross2,Draw_circle,Draw_frame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Kółko i Krzyżyk"    

class MyGame(arcade.Window):
    def __init__(self, width, height, title):        
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.frame=None
        self.mycircle=None
        self.cross=None
        self.Text=None
        self.scoreX=0
        self.score0=0
        self.zwyciesca=0
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
        self.end=0              
    def on_draw(self):
        arcade.start_render()
        for x in range(0, 601, 200):
            arcade.draw_line(x, 0, x, 600, arcade.color.WHITE, 5)
        for y in range(0, 601, 200):
            arcade.draw_line(0, y, 800, y, arcade.color.WHITE, 5)
        self.frame.draw()
        self.cross.draw()
        self.mycircle.draw()        
        arcade.draw_text("Wynik X:"+str(self.scoreX)+" Wynik O:"+str(self.score0),150,550,arcade.color.RED, 30)

        if self.end==1:
            arcade.draw_text("END", 100, 200, arcade.color.RED, 200)            
            self.setup()
        
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
                self.end=1
                self.zwyciesca=v
        for i in range(3):
            if self.InfoMatrix[0][i]==self.InfoMatrix[1][i] and self.InfoMatrix[0][i]==self.InfoMatrix[2][i] and self.InfoMatrix[0][i]!=0 :
                self.end=1
                self.zwyciesca=self.InfoMatrix[0][i]
        if  self.InfoMatrix[0][0]==self.InfoMatrix[1][1] and self.InfoMatrix[1][1]==self.InfoMatrix[2][2] and self.InfoMatrix[0][0]!=0:
                self.end=1
                self.zwyciesca=self.InfoMatrix[0][0]
        if  self.InfoMatrix[0][2]==self.InfoMatrix[1][1] and self.InfoMatrix[1][1]==self.InfoMatrix[2][0] and self.InfoMatrix[0][2]!=0:
                self.end=1
                self.zwyciesca=self.InfoMatrix[0][2]
        if self.zwyciesca==2:
            self.scoreX+=1
            self.zwyciesca=0
        elif self.zwyciesca==1:
            self.score0+=1
            self.zwyciesca=0

        
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

