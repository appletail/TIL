# 전위순회(preorder traversal)
def pre(root):
    if root:    # != 0
        print(root, end=' ')
        pre(tree[root][0])
        pre(tree[root][1])


# 중위순회(inorder traversal)
def inorder(root):
    if tree[root][0] != 0:
        inorder(tree[root][0])
    print(root, end=' ')
    if tree[root][1] != 0:
        inorder(tree[root][1])


# 후휘순회(postorder traversal)
def post(root):
    if tree[root][0] != 0:
        post(tree[root][0])
    if tree[root][1] != 0:
        post(tree[root][1])
    print(root, end=' ')


inputS = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, inputS.split()))
V = 13
tree = [[0, 0] for _ in range(V + 1)]
parent = [0] * (V + 1)

for idx in range(0, len(lst), 2):
    p, c = lst[idx], lst[idx + 1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    parent[c] = p

pre(1)
print()
inorder(1)
print()
post(1)
