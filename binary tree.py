from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # a) Insert (Handle insertion of duplicate entry by ignoring duplicates)
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        else:
            # Duplicate key found, ignoring insertion
            print(f"Duplicate key {key} not inserted.")
        return root

    # b) Delete
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # Node with two children: get inorder successor (smallest in right subtree)
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # c) Search
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    # d) Display tree (Inorder traversal)
    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, root, res):
        if root:
            self._inorder(root.left, res)
            res.append(root.key)
            self._inorder(root.right, res)

    # e) Display - Depth of tree
    def depth(self):
        return self._depth(self.root)

    def _depth(self, root):
        if root is None:
            return 0
        left_depth = self._depth(root.left)
        right_depth = self._depth(root.right)
        return max(left_depth, right_depth) + 1

    # f) Display - Mirror image (create mirror of the tree)
    def mirror(self):
        self._mirror(self.root)

    def _mirror(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self._mirror(root.left)
            self._mirror(root.right)

    # g) Create a copy of the tree
    def copy(self):
        new_tree = BST()
        new_tree.root = self._copy(self.root)
        return new_tree

    def _copy(self, root):
        if root is None:
            return None
        new_node = Node(root.key)
        new_node.left = self._copy(root.left)
        new_node.right = self._copy(root.right)
        return new_node

    # h) Display all parent nodes with their child nodes
    def display_parents_with_children(self):
        res = []
        self._display_parents(self.root, res)
        return res

    def _display_parents(self, root, res):
        if root:
            children = []
            if root.left:
                children.append(root.left.key)
            if root.right:
                children.append(root.right.key)
            if children:
                res.append((root.key, children))
            self._display_parents(root.left, res)
            self._display_parents(root.right, res)

    # i) Display leaf nodes
    def display_leaf_nodes(self):
        leaves = []
        self._display_leaves(self.root, leaves)
        return leaves

    def _display_leaves(self, root, leaves):
        if root:
            if root.left is None and root.right is None:
                leaves.append(root.key)
            self._display_leaves(root.left, leaves)
            self._display_leaves(root.right, leaves)

    # j) Display tree level-wise (Breadth First Traversal)
    def level_order(self):
        res = []
        if not self.root:
            return res

        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.key)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(current_level)
        return res


# Example Usage:
if __name__ == "__main__":
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)
    bst.insert(70)  # Duplicate example

    print("Inorder traversal:", bst.inorder())
    print("Depth of tree:", bst.depth())
    print("Search 40:", bst.search(40))
    print("Search 100:", bst.search(100))

    print("Level order traversal:", bst.level_order())

    print("Parents with children:", bst.display_parents_with_children())
    print("Leaf nodes:", bst.display_leaf_nodes())

    # Create a copy and display its inorder traversal
    copy_bst = bst.copy()
    print("Copied tree inorder traversal:", copy_bst.inorder())

    # Mirror the tree and display inorder traversal
    bst.mirror()
    print("Inorder traversal of mirrored tree:", bst.inorder())

    # Delete a node and display inorder traversal
    bst.delete(70)
    print("Inorder traversal after deleting 70:", bst.inorder())
