import pygame
from pygame import display, draw, Rect, image, KEYDOWN, QUIT, camera


class Simulation:

    def __init__(self):

        self.size = self.x, self.y = 800, 600
        self.screen = display.set_mode(self.size)
        display.set_caption('Camera Simulation')
        self.screen.fill((0, 0, 0))

        self.bg_img = image.load('space_(3840x2160).jpg')

        self.camera_x = 30
        self.camera_y = 30

        self.player_x = 40
        self.player_y = 40

        self.camera = camera.Camera()

    def draw(self):
        self.screen.blit(self.bg_img, (0, 0))

        draw.rect(
            self.screen, (0, 0, 255),
            Rect((self.camera_x, self.camera_y), (30, 30)),
            1
        )

        draw.rect(
            self.screen, (255, 0, 0),
            Rect((self.player_x, self.player_y), (10, 10)),
            1
        )

    def main(self):

        exit_ = False

        while not exit_:

            self.draw()
            display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:
                    exit_ = True

                elif event.type == KEYDOWN:

                    if event.key == pygame.K_UP:

                        self.camera_y -= 10
                        self.player_y -= 10

                    if event.key == pygame.K_DOWN:

                        self.camera_y += 10
                        self.player_y += 10

                    if event.key == pygame.K_RIGHT:
                        self.camera_x += 10
                        self.player_x += 10

                    if event.key == pygame.K_LEFT:
                        self.camera_x -= 10
                        self.player_x -= 10

                    self.draw()
                    display.flip()

        pygame.quit()


if __name__ == '__main__':
    Simulation().main()
