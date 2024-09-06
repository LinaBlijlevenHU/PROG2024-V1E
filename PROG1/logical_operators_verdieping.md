# Logical Operators and Truth Tables

Logical operators are fundamental in programming, mathematics and the field of logic, 
used to evaluate expressions based on given truth values (True or False). The most common logical operators are **AND**, **OR**, and **NOT**.

These truth tables can be used to specify the outcome of logical expressions, which can 
be helpful when we are writing longer statements and mixing operators.

- [AND](#1-and-operator--or-and)
- [OR](#2-or-operator--or-or)
- [NOT](#3-not-operator--or-not)

### 1. **AND Operator (`&&` or `AND`)**

In Python the 'AND' operator is just `and`. In other languages, we often use `&&`.

The AND operator returns `True` only if **both** operands are true. Otherwise, it returns `False`.

| A     | B     | A AND B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

### 2. **OR Operator (`||` or `OR`)**

In Python the 'AND' operator is just `or`. In other languages, we often use `||`.

The OR operator returns `True` if **at least one** operand is true. It only returns `False` when both are false.

| A     | B     | A OR B |
|-------|-------|--------|
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

### 3. **NOT Operator (`!` or `NOT`)**

In Python the 'AND' operator is `not`. In other languages, we often use `!`, the exclamation mark. 
Interestingly, we do use this for the `!=` non-equality operator.

The NOT operator inverts the truth value of its operand. If the value is `True`, it becomes `False`, and vice versa.

| A     | NOT A |
|-------|-------|
| True  | False |
| False | True  |

### Combining Operators

Logical operators can be combined to form more complex expressions. For example:

- `(A AND B) OR (NOT A)` is evaluated by first computing `A AND B`, followed by the result of `NOT A`, and finally applying the OR operation.

Truth tables are a great tool to visualize the result of logical expressions, simplifying the process of reasoning in programming and Boolean algebra.
