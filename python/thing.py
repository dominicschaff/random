from PIL import Image, ImageDraw
from random import randint


def cc(colour, perc):
    return (max(0, min(255, int(colour[0]*perc))), max(0, min(255, int(colour[1]*perc))), max(0, min(255, int(colour[2]*perc))))


class Balls:

    def __init__(self, width, height):
        self.width, self.height = width, height
        self.img = Image.new('RGB', (width, height), color='black')
        self.draw = ImageDraw.Draw(self.img)

    def show(self):
        self.img.show()

    def save(self, filename):
        self.img.save(filename)

    def ball(self, middle, size, colour, through=0.4):

        for i in range(int(size*1.2), -1, -1):
            h = i/2
            bbox = [middle[0]-h, middle[1]-h, middle[0]+h, middle[1]+h]
            if i < size*through:
                p = max(i/(size*through), 0.6)
                self.draw.ellipse(bbox, fill=cc(colour, p))
            elif i > size:
                p = i/size
                self.draw.ellipse(bbox, fill=cc(colour, p))
            else:
                self.draw.ellipse(bbox, fill=colour)


if __name__ == '__main__':
    balls = Balls(1920, 1080)
    for f in range(2500):
        balls.ball([randint(0, 1920), randint(0, 1080)], randint(50, 200), (randint(0, 255), randint(0, 255), randint(0, 255)))
    balls.save("thing.png")
