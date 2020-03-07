import arcade

def Draw_cross1(positionX,positionY):
    addX=positionX*200
    addY=positionY*200
    shape=arcade.create_line(0+addX,0+addY,200+addX,200+addY,arcade.color.RED, 8)
    return shape

def Draw_cross2(positionX,positionY):
    addX=positionX*200
    addY=positionY*200
    shape2=arcade.create_line(0+addX,200+addY,200+addX,0+addY,arcade.color.RED, 8)
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