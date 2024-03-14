from typing import Any, List, Tuple

import pytest

from pyleetcode_utils import exceptions
from pyleetcode_utils.datatypes import tree


@tree.make_tree
def decorated_sample_function(arg1: Any, tree_data: List[int], arg3: Any) -> Tuple[Any, tree.TreeNode, Any]:
    return arg1, tree_data, arg3  # type: ignore[return-value]


def test_make_tree() -> None:
    tree_list = [1, 2, 3, 4, 5, 6, 7]

    arg1, test_tree, arg3 = decorated_sample_function('arg1', tree_list, 'arg3')

    assert isinstance(test_tree, tree.TreeNode)
    assert test_tree.val == 1
    assert test_tree.left.val == 2  # type: ignore[union-attr]
    assert test_tree.right.val == 3  # type: ignore[union-attr]
    assert test_tree.left.left.val == 4  # type: ignore[union-attr]


def test_make_tree_with_invalid_list() -> None:
    tree_list = [1, 2]

    with pytest.raises(exceptions.NotBinaryTreeError):
        decorated_sample_function('arg1', tree_list, 'arg3')
