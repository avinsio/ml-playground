# Strings

## What is a String?

A **string** is a sequence of characters used to store text in Python. A string can contain letters, numbers, symbols, or spaces.

You can create a string using single quotes (`' '`), double quotes (`" "`), or triple quotes (`""" """`) for multi-line text.

```python
message = 'Hello'
message = "Hello"

message = """Hello
World"""
```

---

## Length of a String

Use the `len()` function to find the total number of characters in a string.

```python
message = "Hello World"

len(message)
```

Output

```text
11
```

---

## Accessing Characters (Indexing)

Every character in a string has a position called an **index**.

Python starts counting from **0**.

```python
message = "Hello"

message[0]   # H
message[1]   # e
message[-1]  # o (last character)
```

---

## Extracting Part of a String (Slicing)

Slicing allows you to get a portion of a string.

Syntax:

```python
string[start:stop]
```

- `start` is included.
- `stop` is excluded.

```python
message = "Hello World"

message[0:5]
message[:5]
message[6:]
```

Output

```text
Hello
Hello
World
```

---

# Common String Methods

## Convert to Lowercase

```python
message.lower()
```

Converts all characters to lowercase.

---

## Convert to Uppercase

```python
message.upper()
```

Converts all characters to uppercase.

---

## Count

```python
message.count("l")
```

Counts how many times a character or substring appears.

---

## Find

```python
message.find("World")
```

Returns the index of the first occurrence.

If the value isn't found, it returns `-1`.

```python
message.find("Python")
```

---

## Replace

```python
message.replace("World", "Universe")
```

Returns a new string with the specified text replaced.

---

# Joining Strings (Concatenation)

You can combine multiple strings using the `+` operator.

```python
greeting = "Hello"
name = "Michael"

message = greeting + " " + name
```

---

# String Formatting

### Using `format()`

```python
"{}, {}".format(greeting, name)
```

### Using f-Strings (Recommended)

```python
f"{greeting}, {name}"
```

f-strings are easier to read and are the preferred way to format strings in modern Python.

---

# Useful Built-in Functions

### `dir()`

Shows all available methods and attributes of an object.

```python
dir(str)
```

### `help()`

Displays the documentation for an object or method.

```python
help(str)

help(str.lower)
```

---

# Function vs Method

### Function

A function works independently and receives an object as an argument.

```python
len(message)
```

### Method

A method belongs to an object and is called using dot (`.`) notation.

```python
message.upper()
message.lower()
```

---

# Things to Remember

- A string is used to store text.
- Strings are **immutable**, which means you cannot modify them directly.
- Indexing starts from **0**.
- Negative indexing starts from the end (`-1` is the last character).
- In slicing, the ending index is **not included**.
- Most string methods return a **new string** instead of changing the original one.
- Use **f-strings** for cleaner and more readable string formatting.