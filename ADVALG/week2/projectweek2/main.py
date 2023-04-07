from AVLTree import AVLTree




def main():
    tree = AVLTree()
    root = None
    while True:
        num = int(input("Enter a positive integer (or a non-positive integer to exit): "))
        if num <= 0:
            break
        if tree.search(root, num):
            tree.delete_node(root, num)
            print(f"{num} deleted from the tree:")
        else:
            root = tree.insert_node(root, num)
            print(f"{num} inserted into the tree:")

        tree.printHelper(root, "", True)
        print("\n")

main()