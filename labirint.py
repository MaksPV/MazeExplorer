import random, sys

# Конфигурация клавиш
buttons = ("2", "6", "8", "4")

# Карта
map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 1, 5, 0, 3, 0, 0, 2, 1],
             [1, 3, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 3, 0, 1],
             [1, 0, 1, 2, 1, 1, 0, 1, 0, 1],
             [1, 2, 1, 1, 1, 1, 0, 1, 2, 1],
             [1, 0, 1, 0, 0, 3, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 2, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Позиция игрока
pos = [8, 1]

# Здоровье игрока
hp = 3

# Баннер
banner = "\n"*50 + '''
 __  __                                                          
|  \/  |    o O O  __ _      o O O    ___     o O O   ___        
| |\/| |   o      / _` |    o        |_ /    o       / -_)       
|_|__|_|  TS__[O] \__,_|   TS__[O]  _/__|   TS__[O]  \___|       
_|"""""| {======|_|"""""| {======|_|"""""| {======|_|"""""|      
"`-0-0-'./o--000'"`-0-0-'./o--000'"`-0-0-'./o--000'"`-0-0-'      
   ___             _ __     _                                    
  | __|   __ __   | '_ \   | |     ___      _ _    ___      _ _  
  | _|    \ \ /   | .__/   | |    / _ \    | '_|  / -_)    | '_| 
  |___|   /_\_\   |_|__   _|_|_   \___/   _|_|_   \___|   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 

'''

# Функция, которая рисует миникарту
def draw_mini_map():
    global pos, map
    mini_map = ""
    if map[pos[0] - 1][pos[1]] == 1:
        mini_map += " ■ \n"
    else:
        mini_map += "   \n"
    
    if map[pos[0]][pos[1] - 1] == 1:
        mini_map += "■Я"
    else:
        mini_map += " Я"
    if map[pos[0]][pos[1] + 1] == 1:
        mini_map += "■\n"
    else:
        mini_map += " \n"
    
    if map[pos[0] + 1][pos[1]] == 1:
        mini_map += " ■ \n"
    else:
        mini_map += "   \n"
    
    print(mini_map)

# Сражение с монстром
def monster():
    global hp, pos, map
    print(banner)
    print("Вы встретили монстра, решите его задачи, чтобы победить его\n")
    input("Нажмите ENTER чтобы продолжть")
    monster_hp = 3
    while True:
        print(banner)
        print(f"Ваше здоровье {hp}")
        print(f"Здоровье монстра {monster_hp}")
        print()
        print("Монстр загадал")
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        znak = random.choice(["+", "-", "*"])
        print(str(a), znak, str(b))
        try:
            ansewer = int(input())
        except ValueError:
            ansewer = 0
        if znak == "+":
            if ansewer == a + b:
                monster_hp -= 1
                print("Верно, монстру нанесён удар")
            else:
                hp -= 1
                print("Вы решили неправильно, монстр нанёс вам урон")
        elif znak == "-":
            if ansewer == a - b:
                monster_hp -= 1
                print("Верно, монстру нанесён удар")
            else:
                hp -= 1
                print("Вы решили неправильно, монстр нанёс вам урон")
        if znak == "*":
            if ansewer == a * b:
                monster_hp -= 1
                print("Верно, монстру нанесён удар")
            else:
                hp -= 1
                print("Вы решили неправильно, монстр нанёс вам урон")
         
        if monster_hp == 0:
            print("Вы победили монстра!")
            map[pos[0]][pos[1]] = 0
            break
        elif hp == 0:
            print("Вы умерли в данной схватке :(")
            sys.exit()
        else:
            input("ENTER чтобы продолжить")

# Сражение с магом
def question():
    global hp
    print(banner)
    print("Вы должны ответить на загадку мага\n")
    questions = ["Не лает, не кусает, в дом не пускает, кто это?", "Речка спятила с ума — По домам пошла сама.", "На раскрашенных страницах\nМного праздников хранится.", "Ах, не трогайте меня:\nОбожгу и без огня!", "Стоит дуб,\nВ нем двенадцать гнезд,\nВ каждом гнезде\nПо четыре яйца,\nВ каждом яйце\nПо семи цыпленков.", "Ёжик странный у Егорки\nНа окне сидит в ведерке.\nДень и ночь он дремлет,\nСпрятав ножки в землю."]
    ansewers = ["замок", "водопровод", "календарь", "крапива", "год", "кактус"]
    quest = random.randint(0, len(questions) - 1)
    
    print(questions[quest])
    if input().lower() == ansewers[quest]:
        print(banner)
        print("Вы победили мага")
    else:
        print(banner)
        print("Маг нанёс вам урон")
        hp -= 1
        input("\nНажмтье ENTER для продолжения")
    map[pos[0]][pos[1]] = 0

# Начальный экран
print(banner)
print("Вам предстоит пройти лабиринт, в нём вас ждут маги и монстры, которые будут мешать вашему прохождению.\nСоветую взять листок в клетку, чтобы записать лабиринт.")
input("\nНажмите ENTER для начала")
# Основной цикл программы
while True:
    print(banner)
    
    draw_mini_map()
    
    print(f"Ваше здоровье: {hp}\n")
    
    print("Вы можете пойти:")
    if map[pos[0] - 1][pos[1]] != 1:
        print(f"{buttons[0]} - Вверх")
    if map[pos[0] + 1][pos[1]] != 1:
        print(f"{buttons[2]} - Вниз")
    if map[pos[0]][pos[1] - 1] != 1:
        print(f"{buttons[3]} - Влево")
    if map[pos[0]][pos[1] + 1] != 1:
        print(f"{buttons[1]} - Вправо")
    
    menu = input("\n").lower()
    
    if menu == buttons[0] and map[pos[0] - 1][pos[1]] != 1:
        pos[0] -= 1
    elif menu == buttons[2] and map[pos[0] + 1][pos[1]] != 1:
        pos[0] += 1
    elif menu == buttons[3] and map[pos[0]][pos[1] - 1] != 1:
        pos[1] -= 1
    elif menu == buttons[1] and map[pos[0]][pos[1] + 1] != 1:
        pos[1] += 1
    
    if map[pos[0]][pos[1]] == 2:
        monster()
    elif map[pos[0]][pos[1]] == 3:
        question()
    elif map[pos[0]][pos[1]] == 5:
        print(banner)
        print("Вы нашли выход, поздравляем!")
        sys.exit()
