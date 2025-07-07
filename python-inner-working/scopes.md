# Closures and Scoping in Python

## Introduction

Scoping defines where variables are accessible in your code, controlling their visibility and lifetime. Closures allow a function to "remember" variables from its enclosing scope, even after that scope has finished executing. This note explains these concepts using first principles, with examples to illustrate how they work in Python.

## Scoping: The LEGB Rule

Python uses the **LEGB rule** to resolve variable names:

- **Local**: Inside the current function or block.
- **Enclosing**: In any enclosing function (for nested functions).
- **Global**: At the module level.
- **Built-in**: Python’s predefined names (e.g., `print`, `len`).

Python searches these scopes in order, stopping at the first match.

### Example: LEGB in Action

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # Prints: local

    inner()
    print(x)  # Prints: enclosing

outer()
print(x)  # Prints: global
```

**Explanation**:

- Each function has its own namespace.
- `inner()` finds `x` in its local scope.
- `outer()` finds `x` in its local (enclosing) scope.
- The module finds `x` in the global scope.

## Closures: Remembering Enclosing Scope

A closure is a nested function that captures variables from its enclosing scope and retains access to them after the outer function finishes. This is useful for preserving state without global variables.

### How Closures Work

- Functions are first-class objects in Python.
- A nested function can access variables from its enclosing function.
- Closures extend the lifetime of these variables via the function’s `__closure__` attribute.

### Example: Creating a Closure

```python
def outer(x):
    def inner():
        print(x)  # Accesses x from enclosing scope
    return inner

f1 = outer(5)
f2 = outer(10)
f1()  # Prints: 5
f2()  # Prints: 10
```

**Explanation**:

- `outer(5)` creates a closure where `inner` remembers `x = 5`.
- `f1` and `f2` are separate closures with their own `x` values.
- Inspect the closure: `f1.__closure__[0].cell_contents` returns `5`.

## Modifying Enclosing Variables: The `nonlocal` Keyword

Assigning to a variable in a nested function creates a new local variable unless you use `nonlocal` to refer to the enclosing scope.

### Example: Without `nonlocal` (Error)

```python
def outer():
    x = 10
    def inner():
        x = x + 1  # Error: local variable 'x' referenced before assignment
        print(x)
    inner()

outer()
```

### Example: With `nonlocal`

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        print(x)
    inner()
    print(x)

outer()  # Prints: 11, 11
```

**Explanation**:

- `nonlocal x` binds `inner` to `outer`’s `x`, allowing modification.
- Without `nonlocal`, `x = x + 1` creates a new local `x`, causing an error.

## Practical Use of Closures

Closures are useful for:

- **State preservation**: Maintain state without global variables.
- **Function factories**: Create specialized functions dynamically.
- **Data hiding**: Encapsulate variables within the closure.

### Example: Function Factory

```python
def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

times_two = make_multiplier(2)
times_three = make_multiplier(3)
print(times_two(5))   # Prints: 10
print(times_three(5)) # Prints: 15
```

**Explanation**:

- Each `make_multiplier` call creates a closure with a unique `factor`.
- The returned function (`multiply`) remembers its `factor`.

## Pitfall: Late Binding Closures

Closures capture variables by reference, which can cause issues in loops.

### Example: Incorrect Behavior

```python
functions = []
for i in range(3):
    def func():
        print(i)
    functions.append(func)

for f in functions:
    f()  # Prints: 2, 2, 2
```

**Explanation**:

- `func` captures `i` by reference.
- When called, `func` uses the final value of `i` (`2`) after the loop ends.

### Fix: Use a Factory Function

```python
def make_func(i):
    def func():
        print(i)
    return func

functions = []
for i in range(3):
    functions.append(make_func(i))

for f in functions:
    f()  # Prints: 0, 1, 2
```

**Explanation**:

- `make_func(i)` creates a new closure for each `i`, capturing its value at the time of creation.

## Key Takeaways

- **LEGB Rule**: Python resolves variable names by searching Local, Enclosing, Global, and Built-in scopes.
- **Closures**: Nested functions that capture enclosing variables, stored in `__closure__`.
- **Nonlocal**: Use to modify enclosing scope variables.
- **Closures Enable Encapsulation**: Create stateful, reusable functions.
- **Late Binding**: Capture loop variables carefully using a factory function.

## Test Your Understanding

```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c1 = counter()
c2 = counter()
print(c1())  # Prints: 1
print(c1())  # Prints: 2
print(c2())  # Prints: 1
```

**Explanation**:

- Each `counter()` call creates a new closure with its own `count`.
- `c1` and `c2` maintain separate states.
