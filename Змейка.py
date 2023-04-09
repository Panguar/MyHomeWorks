

from random import seed, randint


menu_move = """8. Вверх
2. Вниз
6. Вправо
4. Влево"""

seed(10)

print("Введите размер поля:")
table_widht = table_height = int(input())
table = list()
for _ in range(table_height):
    row = ["." for _ in range(table_widht)]
    table.append(row)


snake = []

snake_start_head_y = table_height // 2
snake_start_head_x = table_widht // 2

snake_new_part = [snake_start_head_y, snake_start_head_x]
snake.append(snake_new_part)



apple_y = randint(0, table_height - 1)
apple_x = randint(0, table_widht - 1)

table[apple_y][apple_x] = "+"



table_copy = [row.copy() for row in table]

for snake_part in snake:
    snake_part_y = snake_part[0]
    snake_part_x = snake_part[1]
    table_copy[snake_part_y][snake_part_x] = "*"

for row in table_copy:
    print(*row)




print(menu_move)
snake_move_num = int(input())
while snake_move_num != 0:

    snake_head = snake[0]

    snake_head_y = snake_head[0]
    snake_head_x = snake_head[1]



    if snake_move_num == 8:
        snake_head_y -= 1
    elif snake_move_num == 2:
        snake_head_y += 1
    elif snake_move_num == 4:
        snake_head_x -= 1
    elif snake_move_num == 6:
        snake_head_x += 1

    new_head = [snake_head_y, snake_head_x]
    snake.insert(0, new_head)

    if table[snake_head_y][snake_head_x] != "+":
        snake.pop()
    else:
        table[apple_y][apple_x] = "."
        apple_y = randint(0, table_height - 1)
        apple_x = randint(0, table_widht - 1)
        table[apple_y][apple_x] = "+"


    table_copy = [row.copy() for row in table]

    for snake_part in snake:
        snake_part_y = snake_part[0]
        snake_part_x = snake_part[1]
        table_copy[snake_part_y][snake_part_x] = "*"

    for row in table_copy:
        print(*row)

    print(menu_move)
    snake_move_num = int(input())