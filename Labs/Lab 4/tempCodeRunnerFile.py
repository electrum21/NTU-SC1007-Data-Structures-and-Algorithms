if root.data > p and root.data > q:  # Both values are smaller than the root
            return self.findLCA(root.left, p, q)  # Move to the left subtree
        elif root.data < p and root.data < q:  # Both values are larger than the root
            return self.findLCA(root.right, p, q)  # Move to the right subtree
        else:  # One value on each side, or root itself is one of the values
            return root.data  # The current node is the LCA