import pygame
run = True
pygame.init()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_buttons = pygame.mouse.get_pressed()

    button_msg = ""
    if mouse_buttons[0]:
        button_msg += "left mouse button  "
    if mouse_buttons[1]:
        button_msg += "middle mouse button  "
    if mouse_buttons[2]:
        button_msg += "right mouse button  "

    if button_msg == "":
        print("no button pressed")
    else:
        print(button_msg)