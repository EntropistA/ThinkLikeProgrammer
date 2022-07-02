from collections import deque

# Size is 3x3
from random import shuffle

BLANK_TILE = 0

SOLUTION = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, BLANK_TILE),
)


def index_exists(game_state: tuple, tile_index: tuple) -> bool:
    x, y = tile_index
    if 0 <= x < len(game_state) and 0 <= y < len(game_state[0]):
        return True
    return False


def find_tile_index(game_state: tuple, number: int) -> tuple:
    number_index = None
    for zero_row, row in enumerate(game_state):
        for zero_col, n in enumerate(row):
            if n == number:
                number_index = (zero_row, zero_col)

    if number_index is None:
        raise ValueError

    return number_index


def adjacent_numbers(game_state: tuple) -> list:
    blank_tile_index = find_tile_index(game_state, BLANK_TILE)
    numbers = []

    x, y = blank_tile_index

    if index_exists(game_state, (x - 1, y)):
        numbers.append(game_state[x - 1][y])

    if index_exists(game_state, (x + 1, y)):
        numbers.append(game_state[x + 1][y])

    if index_exists(game_state, (x, y - 1)):
        numbers.append(game_state[x][y - 1])

    if index_exists(game_state, (x, y + 1)):
        numbers.append(game_state[x][y + 1])

    return numbers


def perform_move(game_state: tuple, number: int) -> tuple:
    result = [list(row) for row in game_state]

    x, y = find_tile_index(game_state, 0)
    result[x][y] = number

    x, y = find_tile_index(game_state, number)
    result[x][y] = 0

    return tuple(tuple(row) for row in result)


def find_smallest_number_of_moves(start_game_state):
    checked_game_states = set()
    possible_solutions = deque()

    possible_solutions.append(
        (start_game_state, [])
    )

    while possible_solutions:
        game_state, moves = possible_solutions.popleft()
        if game_state in checked_game_states:
            continue
        if game_state == SOLUTION:
            return moves
        checked_game_states.add(game_state)

        for move in adjacent_numbers(game_state):
            new_game_state = perform_move(game_state, move)
            new_moves = moves + [move]

            possible_solutions.append(
                (new_game_state, new_moves)
            )


def generate_random_game_state():
    numbers = list(range(9))
    shuffle(numbers)
    game_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 0
    for x in range(len(game_state)):
        for y in range(len(game_state[x])):
            game_state[x][y] = numbers[i]
            i += 1
    return tuple(tuple(row) for row in game_state)


if __name__ == "__main__":
    for _ in range(5):
        random_game_state = generate_random_game_state()
        print("Game state:")
        for row in random_game_state:
            print(row)
        result = find_smallest_number_of_moves(random_game_state)
        if result:
            print(f"Solution: {result}")
        else:
            print("Not solvable.")
