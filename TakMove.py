from enum import Enum


class Slide(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @staticmethod
    def get_slide_val(move):
        pos = 2
        if not move[0].isalpha():
            pos = 3
        if len(move) > 2:
            if move[pos] == "+":
                return Slide.UP
            elif move[pos] == "-":
                return Slide.DOWN
            elif move[pos] == ">":
                return Slide.RIGHT
            elif move[pos] == "<":
                return Slide.LEFT


    @staticmethod
    def is_slide(move):
        pos = 2
        if not move[0].isalpha():
            pos = 3
        if len(move) > pos:
            if move[pos] == "+" or move[pos] == "-" or move[pos] == ">" or move[pos] == "<":
                return True
        return False

    def __str__(self):
        if self.value == Slide.UP.value:
            return "+"
        elif self.value == Slide.DOWN.value:
            return "-"
        elif self.value == Slide.RIGHT.value:
            return ">"
        elif self.value == Slide.LEFT.value:
            return "<"


class ParseMoveException(Exception):
    pass


class Node:

    def __init__(self, move, ply):
        self.move = move
        self.ply = ply
        self.children = []
        self.count = 1

    def add_child(self, childNode):
        self.children.append(childNode)

    def add_count(self):
        self.count += 1


def parse_server_move(move): #P a5; M a5 a4 1 --> a5, a5-
    if move == "":
        return ""
    code = move[0]
    if code == "P":
        square = move[2:4]
        noble = ""
        if len(move) > 5:
            noble = move[5]
        out = square
        if noble == "W":
            out = "S"+out
        elif noble == "C":
            out = "C"+out
        return out
    elif code == "M":
        from_square = move[2:4]
        to_square = move[5:7]
        drops = move[8:].split()

        direction = ""
        if from_square[0] < to_square[0]:
            direction = ">"
        elif from_square[0] > to_square[0]:
            direction = "<"
        elif from_square[0] == to_square[0]:
            if from_square[1] < to_square[1]:
                direction = "+"
            elif from_square[1] > to_square[1]:
                direction = "-"
        top = str(sum([int(x) for x in drops]))
        if top == "1":
            top = ""
        if len(drops) == 1:
            drops = ""
        else:
            drops = "".join(drops)
        out = top + from_square + direction + drops
        return out
    else:
        raise ParseMoveException("No such Move code "+code)
