import os
# чистка терминала
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

# игровое поел
board = [
   ["-", "-", "-"],
   ["-", "-", "-"],
   ["-", "-", "-"]
]
copy_of_board = board.copy()
last_motion = None
next_player = None
number = [1, 2, 3]

# отрисовка поля
def print_board():
    i = 1
    print(" ", "1", "2", "3")
    for row in board:
        print(i, " ".join(row))
        i += 1

# сделать ход на доске
def make_motion(current_player):
    print("Давайте походим)")
    x = int(input("Куда по оси x?: "))
    y = int(input("Куда по иси y?: "))

    if x not in number or y not in number:
        print("Введите корректные значения")
        make_motion(current_player)

    if board[y-1][x-1] != 'x' and board[y-1][x-1] != '0':
        board[y-1][x-1] = current_player
    else:
        print("Эта клетка уже занята, попробуйте еще раз")
        make_motion(current_player)
    next_player = '0' if current_player == 'x' else 'x'
    clear()
    print_board()
    return next_player

# регулировка игры/ ведение игры
def motion_of_game():
    print_board()
    current_player = str(input("Кто первый? X или 0: ")).lower()
    if current_player != 'x' and current_player != '0':
        print("Ошибка ввода, попробуйте сначала")
        motion_of_game()
 
    while(True):
        current_player = make_motion(current_player)
        winner = check_win(board)
        if winner:
            print(f"Победил игрок: {winner.upper()}!")
            break

# проверка победных комбинаций
def check_win(board):
    win_combinations = [
        # Горизонтали
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # Вертикали
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # Диагонали
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
    
    for combo in win_combinations:
        symbols = [board[x][y] for x, y in combo]
        if symbols[0] != "-" and symbols.count(symbols[0]) == 3:
            return symbols[0]  
    
    return None  

# главное меню
def main_func():
    while(True):
        global board
        board = [row.copy() for row in copy_of_board]
        print("1. Новая игра")


        choice = int(input("Что будем делать? (введите цифру): "))
        if choice == 1:
            motion_of_game()


main_func()            