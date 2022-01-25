# Markdown: Quick and Dirty
Author: Darren Bentler

Date: May 23, 2021

## What is Markdown?

Markdown is a simple text formatting language. You can use it to easily create tables, add headers, display bare code with syntax highlighting, etc.

It can be used for a multitude of things. I've personally used it to help me write articles on my [personal website](https://github.com/dbentler/personalwebsite/tree/main/markdown). Other notable users of Markdown syntax would be in Discord and Reddit.

This guide will help you understand the very basics of Markdown so you can start using it.

## Headers

Headers are used to divide up a Markdown section. They follow a similar formatting style to HTML headers: `<h1>, <h2>, <h3>`. Unlike HTML headers though, they can expressed by `#`'s.

Here's a table of headers:

| Header Syntax   | 
|-----------------|
| # Heading 1     |
| ## Heading 2    | 
| ### Heading 3   |
| #### Heading 4  |
| ##### Heading 5 |
| ###### Heading 6 |

## Text Formatting

Text formatting is pretty straight forward:

| Formatting Character | What it Does | Rendered Example  | Syntax |
|----------------------|--------------|-------------------|---------|
| *                    | Italicize text | *Woah, so fancy*| `*Woah, so fancy*`|
| **                   | Bold Text    | **Woah, so bold** | `**Woah, so bold**`|
| ~~                   | Strikethrough Text | ~~REDACTED~~| `~~Redacted~~` |
| >                    | Block Quotes | > "Hello world"   | `> "Hello World"` |

You can also combine formatting characters:

> *This text is italicized, **but this part is also bold***.

> This module is very ~~**IMPORTANT**~~ deprecated.

## Lists
The syntax for a bullet point list is:

```markdown
- Item 1
- Item 2
- Item 3
```

- Item 1
- Item 2
- Item 3

You can use indents to create nested lists:

```markdown
- Item 1
    - Item 1A
    - Item 1B
- Item 2
```

- Item 1
    - Item 1A
    - Item 1B
- Item 2

You can also do ordered lists, and nest unordered lists, or vice versa:

```markdown
1. Item 1
    - Item 1A
    - Item 1B
2. Item 2
```

1. Item 1
    - Item 1A
    - Item 1B
2. Item 2

## Tables

Tables follow the syntax:

```markdown

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 1   |
| Data 2   | Data 2   |

```
Rendered:

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 1   |
| Data 2   | Data 2   |

*It should be noted that the table dividers,* `|`*, do not need to match up perfectly.*

## Code Formating

You can use backticks, for small snippets of code, or to point out an item of interest:

> The main driving code of our bot can be found in `main.py`.

> You can define a string representation of a class in Python by defining a `__repr__` function.

You can also add in Code Blocks by enclosing your code with 3 backticks. You can also define the syntax highlighting for the language.

```cpp
// C++
include <iostream>

int main(){
    std::cout << "Hello World" << std::endl;
    return 0;
}
```

```python
# Python
if __name__ == "__main__":
    print("Hello World")
```

```diff
+ L115A3 Rework Project
+ L115A3 Rework Project JSRS Compatibility
+ RKSL Studios- Attachments v3.02
+ ACE Compat - RKSL Studios- Attachments
- All USP mods.
```

## Hyperlinks

Links follow the following syntax:

> `[Silver Squadron's Forums](http://77smu.us/)`

Which, when rendered, will simply display as:

>  [Silver Squadron's Forums](http://77smu.us/).

Instead of URLs, you can also link to other pages in this wiki by entering in the file directory from the root folder:

> `[This link will bring you back to this page](/docs/markdown/basic_markdown.md)`

> [This link will bring you back to this page](/docs/markdown/basic_markdown.md)

## Embeded Images

Embeded images follow the same syntax as links, but with an exclamation mark in front of them.

Here's an example of me embedding an image of a rabbit:

> `![a rabbit](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Oryctolagus_cuniculus_Rcdo.jpg/1200px-Oryctolagus_cuniculus_Rcdo.jpg)`.

Rendered image:

![a rabbit](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Oryctolagus_cuniculus_Rcdo.jpg/1200px-Oryctolagus_cuniculus_Rcdo.jpg)

You can also link to images uploaded in the directory by entering in the file directory from the root folder.

## Further Reading

I highly recommend checking out the [Markdown's Guide](https://www.markdownguide.org/basic-syntax/) article on basic markdown syntax to learn best practices.
