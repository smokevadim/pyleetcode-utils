import functools
from typing import Optional, TypeVar, Callable, Any, List, Tuple

from pyleetcode_utils import exceptions

Func = TypeVar('Func', bound=Callable[..., Any])


class TreeNode(object):
    """Builtin Leetcode class."""

    def __init__(
        self,
        val: int = 0,  # noqa: WPS110
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None,
    ):
        self.val = val  # noqa: WPS110
        self.left = left
        self.right = right


def make_tree(func: Func) -> Func:
    """Decorator to convert List[int] to TreeNode."""

    def _make_tree(source_list: List[int], cur: int = 0) -> TreeNode:
        current_value = source_list[cur]
        if (cur * 2) + 2 > len(source_list):
            return TreeNode(current_value)
        left = 1 if cur == 0 else cur * 2 + 1
        right = 2 if cur == 0 else cur * 2 + 2
        return TreeNode(
            current_value,
            _make_tree(source_list, left),
            _make_tree(source_list, right),
        )

    def prepare_new_args(args: Tuple[Any, ...], **kwargs: Any) -> Tuple[Any, ...]:
        start_args = args[:1]
        end_args = args[2:]
        tree_arg = (_make_tree(args[1]),)
        return start_args + tree_arg + end_args

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            new_args = prepare_new_args(args, **kwargs)
        except Exception:
            raise exceptions.NotBinaryTreeError('Not valid binary tree has been provided!')
        return func(*new_args, **kwargs)

    return wrapper  # type: ignore[return-value]
