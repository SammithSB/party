''' Game of Life '''


def game_of_life(board):
    '''
    Function that implements game of life
    '''
    new_board = []
    for row in board:
        new_board.append([])
        for cell in row:
            new_board[-1].append(0)
    for row in range(len(board)):
        for cell in range(len(board[row])):
            neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if row + i >= 0 and row + i < len(board) and \
                            cell + j >= 0 and cell + j < len(board[row]):
                        if board[row + i][cell + j] == 1:
                            neighbors += 1
            if board[row][cell] == 1 and neighbors < 2:
                new_board[row][cell] = 0
            elif board[row][cell] == 1 and neighbors > 3:
                new_board[row][cell] = 0
            elif board[row][cell] == 0 and neighbors == 3:
                new_board[row][cell] = 1
            else:
                new_board[row][cell] = board[row][cell]
    return new_board


if __name__ == "__main__":
    # random board of containing 0s and 1s of size 50x50
    import random
    board = [[random.randint(0, 1) for i in range(50)] for j in range(50)]

    # Visualise and run the game using Pygame
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Game of Life")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        for row in range(len(board)):
            for cell in range(len(board[row])):
                if board[row][cell] == 1:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (cell * 10, row * 10, 10, 10))
        board = game_of_life(board)
        pygame.display.flip()
    pygame.quit()
    quit()
