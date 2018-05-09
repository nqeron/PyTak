import string
import math
import TakMove

alphabet = string.ascii_lowercase


def m_dist(xOne, yOne, xTwo, yTwo):
    return int(math.fabs(xOne - xTwo) + math.fabs(yOne - yTwo))


def get_row_num(pos):
    return int(pos[1]) - 1 #zero base


def get_col_num(pos):
    return alphabet.index(pos[0])


def mirror_y(move_list, size):
    out = []
    for move in move_list:
        col = size - get_col_num(move)
        slide = ""
        if TakMove.Slide.is_slide(move):
            slide = TakMove.Slide.get_slide_val(move)
            if slide == TakMove.Slide.UP:
                slide = TakMove.Slide.DOWN
            elif slide == TakMove.Slide.DOWN:
                slide = TakMove.Slide.UP
        rest = ""
        if len(move) > 3:
            rest = move[3:]
        out_move = move[0] + str(col + 1) + str(slide) + rest
        out.append(out_move)
    return out


def mirror_x(move_list, size):
    out = []
    for move in move_list:
        row = size - get_row_num(move)
        row = string.ascii_lowercase[row]
        slide = ""
        if TakMove.Slide.is_slide(move):
            slide = TakMove.Slide.get_slide_val(move)
            if slide == TakMove.Slide.LEFT:
                slide = TakMove.Slide.RIGHT
            elif slide == TakMove.Slide.RIGHT:
                slide = TakMove.Slide.LEFT
        rest = ""
        if len(move) > 3:
            rest = move[3:]
        out_move = row + move[1] + str(slide) + rest
        out.append(out_move)
    return out


def mirror_diag(move_list, size):
    out = []
    for move in move_list:
        row = get_col_num(move)
        col = get_row_num(move)
        row = string.ascii_lowercase[row]
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
        if len(move) > 3:
            rest = move[3:]
        out_move = row + str(col + 1) + str(slide) + rest
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
