# Contributing Code, The Smart Way

This project uses Python as it's main programming language. However, Python is notorious for being a pain in the ass to understand as an outside due to the the fact that it does not have static typing.

This small article will give you a brief overview of how to contribute code the smart way, and make it easier for others to understand.

## The PEP8 Standard

We'll be abiding to the standards set out by [PEP8](https://www.python.org/dev/peps/pep-0008/). You don't have to read through the entire document to understand PEP8. Just take away these key points:

- Use 4 spaces for indentations. You can easily do this by setting your IDE's or text editor's tab to be 4 spaces.
    - This is optional for continuation lines, but it is recommended that you still abide by it.

```python
# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

```python
# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

- Limit lines to 79 characters in length.

```python
# Correct
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

```python
# Incorrect
with open('/path/to/some/file/you/want/to/read') as file_1, open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

- Imports should have their own separate lines.

```python
# Correct:
import os
import sys
from subprocess import Popen, PIPE
```

```python
# Wrong:
import sys, os
```

- The same applies to importing classes from other files.

```python
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

## Strings

Strings in Python use either double quotes, `"`, or single quotes, `'`. The PEP8 document does not have a recommendation for which to use in which case.

What we'll be doing is using double quotes in regards to strings, and single quotes in regards to chars:

```python
my_string = "Hello World"
my_char = 'Q'
```

If you need to display data into a string, use an F-string instead of concatenating.

```python
# Correct
your_name = "Bob"
your_age = 21
print(f"Your name is {your_name}. You are {your_age} year(s) old.")
```

```python
# Incorrect
print(f"Your name is " + your_name +". You are " + your_age + " year(s) old.")
```

## Functions
*This isn't specified in PEP8, but I'm adding it here now.*

While Python isn't a statically typed language, you can still add typing to functions.

To make our code easily readable to anyone, use typing:

```python
# Correct. You can easily tell that the expected input is a string and the output will be a list.
def string_list(my_string: str) -> list:
    return my_string.split()
```

```python
# Incorrect. An untrained eye has no idea what this function's expected input or output is.
def string_list(my_string):
    return my_string.split()
```

Use comments for complex functions:

```python
def change_rank(name: str, rank: str) -> NULL:
    """
    Changes specified Player's rank (name) to the target rank in both Discord
    and the Google Sheet.
    Returns void.
    """
    pass
```

## Naming Your Variables and Duck Typing

*"If it looks like a duck, and acts like a duck, then it's a duck."*

This is Python's philosophy. Therefore, we should we strive to follow it.

Name your variables smartly to better distinguish their type.

```python
# Don't do:
var = "QWERTY"
var2 = 24
var3 = [1, 2, "Rabbit"]
```

```python
# DO:
a_string = "QWERTY"
a_num = 24
a_list = [1, 2, "Rabbit"]
```

I know you already know this. Don't let me down.