# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_AbstractMethod.ipynb (unless otherwise specified).

__all__ = ['AbstractMethod']

# Cell
#hide
from typing import Union, List

import sys
sys.path.append("..")

from .EditOperations import *


# Cell
class AbstractMethod:
    """
    Creates an AbstractMethod from the given `tokens`, which can be either:

    - a string with tokens delimited by `delimiter` (defaults to a single space)
    - a list of tokens
    """

    def __init__(self, tokens: Union[str, List[str]], delimiter = " ") -> None:
        if type(tokens) is str:
            self.__tokens = [] if len(tokens) == 0 else tokens.split(delimiter)
        else:
            self.__tokens = tokens.copy()

    def __eq__(self, other: "AbstractMethod") -> bool:
        return type(other) is AbstractMethod and self.__tokens == other.__tokens

    def __getitem__(self, key: int) -> str:
        return self.__tokens[key]

    def __len__(self) -> int:
        return len(self.__tokens)

    def __str__(self) -> str:
        return repr(" ".join(self.__tokens))

    def __repr__(self) -> str:
        return str(self)

    def applyEditOperation(self, operation: EditOperation):
        """
        Applies the given `operation`.
        """
        operation.applyToTokens(self.__tokens)

    def applyEditOperations(self, operations: List[EditOperation]):
        """
        Applies the given list of `operations` in order.
        """
        for op in operations:
            self.applyEditOperation(op)

    def getEditOperationsTo(self, other: "AbstractMethod") -> List[EditOperation]:
        """
        Returns the minimal list of edit operations which, if applied, would result in the `AbstractMethod`
        given by `other`.
        """

        matrix = self.__getEditOpsMatrix(other)
        editOps = []

        r = len(matrix) - 1
        c = len(matrix[0]) - 1

        while True:
            if matrix[r][c] == 0:
                break
            elif r == 0:
                c -= 1
                editOps.insert(0, InsertOperation(c, other[c]))
            elif c == 0:
                r -= 1
                editOps.insert(0, DeleteOperation(c))
            elif self[r - 1] == other[c - 1]:
                r -= 1
                c -= 1
            elif matrix[r][c] == matrix[r - 1][c - 1] + 1:
                r -= 1
                c -= 1
                editOps.insert(0, ReplaceOperation(c, other[c]))
            elif matrix[r][c] == matrix[r][c - 1] + 1:
                c -= 1
                editOps.insert(0, InsertOperation(c, other[c]))
            elif matrix[r][c] == matrix[r - 1][c] + 1:
                r -= 1
                editOps.insert(0, DeleteOperation(c))
            else:
                raise RuntimeError("AbstractMethod: invalid matrix!")

        return editOps

    def __getEditOpsMatrix(self, other: "AbstractMethod") -> List[List[int]]:

        numRows = len(self) + 1
        numCols = len(other) + 1

        # initialize matrix
        matrix = []
        for r in range(numRows):
            matrix.append([c if r == 0 else 0 for c in range(numCols)])
            matrix[r][0] = r

        # iterate through matrix and assign values
        for r in range(1, numRows):
            for c in range(1, numCols):

                left =    matrix[r    ][c - 1]
                topLeft = matrix[r - 1][c - 1]
                top =     matrix[r - 1][c    ]

                if self[r - 1] == other[c - 1]:
                    matrix[r][c] = topLeft
                else:
                    matrix[r][c] = min(left, topLeft, top) + 1

        return matrix