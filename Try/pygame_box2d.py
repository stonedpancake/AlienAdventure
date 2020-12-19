from Special.imports import *


class World:

    def __init__(self):

        self.size = self.x, self.y = 800, 600

        self.screen = display.set_mode(self.size)
        display.set_caption('Camera Simulation')
        self.screen.fill((0, 0, 0))

        self.world = b2World()
        self.world.gravity = (0, -5)

        self.bg_img = image.load('space_(3840x2160).jpg')
        self.camera = camera.Camera()

        self.camera_x = 30
        self.camera_y = 30

        self.player_x = 40
        self.player_y = 40

    def drawPolygons(self, screen, body):
        for fixture in body.fixtures:
            shape = fixture.shape
            vertices = [body.transform * v * 10 for v in shape.vertices]
            vertices = [(v[0], 450 - v[1]) for v in vertices]
            pygame.draw.polygon(screen, (255, 255, 255), vertices)

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

        '''ground = self.world.CreateStaticBody(
            position=(50, 50),
            shapes=b2PolygonShape(box=(60, 5)))

        obj = self.world.CreateDynamicBody(
            angle=15,
            position=(90, 90),
            shapes=b2PolygonShape(box=(5, 5)))'''

        '''circle = b2FixtureDef(
            shape=b2CircleShape(radius=3), density=1,
            friction=1.0, restitution=0.5
        )'''

    def main(self):

        exit_ = False

        while not exit_:

            self.draw()
            display.flip()

            for event_ in pygame.event.get():

                if event_.type == QUIT:
                    exit_ = True

                elif event_.type == KEYDOWN:

                    if event_.key == pygame.K_UP:
                        self.camera_y -= 10
                        self.player_y -= 10

                    if event_.key == pygame.K_DOWN:
                        self.camera_y += 10
                        self.player_y += 10

                    if event_.key == pygame.K_RIGHT:
                        self.camera_x += 10
                        self.player_x += 10

                    if event_.key == pygame.K_LEFT:
                        self.camera_x -= 10
                        self.player_x -= 10

                    self.draw()
                    display.flip()

        pygame.quit()


if __name__ == '__main__':
    World().main()
