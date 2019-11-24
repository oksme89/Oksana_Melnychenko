# # import pygame
# # # Loop until the user clicks the close button.
# # done = False
# # # Used to manage how fast the screen updates
# # clock = pygame.time.Clock()
	
# # # -------- Main Program Loop -----------
# # while not done:
# # 	# --- Main event loop
# # 	for event in pygame.event.get(): # User did something
# # 		if event.type == pygame.QUIT: # If user clicked close
# # 		    done = True # Flag that we are done so we exit this loop
	
# # 	# --- Game logic should go here
# # 	# --- Drawing code should go here
# # 	# First, clear the screen to white. Don't put other drawing commands
# # 	# above this, or they will be erased with this command.
# # 	screen.fill(WHITE)
# # 	# --- Go ahead and update the screen with what we've drawn.
# # 	pygame.display.update()
# # 	# --- Limit to 60 frames per second
# # 	clock.tick(60)
# # import pygame
# # pygame.init()
# # gameDisplay=pygame.display.set_mode((400,300))
# # pygame.display.set_caption("My first game")
# # clock=pygame.time.Clock()
# # crashed=False
# # while not crashed:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             print("User asked to quit.")
# #         elif event.type == pygame.KEYDOWN:
# #             print("User pressed a key.")
# #         elif event.type == pygame.KEYUP:
# #             print("User let go of a key.")
# #         elif event.type == pygame.MOUSEBUTTONDOWN:
# #             print("User pressed a mouse button")

        
# #     pygame.display.update()

# #     clock.tick(60)

# # pygame.quit()
# # #quit()
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Draw primitives")
# clock = pygame.time.Clock()
# WHITE=(255,255,255)
# done = False
# clock = pygame.time.Clock()
# while not done:
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             done=True
    
#     #pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
#     # pygame.draw.line(screen, WHITE, [10, 30], [290, 15], 3)
#     # pygame.draw.line(screen, WHITE, [10, 50], [290, 35])
    
#     # #aaline згладжена лінія, товщина в цьому
#     # випадку не задається
# # pygame.draw.aaline(screen, WHITE, [10, 70], [290, 55])
# # pygame.display.update()
#     # r1 = pygame.Rect((150, 20, 100, 75))
# # pygame.draw.rect(screen, WHITE, (20, 20, 100, 75))
# # # pygame.draw.rect(screen, YELLOW, r1, 8)
#     # pygame.draw.circle(screen, YELLOW, (100, 100), 50,5)
#     # pygame.draw.circle(screen, PINK, (200, 100  Liubov Koliasa, [15.11.19 18:49]
#     # pygame.draw.circle(screen, YELLOW, (100, 100), 50,5)
#     #     pygame.draw.circle(screen, PINK, (200, 100), 50)


#     # pygame.draw.polygon(screen, WHITE, [[150, 10], [180, 50], [90, 90], [30, 30]],8)
#     # #pygame.draw.polygon(screen, WHITE, [[250, 110], [280, 150], [190, 190], [130, 130]])
#     #     pygame.draw.aalines(screen, WHITE, True, [[250, 110], [280, 150], [190, 190], [130, 130]])