# Python Closures and Nested Functions

## Introduction

In Python, a **nested function** is a function defined inside another function. A **closure** is a special type of nested function that allows access to variables from the outer function's scope, even after the outer function has finished executing. This note explains nested functions and closures with clear examples, formatted for easy understanding.

## Nested Functions

A nested function is a function defined within another function (the outer function). The inner function can access variables from the outer function's scope and operates like any other function when called.

### Example: Nested Function

```python
def greet(name):
    # Inner function
    def display_name():
        print("Hi", name)

    # Call inner function
    display_name()

# Call outer function
greet("John")
```

**Output**:

```
Hi John
```

**Explanation**:

- The `display_name()` function is defined inside `greet()`.
- It accesses the `name` parameter of the outer function.
- The inner function executes when called within `greet()`.

## Python Closures

A closure is a nested function that retains access to variables from the outer function's scope, even after the outer function has completed execution. This allows the inner function to "remember" the outer function's variables.

### How Closures Work

- The inner function captures variables from the outer function's scope.
- These variables are preserved in the closure, even after the outer function's scope is destroyed.
- Closures are often created by returning the inner function from the outer function.

### Example: Closure with Lambda

```python
def greet():
    # Variable defined in outer function
    name = "John"

    # Return a nested anonymous function
    return lambda: "Hi " + name

# Call outer function
message = greet()

# Call inner function
print(message())
```

**Output**:

```
Hi John
```

**Explanation**:

- The `greet()` function defines a variable `name` and returns a lambda function that uses `name`.
- When `greet()` is called, it returns the lambda function, which is assigned to `message`.
- Even though `greet()` has finished executing, the lambda function retains access to `name`.
- Calling `message()` executes the lambda, accessing `name` from the closure.

### Why Closures Work MOOOOOOSTTTTT IMPPPPPP

- Python stores the outer function’s variables in the inner function’s `__closure__` attribute.
- This preserves the variable’s value, allowing the inner function to use it later.
- However, Lambda can access these variables because they’re now part of the lambda func (a closure) itself. That’s why you can say that a closure is a function with an extended scope.

## Key Points

- **Nested Functions**: Functions defined inside other functions, with access to the outer function’s variables.
- **Closures**: Nested functions that retain access to outer function variables after the outer function’s execution ends.
- **Use Cases**: Closures are useful for maintaining state, creating function factories, and encapsulating data.

## Summary

Nested functions allow modular code within a function, while closures extend this by preserving outer scope variables. The examples demonstrate how a nested function operates normally and how a closure retains access to variables using a lambda function.
