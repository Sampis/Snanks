orm_storlek = 10
orm_hastighet = 15

x1 = screen_width / 2
y1 = screen_height / 2

x1_change = 0
y1_change = 0

snake_list = []
Length_of_snake = 1

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Poäng:" + str(score), True, black)
    screen.blit(value, [0, 0])

def our_snake(orm_storlek, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], orm_storlek, orm_storlek])

while not game_over:

    while game_close == True:
        screen.fill(blue)
        message("You Lost, press Q to exit or C to play again", black)
        your_score(Length_of_snake - 1)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    gameloop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x1_change = -orm_storlek
                y1_change = 0
            elif event.key == pygame.K_d:
                x1_change = orm_storlek
                y1_change = 0
            elif event.key == pygame.K_w:
                y1_change = -orm_storlek
                x1_change = 0
            elif event.key == pygame.K_s:
                y1_change = orm_storlek
                x1_change = 0

    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
        game_close = True
    x1 += x1_change
    y1 += y1_change
    screen.fill(blue)
    pygame.draw.rect(screen, green, [foodx, foody, orm_storlek, orm_storlek])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > Length_of_snake:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_close = True

    our_snake(orm_storlek, snake_list)
    your_score(Length_of_snake - 1)

    pygame.display.update()
