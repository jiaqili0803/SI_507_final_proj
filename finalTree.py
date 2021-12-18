yesBag = ["Yes", 'yes', 'Y', 'y', 'Yup', 'yup', 'Sure', 'sure']

# tree example:
#                  Question1
#                  /       \
#                 Y         N
#                /           \
#             Ques2         Ques2
#            /     \        /    \
#         (Y, Y)  (Y, N)   (N, Y)  (N, N)
# 
# (Q1, (Q2, (Y,Y), (Y,N)), (Q2, (N,Y), (N,N))

# 1. solar_rad: Average solar radiation (W/M^2) 日照
# 2. max_uv: Maximum UV Index (0-11+) 辐射

quesTree = \
    ("Question1: Do you want to know solar radiation?",
        ("Question2: Do you want to know UV Index?",
            ("Yes", "Yes"),
            ("Yes", "No")),
        ("Question2: Do you want to know UV Index??",
            ("No", "Yes"),
            ("No", "No")))

def printTree(tree, level, prefix = '', bend = ''):
    if level == 2:
        print(f'{prefix}{bend}{tree}')

    else: 
        text, left, right = tree
        print(f'{prefix}{bend}{text}')
        if bend == '+-':
            prefix = prefix + '| '
        elif bend == '`-':
            prefix = prefix + '| '
        printTree(left, level+1, prefix, '+-')
        printTree(right, level+1, prefix, '`-')
        

def yes(prompt):
    ans = input(prompt + "  ")
    ans = ans.strip()
    if ans in yesBag:
        return True
    return False

def playLeaf(tree, level):
    if level == 2:
        # output = yes(tree[0])
        return tree

    text, left, right = tree
    ans = yes(text)
    if ans == True:
        output = playLeaf(left, level+1)
    else:
        output = playLeaf(right, level+1)
    
    return output


def main():
    op = playLeaf(quesTree, 0)
    print(op)
    #print(type(op))
    choice1 = op[0]
    choice2 = op[1]
    print(choice1)
    print(type(choice1))
    print('#########################')
    print('######## The Tree #######')
    printTree(quesTree, 0)
    return choice1, choice2

if __name__ == '__main__':
    main()
