from pyleetcode_utils import null
from pyleetcode_utils.datatypes import tree


class Solution:
    """
    Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such
    that their sum is equal to k, or false otherwise.
    """

    @tree.make_tree
    def findTarget(self, root: tree.TreeNode, k: int) -> bool:
        history = set()
        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur.val:
                continue
            if (k - cur.val) in history:
                return True
            else:
                history.add(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False


if __name__ == '__main__':
    assert Solution().findTarget([5, 3, 6, 2, 4, null, 7], 9) is True  # type: ignore[arg-type]
