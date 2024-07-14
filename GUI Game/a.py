import pygame

pygame.init()
pygame.display.set_caption('Game')
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
FPS = 60
font = pygame.font.SysFont('Times New Normal Regular.ttf', 40)


def main(screen):
    clock = pygame.time.Clock()
    a = 10
    b = 50


    isGameRunning = True

    while isGameRunning:
        text1 = font.render(str(a), True, (0, 0, 0))
        text2 = font.render(str(b), True, (0, 0, 0))
        screen.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameRunning = False
            if event.type == pygame.K_SPACE:
                a -= 2
                b -= 10
            
                print(a)
                print(b)
        screen.blit(text1, (10, 10))
        screen.blit(text2, (580, 10))
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main(screen)