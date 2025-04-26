class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def __str__(self, loop=0):
        ret = "  " * loop + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(loop + 1)
        return ret
    


root = TreeNode("Electronics")

laptop = TreeNode("Laptop")
laptop.add_child(TreeNode("Mac"))
laptop.add_child(TreeNode("Surface"))
laptop.add_child(TreeNode("Thinkpad"))

cellphone = TreeNode("Cell Phone")
cellphone.add_child(TreeNode("iPhone"))
cellphone.add_child(TreeNode("Google Pixel"))
cellphone.add_child(TreeNode("Vivo"))

tv = TreeNode("TV")
tv.add_child(TreeNode("Samsung"))
tv.add_child(TreeNode("LG"))

root.add_child(laptop)
root.add_child(cellphone)
root.add_child(tv)

#print(root.__str__())
print(root)