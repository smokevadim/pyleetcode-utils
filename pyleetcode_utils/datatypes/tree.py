from __future__ import annotations

import functools
from typing import Optional, TypeVar, Callable, Any, List, Tuple, Generator
from collections import deque
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

    def __repr__(self):
        queue = deque()
        queue.append(self)
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur.val)
            if not cur.val:
                continue
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return str(res)


def make_tree(func: Func) -> Func:
    """Decorator to convert List[int] to TreeNode."""

    def _make_tree(source_list: List[int], cur: int = 0) -> TreeNode:
        if cur >= len(source_list):
            raise exceptions.NotBinaryTreeError('Not valid binary tree has been provided!')
        current_value = source_list[cur]
        if (cur * 2) + 2 > len(source_list):
            return TreeNode(current_value) if current_value else None
        left = 1 if cur == 0 else cur * 2 + 1
        right = 2 if cur == 0 else cur * 2 + 2
        return TreeNode(
            current_value,
            _make_tree(source_list, left),
            _make_tree(source_list, right),
        )

    def prepare_new_args(args: Tuple[Any, ...], **kwargs: Any) -> Generator[TreeNode | Any, Any, None]:
        return (_make_tree(arg) if isinstance(arg, list) else arg for arg in args)

    def check_recursion(*args, **kwargs):
        """Check if args or kwargs already contains TreeNode."""

        return any((isinstance(arg, TreeNode) for arg in args)) \
            or any(isinstance(arg, TreeNode) for arg in kwargs.values()) \
            or (len(args) > 1 and not args[1])

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if check_recursion(*args, **kwargs):
            return func(*args, **kwargs)
        try:
            new_args = prepare_new_args(args, **kwargs)
        except Exception as e:
            raise exceptions.NotBinaryTreeError('Not valid binary tree has been provided!')
        return func(*new_args, **kwargs)

    return wrapper  # type: ignore[return-value]
