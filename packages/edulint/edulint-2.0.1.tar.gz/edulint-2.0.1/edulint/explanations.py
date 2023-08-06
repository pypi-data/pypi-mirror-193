from typing import Dict


explanations: Dict[str, Dict[str, str]] = {
    "W0612": {
        "why": "Having unused variables in code makes the code unnecessarily complicated.",
        "examples": "A solution is to remove the variable, if possible, or rename it to `_`, which is a common"
        "convention for naming unused variables. A variable named `_` should never be used anywhere later in code."
    },

    "R6201": {
        "why": "Having unnecessary conditions in code makes the code harder to understand.",
        "examples": """
A condition that returns bool in both branches can be simplified even if it contains a logical statement.

```py
def problematic(a: bool, b: bool) -> bool:
    if a or b:
        return True
    else:
        return False
```

```py
def good(a: bool, b: bool) -> bool:
    return a or b
```
"""},

    "R1714": {
        "why": "Shorter conditions are ussually easier to read.",
        "examples": """
Comparison of a variable to two values can be simplified using the `in` operator.
This is more readable and also safer against copy-paste errors.

```py
def problematic(text: str):
    if text == 'a' or text == 'b':
        return
```

```py
def good(text: str):
    if text in ('a', 'b'):
        return
```

If you are comparing a single character, you can also do this:

```py
def good(char: str):
    if char in 'ab':
        return
```
"""
    },

}


def get_explanations() -> Dict[str, Dict[str, str]]:
    return explanations
