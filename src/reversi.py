import typing as t

directions = (
    (-1,-1),(-1, 0),(-1, 1),
    ( 0,-1),        ( 0, 1),
    ( 1,-1),( 1, 0),( 1, 1),
)

def get_color(board, coord: tuple):
    """
    >>> board = [ \
        ['W', 'W', '.', 'W'],\
        ['B', 'B', 'B', '.'],\
        ['.', '.', 'B', 'W'],\
        ['.', '.', 'W', '.'],\
    ]
    >>> get_color(board, (0, 0))
    'W'
    >>> get_color(board, (1, 0))
    'B'
    >>> get_color(board, (3, 3))
    '.'
    """
    row, col = coord
    return board[row][col]


def is_within_bounds(coord: tuple, board_dimension: int) -> bool:
    """
    >>> is_within_bounds((0, 0), 4)
    True
    >>> is_within_bounds((-1, 0), 4)
    False
    >>> is_within_bounds((1, -1), 4)
    False
    >>> is_within_bounds((4, 1), 4)
    False
    """
    row, col = coord
    if row < 0:
        return False
    if col < 0:
        return False
    if row >= board_dimension:
        return False
    if col >= board_dimension:
        return False
    return True


def get_score_in_direction(board: list[list], my_color: str,
                           coord: tuple, direction: tuple,
                           score: int = 0) -> int:
    """
    >>> board = [ \
        ['W', 'W', '.', 'W'],\
        ['B', 'B', 'B', '.'],\
        ['.', '.', 'B', 'W'],\
        ['.', '.', 'W', '.'],\
    ]
    >>> get_score_in_direction(board, 'W', (2, 1), (1, 1))
    0
    >>> get_score_in_direction(board, 'W', (2, 0), (-1, 0))
    1
    >>> get_score_in_direction(board, 'W', (0, 2), (1, 0))
    2
    """
    row, col = coord
    row_increment, col_increment = direction
    new_coord = (row + row_increment, col + col_increment)
    if not is_within_bounds(coord=new_coord, board_dimension=len(board)):
        return 0
    neighbour_color = get_color(board=board, coord=new_coord)
    if neighbour_color == '.':
        return 0
    if neighbour_color is my_color:
        return score
    score = get_score_in_direction(board, my_color, new_coord, direction, score+1)

    return score

def get_score_at_square(board: list[list], my_color: str,
                        coord: tuple) -> int:
    """
    >>> board = [ \
        ['W', 'W', '.', 'W'],\
        ['B', 'B', 'B', '.'],\
        ['.', '.', 'B', 'W'],\
        ['.', '.', 'W', '.'],\
    ]
    >>> get_score_at_square(board, 'W', (2, 0))
    1
    >>> get_score_at_square(board, 'W', (0, 2))
    2
    >>> get_score_at_square(board, 'W', (2, 1))
    3
    >>> get_score_at_square(board, 'B', (2, 1))
    0
    """
    score = 0
    for direction in directions:
        score += get_score_in_direction(board=board, my_color=my_color, 
                                        coord=coord, direction=direction,
                                        score=0)
    return score

def pick_best_move(board: list[list], my_color: str) -> tuple[int, t.Optional[tuple]]:
    """
    >>> board = [ \
        ['W', 'W', '.', 'W'],\
        ['B', 'B', 'B', '.'],\
        ['.', '.', 'B', 'W'],\
        ['.', '.', 'W', '.'],\
    ]
    >>> pick_best_move(board, 'W')
    (3, (2, 1))
    >>> pick_best_move(board, 'B')
    (0, None)
    >>> board = [ \
        ['.', '.', '.', 'W'],\
        ['.', 'W', 'B', '.'],\
        ['.', 'B', 'W', '.'],\
        ['.', '.', '.', '.'],\
    ]
    >>> pick_best_move(board, 'B')
    (1, (0, 1))
    >>> pick_best_move(board, 'W')
    (2, (3, 0))
    """
    best_score, best_move = 0, None
    board_dimension = len(board)
    for row in range(0, board_dimension):
        for col in range(0, board_dimension):
            if get_color(board=board, coord=(row, col)) != '.':
                continue
            score = get_score_at_square(board, my_color, (row, col))
            if score > best_score:
                best_score = score
                best_move = (row, col)
    return best_score, best_move

def flip_pieces(board: list[list], my_color: str,
                           coord: tuple, vector: tuple) -> list[list]:
    """
    >>> board = [ \
        ['W', 'W', '.', 'W'],\
        ['B', 'B', 'B', '.'],\
        ['W', '.', 'B', 'W'],\
        ['.', '.', 'W', 'B'],\
    ]
    >>> flip_pieces(board, 'W', (2, 1), (-1, 0))
    [\
['W', 'W', '.', 'W'], \
['B', 'W', 'B', '.'], \
['W', 'W', 'B', 'W'], \
['.', '.', 'W', 'B']]
    >>> flip_pieces(board, 'W', (2, 1), (-1, 1))
    [\
['W', 'W', '.', 'W'], \
['B', 'W', 'W', '.'], \
['W', 'W', 'B', 'W'], \
['.', '.', 'W', 'B']]
    >>> flip_pieces(board, 'W', (2, 1), (0, 1))
    [\
['W', 'W', '.', 'W'], \
['B', 'W', 'W', '.'], \
['W', 'W', 'W', 'W'], \
['.', '.', 'W', 'B']]
    >>> board = [ \
        ['W', 'W', '.', 'W'],\
        ['B', 'B', 'B', '.'],\
        ['W', '.', 'B', 'W'],\
        ['.', '.', 'W', 'B'],\
    ]
    >>> flip_pieces(board, 'B', (3, 0), (-1, 0))
    [\
['W', 'W', '.', 'W'], \
['B', 'B', 'B', '.'], \
['B', '.', 'B', 'W'], \
['B', '.', 'W', 'B']]
    >>> board = [ \
        ['W', 'W', '.', 'W'],\
        ['B', 'B', 'B', '.'],\
        ['W', '.', 'B', 'W'],\
        ['.', '.', 'W', 'B'],\
    ]
    >>> flip_pieces(board, 'B', (3, 1), (0, 1))
    [\
['W', 'W', '.', 'W'], \
['B', 'B', 'B', '.'], \
['W', '.', 'B', 'W'], \
['.', 'B', 'B', 'B']]
    """
    row, col = coord
    row_increment, col_increment = vector
    board[row][col] = my_color
    while True:
        row = row + row_increment
        col = col + col_increment
        if get_color(board, (row, col)) is my_color:
            break
        board[row][col] = my_color
    return board

def make_move(board: list[list], my_color: str,
                           coord: tuple) -> list[list]:
    """
    >>> board = [ \
        ['W', 'W', '.', 'W'],\
        ['B', 'B', 'B', '.'],\
        ['W', '.', 'B', 'W'],\
        ['.', '.', 'W', '.'],\
    ]
    >>> make_move(board, 'B', (3, 0))
    [\
['W', 'W', '.', 'W'], \
['B', 'B', 'B', '.'], \
['B', '.', 'B', 'W'], \
['B', '.', 'W', '.']]
    >>> board = [ \
        ['W', 'W', '.', 'W'],\
        ['B', 'B', 'B', '.'],\
        ['.', '.', 'B', 'W'],\
        ['.', '.', 'W', '.'],\
    ]
    >>> make_move(board, 'W', (2, 1))
    [\
['W', 'W', '.', 'W'], \
['B', 'W', 'W', '.'], \
['.', 'W', 'W', 'W'], \
['.', '.', 'W', '.']]
    """
    row, col = coord

    for direction in directions:
        score = get_score_in_direction(board=board, my_color=my_color,
                                       coord=coord, direction=direction,
                                       score=0)
        if  score > 0:
            board = flip_pieces(board=board, my_color=my_color,
                                coord=coord, vector=direction)
    board[row][col] = my_color
    return board

def play(board: list[list]):
    colors = ['W', 'B']
    scores = [0, 0]
    pointer = 0
    while True:
        color = colors[pointer]
        score, best_move = pick_best_move(board=board,
                                          my_color=color)
        if not best_move:
            break
        scores[pointer] += score
        board = make_move(board=board, my_color=color,
                          coord=best_move)
        print ("="*40)
        print (f"{color} makes move and gets {score} scores, {color}:{scores[pointer]}")
        for row in board:
            print("".join(row))
        pointer = 1 if pointer == 0 else 0
    winner = scores.index(max(scores))
    print(f"{colors[winner]} is a winner")

if __name__ == '__main__':
    board = [ \
        ['.', '.', '.', '.', '.', '.'],\
        ['.', '.', '.', '.', '.', '.'],\
        ['.', '.', 'B', 'W', '.', '.'],\
        ['.', '.', 'W', 'B', '.', '.'],\
        ['.', '.', '.', '.', '.', '.'],\
        ['.', '.', '.', '.', '.', '.'],\
    ]
    for row in board:
        print("".join(row))
    play(board=board)