class TreeNode:
    def __init__(self,val=0,left=None,right= None):
        self.val=val
        self.left= left
        self.right=right

def check_binary_paths(root):
    def dfs(node,path,paths):
        if not node:
            return
        path += str(node.val)
        if not node.left and not node.right:
            paths.append(path)
        else:
            path += "->"
            dfs(node.left,path,paths)
            dfs(node.right,path,paths)

    result=[]
    dfs(root,"",result)
    return result
        
# Example Usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print(check_binary_paths(root)) 