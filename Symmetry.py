import string
import math
import TakMove

alphabet = string.ascii_lowercase


def m_dist(xOne, yOne, xTwo, yTwo):
    return int(math.fabs(xOne - xTwo) + math.fabs(yOne - yTwo))


def get_square(pos):
    if pos[0].isalpha() and pos[0] != "C" and pos[0] != "S":
        return pos[:2]
    else:
        return pos[1:3]


def get_row_num(square):
    return int(square[1]) - 1 #zero base


def get_col_num(square):
    return alphabet.index(square[0])


def get_top(pos):
    if pos[0].isalpha() and pos[0] != "C" and pos[0] != "S":
        return ""
    else:
        return pos[0]


def mirror_y(move_list, size):
    out = []
    for move in move_list:
        top = get_top(move)
        square = get_square(move)
        col = get_col_num(square)
        row = size - get_row_num(square)
        col = string.ascii_lowercase[col]
        slide = ""
        if TakMove.Slide.is_slide(move):
            slide = TakMove.Slide.get_slide_val(move)
            if slide == TakMove.Slide.UP:
                slide = TakMove.Slide.DOWN
            elif slide == TakMove.Slide.DOWN:
                slide = TakMove.Slide.UP
        rest = ""
        if len(move) >= 4:
            rest = move[4:]
        out_move = top + col + str(row) + str(slide) + rest
        out.append(out_move)
    return out


def mirror_x(move_list, size):
    out = []
    for move in move_list:
        top = get_top(move)
        square = get_square(move)
        row = get_row_num(square)
        col = size - get_col_num(square) - 1
        col = string.ascii_lowercase[col]
        slide = ""
        if TakMove.Slide.is_slide(move):
            slide = TakMove.Slide.get_slide_val(move)
            if slide == TakMove.Slide.LEFT:
                slide = TakMove.Slide.RIGHT
            elif slide == TakMove.Slide.RIGHT:
                slide = TakMove.Slide.LEFT
        rest = ""
        if len(move) >= 4:
            rest = move[4:]
        out_move = top + col + str(row + 1) + str(slide) + rest
        out.append(out_move)
    return out


def mirror_diag(move_list, size):
    out = []
    for move in move_list:
        top = get_top(move)
        square = get_square(move)
        row = get_col_num(square)
        col = get_row_num(square)
        col = string.ascii_lowercase[col]
        slide = ""
        if TakMove.Slide.is_slide(move):
            slide = TakMove.Slide.get_slide_val(move)
            if slide == TakMove.Slide.UP:
                slide = TakMove.Slide.RIGHT
            elif slide == TakMove.Slide.RIGHT:
                slide = TakMove.Slide.UP
            elif slide == TakMove.Slide.DOWN:
                slide = TakMove.Slide.LEFT
            elif slide == TakMove.Slide.LEFT:
                slide = TakMove.Slide.DOWN
        rest = ""
        if len(move) > 4:
            rest = move[4:]
        out_move = top + col + str(row + 1) + str(slide) + rest
        out.append(out_move)
    return out


def standardize(move_list,size):
    gc = get_col_num
    gr = get_row_num
    mid = int(size / 2)
    size = size - 1
    inner_triangle = mid - 1

    if gr(move_list[0]) > mid:
        move_list = mirror_y(move_list, size)
    if gc(move_list[0]) > mid:
        move_list = mirror_x(move_list, size)

    for off_move in move_list:
        if gc(off_move) != gr(off_move):
            break

    if m_dist(gc(off_move), gr(off_move), size, 0) > size:
        move_list = mirror_diag(move_list, size)

    return move_list
