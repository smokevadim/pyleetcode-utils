# pyleetcode-utils

![Latest Version](https://img.shields.io/github/v/tag/smokevadim/pyleetcode-utils?sort=semver)
[![Build Status](https://github.com/smokevadim/pyleetcode-utils/actions/workflows/test.yml/badge.svg?event=push)](https://github.com/smokevadim/pyleetcode-utils/actions/workflows/test.yml/badge.svg?event=push)
[![codecov](https://codecov.io/gh/smokevadim/pyleetcode-utils/branch/master/graph/badge.svg)](https://codecov.io/gh/smokevadim/pyleetcode-utils)
[![Python Version](https://img.shields.io/pypi/pyversions/pyleetcode-utils.svg)](https://pypi.org/project/pyleetcode-utils/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![license](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/smokevadim/pyleetcode-utils/blob/master/LICENSE)

## Features

__Currently, only LeetCode TreeNode implemented.__  
- Converting `[5, 3, 6, 2, 4, null, 7]` -> `TreeNode(5, TreeNode(3,...), TreeNode(6,...))`

## Installation

```bash
pip install pyleetcode-utils
```

## Example

TreeNode usage:

```python
from pyleetcode_utils import null
from pyleetcode_utils.datatypes import tree


class Solution:
  @tree.make_tree
  def findTarget(self, root: tree.TreeNode, k: int) -> bool:
    ...


Solution().findTarget([5, 3, 6, 2, 4, null, 7], 9)
```
