import pygame
import random
import time

class Cube:

    def __init__(self):
        self.colors = {
        "R" : (255,000,000), "G" : (000,255,000), "B" : (000,000,255),
        "Y" : (255,255,000), "O" : (255,100,000), "W" : (255,255,255)}
        self.solved = "YYYYRRRRGGGGOOOOBBBBWWWW"

        # current state
        self.state = "YYYYRRRRGGGGOOOOBBBBWWWW"

        # possible moves and how the characters in self.state re-arrange
        # only using U F and R as this keeps one cubie in a fixed place to avoid reflections
        self.moves = {
        "U" : [1,2,3,0,8,9,6,7,12,13,10,11,16,17,14,15,4,5,18,19,20,21,22,23],
        "U'" : [3,0,1,2,16,17,6,7,4,5,10,11,8,9,14,15,12,13,18,19,20,21,22,23],
        "U2" : [2,3,0,1,12,13,6,7,16,17,10,11,4,5,14,15,8,9,18,19,20,21,22,23],
        "F" : [0,1,7,4,21,5,6,20,9,10,11,8,12,2,3,15,16,17,18,19,13,14,22,23],
        "F'" : [0,1,13,14,3,5,6,2,11,8,9,10,12,20,21,15,16,17,18,19,7,4,22,23],
        "F2" : [0,1,20,21,14,5,6,13,10,11,8,9,12,7,4,15,16,17,18,19,2,3,22,23],
        "R" : [8,1,2,11,4,5,6,7,20,9,10,23,13,14,15,12,16,3,0,19,18,21,22,17],
        "R'" : [18,1,2,17,4,5,6,7,0,9,10,3,15,12,13,14,16,23,20,19,8,21,22,11],
        "R2" : [20,1,2,23,4,5,6,7,18,9,10,17,14,15,12,13,16,11,8,19,0,21,22,3]
        }


    def move(self, move):
        """
        changes self.state to a new state to reflect the move
        move: string specifying the move
        """
        out = ''
        for val in self.moves[move]:
            out += self.state[val]
        self.state = out


    def draw_face(self, face, window, xy, width):
        """
        Draws one face of the cube
        Input:
            face: string of the face to display
            window: pygame window to display on
            xy: tuple with the x and y cordinates to draw the face at
            width: the width and height for the face to be drawn
        """
        width = width / 2 - (width/2/20)

        if face == "U":
            face = self.state[0:4]
        elif face == "L":
            face = self.state[4:8]
        elif face == "F":
            face = self.state[8:12]
        elif face == "R":
            face = self.state[12:16]
        elif face == "B":
            face = self.state[16:20]
        elif face == "D":
            face = self.state[20:24]

        rect1 = pygame.Rect((xy[0],xy[1], width, width))
        rect2 = pygame.Rect((xy[0]+(width+(width/10)),xy[1], width, width))
        rect3 = pygame.Rect((xy[0],xy[1]+(width+(width/10)), width, width))
        rect4 = pygame.Rect((xy[0]+(width+(width/10)),xy[1]+(width+(width/10)), width, width))
        pygame.draw.rect(window, self.colors[face[0]], rect2)
        pygame.draw.rect(window, self.colors[face[1]], rect1)
        pygame.draw.rect(window, self.colors[face[2]], rect3)
        pygame.draw.rect(window, self.colors[face[3]], rect4)


    def draw_cube(self, window):
        """
        Draws the current state of the cube
        """
        size = pygame.display.get_surface().get_size()
        width = (size[0]/4)

        window.fill((000,000,000))

        self.draw_face("U", window, (0 + (width*1), 0 + (width*0)), width)
        self.draw_face("L", window, (0 + (width*0), 0 + (width*1)), width)
        self.draw_face("F", window, (0 + (width*1) * 1, 0 + (width*1)), width)
        self.draw_face("R", window, (0 + (width*2), 0 + (width*1)), width)
        self.draw_face("B", window, (0 + (width*3), 0 + (width*1)), width)
        self.draw_face("D", window, (0 + (width*1), 0 + (width*2)), width)

        pygame.display.update()


if __name__ == "__main__":
    #initialize pygame and set up the window
    pygame.init()
    length = 1200
    size = (int(length),int((length/4)*3))
    window = pygame.display.set_mode(size)

    #initialize the cube
    cube = Cube()
    cube.draw_cube(window)
    time.sleep(4)

    running = True

    #game loop
    while running:

        # create event to exit program
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        time.sleep(0.25)
        cube.move(random.choice(["U","R","F","U'","R'","F'","U2","R2","F2"]))

        #Draw the cube
        cube.draw_cube(window)
