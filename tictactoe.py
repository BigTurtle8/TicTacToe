import random as r
from functions import list_to_str


class Game:
    def __init__(self):
        self.first = False
        if r.random() >= 0.5:
            self.first = True

        self.map = [['_' for _ in range(3)] for _ in range(3)]

    def wrong(self):
        print("That is not the correct input. Please input a coord - ex: A1")

    def display(self):
        for row, areas in enumerate(self.map):
            row -= 2
            row *= -1
            row += 1
            print(str(row) + list_to_str(areas))
        print(' ABC')

    def input_action(self):
        real_action = [0, 1]
        action = input("Where would you like to play?").lower()
        if len(action) == 2:
            true_action = [char for char in action]
            if true_action[0] in 'abc' and true_action[1] in '123':
                if true_action[0] == 'a':
                    real_action[1] = 0
                elif true_action[0] == 'b':
                    real_action[1] = 1
                else:
                    real_action[1] = 2

                if true_action[1] == '1':
                    real_action[0] = 2
                elif true_action[1] == '2':
                    real_action[0] = 1
                else:
                    real_action[0] = 0

                if self.map[real_action[0]][real_action[1]] != '_':
                    print("That area is already filled.")
                    return True
                else:
                    self.map[real_action[0]][real_action[1]] = 'X'
                    return False

            else:
                self.wrong()
                return True
        else:
            self.wrong()
            return True

    def enemy_action(self):
        possible_locations = []
        for row, areas in enumerate(self.map):
            for column, area in enumerate(areas):
                if area == '_':
                    possible_locations.append((row, column))
        chosen = r.choice(possible_locations)
        self.map[chosen[0]][chosen[1]] = 'O'

        chosen_print = []
        if chosen[1] == 0:
            chosen_print.append('A')
        elif chosen[1] == 1:
            chosen_print.append('B')
        else:
            chosen_print.append('C')

        if chosen[0] == 0:
            chosen_print.append('1')
        elif chosen[0] == 1:
            chosen_print.append('2')
        else:
            chosen_print.append('3')

        print(f"AI chose {list_to_str(chosen_print)}")

    def check_win(self):
        col_info = [[], [], []]
        for row in self.map:
            counter1 = 0
            counter2 = 0
            for area in row:
                if area == 'X':
                    counter1 += 1
                elif area == 'O':
                    counter2 += 1

            if counter1 == 3:
                return 1
            elif counter2 == 3:
                return 2

            col_info[0].append(row[0])
            col_info[1].append(row[1])
            col_info[2].append(row[2])

        for col in col_info:
            counter1 = 0
            counter2 = 0
            for area in col:
                if area == 'X':
                    counter1 += 1
                elif area == 'O':
                    counter2 += 1

            if counter1 == 3:
                return 1
            elif counter2 == 3:
                return 2

        diag1 = [self.map[0][0], self.map[1][1], self.map[2][2]]
        diag2 = [self.map[0][2], self.map[1][1], self.map[2][0]]
        counter1 = 0
        counter2 = 0
        for area in diag1:
            if area == 'X':
                counter1 += 1
            elif area == 'O':
                counter2 += 1

            if counter1 == 3:
                return 1
            elif counter2 == 3:
                return 2

        counter1 = 0
        counter2 = 0
        for area in diag2:
            if area == 'X':
                counter1 += 1
            elif area == 'O':
                counter2 += 1

            if counter1 == 3:
                return 1
            elif counter2 == 3:
                return 2

        return 0

    def play(self):
        first = True
        if not self.first:
            self.enemy_action()
            self.display()
        while True:
            if first and self.first:
                self.display()
                first = False
            inputting = True
            while inputting:
                inputting = self.input_action()
            self.display()
            if (check := self.check_win()) == 1:
                print('Player 1 Wins!')
                break
            elif check == 2:
                print('Player 2 Wins!')
                break
            self.enemy_action()
            self.display()
            if (check := self.check_win()) == 1:
                print('Player 1 Wins!')
                break
            elif check == 2:
                print('Player 2 Wins!')
                break


g = Game()


g.play()
