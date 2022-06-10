from turtle import *
from math import *

turtle = Turtle()
turtle.speed(1000)


def distance(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def fence_len(fence):
    sum = 0
    for i in range(0, len(fence)):
        sum += distance(fence[i][0], fence[i][1], fence[(i + 1) % len(fence)][0], fence[(i + 1) % len(fence)][1])
    return sum


def dots_to_y(x, x1, y1, x2, y2):
    return float(x - x1) * ((float(y2 - y1)) / (float(x2 - x1))) + y1


def dots_to_x(y, x1, y1, x2, y2):
    return float(y - y1) * ((float(x2 - x1)) / (float(y2 - y1))) + x1


def draw_tree(x, y):
    turtle.color('green')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()


def draw_fence(x1, y1, x2, y2):
    turtle.color('brown')
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


def is_good_tree(tree1, tree2, trees):
    greater = less = 0
    for tree in trees:
        if tree == tree1 or tree == tree2:
            continue
        dim = dot = 0
        if tree1[0] == tree2[0]:
            dot = dots_to_x(tree[1], tree1[0], tree1[1], tree2[0], tree2[1])
            dim = 0
        else:
            dot = dots_to_y(tree[0], tree1[0], tree1[1], tree2[0], tree2[1])
            dim = 1
        if tree[dim] > dot:
            greater += 1
        elif tree[dim] < dot:
            less += 1
        if less * greater != 0:
            return False
        if tree[dim] == dot:
            dim2 = abs(dim - 1)
            dot1 = min(tree1[dim2], tree2[dim2])
            dot2 = max(tree1[dim2], tree2[dim2])
            if tree[dim2] >= dot1 and tree[dim2] <= dot2:
                return False

    return True


def link_trees(cur_tree, prev_tree, trees, fence):
    for tree in trees:
        if tree == cur_tree or tree == prev_tree:
            continue
        if is_good_tree(cur_tree, tree, trees):
            fence.append(tree)
            return


print("Деревосоединялка (бета-версия)\nУ вас есть лес или что-то, вокруг чего необхоидмо построить забор минимальной длины? Мы готовы вам помочь!")
trees = list()
trees_cnt = int(input("Так-с, начнем. Введите количество деревьев\n"))
print("Супер! Теперь введите координаты каждого дерева (каждая координата должна быть в отдельной строке)")
for i in range(trees_cnt):
    x = int(input())
    y = int(input())
    trees.append((x, y))
    draw_tree(x, y)

first_tree = tuple()
x_min = 10000000
for tree in trees:
    if tree[0] < x_min:
        x_min = tree[0]
        first_tree = tree
prev_tree = first_tree
cur_tree = first_tree
fence = list()
link_trees(cur_tree, prev_tree, trees, fence)
prev_tree = cur_tree
cur_tree = fence[len(fence) - 1]
draw_fence(cur_tree[0], cur_tree[1], prev_tree[0], prev_tree[1])
while cur_tree != first_tree:
    link_trees(cur_tree, prev_tree, trees, fence)
    prev_tree = cur_tree
    cur_tree = fence[len(fence) - 1]
    draw_fence(cur_tree[0], cur_tree[1], prev_tree[0], prev_tree[1])

print(f"Вот изображение вашего чудного забора!\nЕго длина: {round(fence_len(fence), 2)}")

done()
