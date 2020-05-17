class AVLNode(object):
    def init(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class AVLTree(object):
    def insert(self, root, val):
        if not root:
            root = AVLNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
            root = self.balance(root)

        elif val > root.val:
            root.right = self.insert(root.right, val)
            root = self.balance(root)
        return root

    def get_heigh(self, root):
        h = 0
        if root:
            hl = self.get_heigh(root.left)
            hr = self.get_heigh(root.right)
            max_heigh = max(hl, hr)
            h = max_heigh + 1
        return h

    def is_balance(self, root):
        return self.get_heigh(root.left) - self.get_heigh(root.right)

    def smal_right_rotation(self, node):
        current = node.right
        node.right = current.left
        current.left = node
        return current

    def smal_left_rotation(self, root):
        current = root.left
        root.left = current.right
        current.right = root
        return current

    def big_right_rotation(self, root):
        current = root.left
        root.left = self.smal_right_rotation(current)
        return self.smal_left_rotation(root)

    def big_left_rotation(self, root):
        current = root.right
        root.right = self.smal_left_rotation(current)
        return self.smal_right_rotation(root)

    def balance(self, root):
        balancefactor = self.is_balance(root)
        if balancefactor > 1:
            if self.is_balance(root.left) > 0:
                root = self.smal_left_rotation(root)
            else:
                root = self.big_right_rotation
        elif balancefactor < -1:
            if self.is_balance(root.right) > 0:
                root = self.big_left_rotation(root)
            else:
                root = self.smal_right_rotation(root)
        return root

    def preorder(self, root):
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def search(self, root, k):
        if not root:
            return None
        if k == root.val:
            return root
        if k < root.val:
            return self.search(root.left, k)
        if k > root.val:
            return self.search(root.right, k)

