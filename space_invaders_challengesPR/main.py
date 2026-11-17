import pygame
from player import Player
from obstacle import Obstacle

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Challenges")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 36)


def restart_game():
    player1 = Player(200, 500, (0, 255, 0))
    player2 = Player(550, 500, (0, 0, 255))
    obstacles = []
    score = 0
    return player1, player2, obstacles, score


def main():
    player1, player2, obstacles, score = restart_game()
    high_score = 0
    obstacle_timer = 0
    spawn_interval = 500
    paused = False
    game_over = False
    running = True
    survival_time = 0
    last_time = pygame.time.get_ticks()

    while running:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - last_time
        last_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not game_over:
                    paused = not paused

                if event.key == pygame.K_r and game_over:
                    player1, player2, obstacles, score = restart_game()
                    obstacle_timer = 0
                    spawn_interval = 500
                    survival_time = 0
                    paused = False
                    game_over = False

                if not paused and not game_over:
                    if event.key in (pygame.K_PLUS, pygame.K_KP_PLUS):
                        player1.change_speed(1)
                    if event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
                        player1.change_speed(-1)

        if not paused and not game_over:
            survival_time += elapsed_time
            keys = pygame.key.get_pressed()
            player1.move(keys, pygame.K_w, pygame.K_s,
                         pygame.K_a, pygame.K_d)
            player2.move(keys, pygame.K_UP, pygame.K_DOWN,
                         pygame.K_LEFT, pygame.K_RIGHT)
            player1.update(elapsed_time)
            player2.update(elapsed_time)
            obstacle_timer += elapsed_time

            if obstacle_timer >= spawn_interval:
                obstacles.append(Obstacle())
                obstacle_timer = 0

            for obstacle in obstacles[:]:
                obstacle.move()
                if player1.rect.colliderect(obstacle.rect):
                    player1.hit()
                if player2.rect.colliderect(obstacle.rect):
                    player2.hit()
                if obstacle.rect.top > HEIGHT:
                    obstacles.remove(obstacle)
                    score += 1
                    if score > high_score:
                        high_score = score
                    if score % 10 == 0:
                        spawn_interval = max(150, spawn_interval - 50)

            if player1.lives == 0 and player2.lives == 0:
                game_over = True

        screen.fill((0, 0, 0))
        player1.draw(screen)
        player2.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)

        score_text = small_font.render(
            "Score: " + str(score), True, (255, 255, 255)
        )
        screen.blit(score_text, (10, 10))
        seconds = survival_time // 1000
        time_text = small_font.render(
            "Time: " + str(seconds) + "s", True, (255, 255, 255)
        )
        screen.blit(time_text, (10, 45))
        speed_text = small_font.render(
            "Speed P1: " + str(player1.speed), True, (0, 255, 0)
        )
        screen.blit(speed_text, (10, 80))
        high_score_text = small_font.render(
            "High Score: " + str(high_score), True, (255, 255, 0)
        )
        screen.blit(high_score_text, (10, 115))
        lives1_text = small_font.render(
            "P1 Lives: " + str(player1.lives), True, (0, 255, 0)
        )
        screen.blit(lives1_text, (10, 150))
        lives2_text = small_font.render(
            "P2 Lives: " + str(player2.lives), True, (0, 100, 255)
        )
        screen.blit(lives2_text, (10, 185))

        if paused:
            text = font.render("PAUSE", True, (255, 255, 255))
            screen.blit(text, (320, 270))
        if game_over:
            text = font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(text, (260, 230))
            restart_text = small_font.render(
                "Press R to restart", True, (255, 255, 255)
            )
            screen.blit(restart_text, (290, 300))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
