from heapq import heapify
from random import randint

SMALL = 100
LARGE = SMALL * 10
RANGE = (1, 100_000,)

random_list_small = [randint(*RANGE) for _ in range(SMALL)]
random_list_large = [randint(*RANGE) for _ in range(LARGE)]

small_sum = sum(random_list_small)
large_sum = sum(random_list_large)

print("small: ", small_sum)
print("large: ", large_sum)


# Tail Recursion

def recursive_tail_sum(list_, sum_=0):
    if not list_:
        return sum_
    return recursive_tail_sum(list_[1:], sum_ + list_[0])


def recursive_like_tail_sum(list_):
    sum_ = 0
    while list_:
        sum_, list_ = sum_ + list_[0], list_[1:]
    return sum_


assert recursive_tail_sum(random_list_small) == small_sum
try:
    assert recursive_tail_sum(random_list_large) == large_sum
except RecursionError:
    print("Trying optimized recursive-like solution")
    assert recursive_like_tail_sum(random_list_large) == large_sum


# Head Recursion

def recursive_head_sum(list_):
    if not list_:
        return 0
    return list_[0] + recursive_head_sum(list_[1:])


assert recursive_head_sum(random_list_small) == small_sum

try:
    assert recursive_head_sum(random_list_large)
except RecursionError:
    print("Too big input")

random_target = randint(*RANGE)


# Head Recursion
def count_in_list(list_, target):
    if not list_:
        return 0
    return int(list_[0] == target) + count_in_list(list_[1:], target)


assert count_in_list(random_list_small, random_target) == random_list_small.count(random_target)


class BinaryTree:
    __slots__ = ("right", "value", "left")

    def __init__(self, left, value: int, right):
        self.left = left
        self.value = value
        self.right = right

    def __str__(self):
        result = ""
        if self.left:
            result += str(self.left)
        result += f" {self.value} "
        if self.right:
            result += str(self.right)
        return result


def create_binary_tree_recursive(list_):
    if not list_:
        return None
    value, list_ = list_[0], list_[1:]
    middle_index = len(list_) // 2
    root = BinaryTree(
        create_binary_tree_recursive(list_[:middle_index]),
        value,
        create_binary_tree_recursive(list_[middle_index:])
    )
    return root


def count_nodes(binary_tree: BinaryTree):
    if not binary_tree:
        return 0
    return count_nodes(binary_tree.left) + 1 + count_nodes(binary_tree.right)


assert count_nodes(create_binary_tree_recursive(random_list_small)) == len(random_list_small)


def max_value(binary_tree: BinaryTree):
    max_ = binary_tree.value
    if binary_tree.left:
        max_left = max_value(binary_tree.left)
        if max_left > max_:
            max_ = max_left
    elif binary_tree.right:
        max_right = max_value(binary_tree.right)
        if max_right > max_:
            max_ = max_right
    return max_


def is_heap(binary_tree: BinaryTree):
    if binary_tree.left is None and binary_tree.right is None:
        return binary_tree.value
    if binary_tree.left is None:
        return binary_tree.value > binary_tree.right
    if binary_tree.right is None:
        return binary_tree.value > binary_tree.left
    return binary_tree.value > max_value(binary_tree.left) and binary_tree.value > max_value(binary_tree.right)


print(create_binary_tree_recursive(random_list_small))
