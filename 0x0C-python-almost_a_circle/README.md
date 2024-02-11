# 0x0C. Python - Almost a Circle

## Overview
"0x0C. Python - Almost a Circle" is a Python module that encompasses essential concepts of object-oriented programming (OOP), data serialization, and file management through the lens of geometric shapes - specifically, rectangles and squares. This project serves as a practical approach to understanding inheritance, encapsulation, polymorphism, and more, by allowing users to create, manipulate, and store geometric shapes in various formats.

## Features
- **Base Class Management:** A foundational class that handles the unique identification of geometric objects, ensuring a streamlined process for managing and extending object properties.
- **Geometric Shapes Modeling:** Through the `Rectangle` and `Square` classes, users can define and manipulate shapes' dimensions, positions, and unique identifiers, showcasing inheritance and method overriding.
- **Attribute Validation:** Incorporates robust input validation to ensure that geometric objects are instantiated with valid attributes, promoting data integrity and error handling.
- **Serialization and Deserialization:** Utilizes JSON and CSV formats for serializing objects into strings for file storage and reconstructing objects from these strings, illustrating practical applications of serialization in data persistence and transfer.
- **Graphical Representation:** Features a method to draw objects using the Turtle graphics library, providing a visual representation of shapes and demonstrating the utility of Python modules in creating graphics.

## Getting Started
This project is part of the ALX Software Engineering programme's Python curriculum. To get started:
1. Clone the "alx-higher_level_programming" repository:
   ```
   git clone https://github.com/Y4SS11N3/alx-higher_level_programming.git
   ```
2. Navigate to the "0x0C-python-almost_a_circle" directory:
   ```
   cd alx-higher_level_programming/0x0C-python-almost_a_circle
   ```

## Testing
Unit tests for this project are defined in the `tests/` directory. To run all tests, execute the following command from the project's root directory:
```
python3 -m unittest discover tests
```

## Commands Quick Reference
- **Create a Rectangle:** `Rectangle(width, height, x=0, y=0, id=None)`
- **Create a Square:** `Square(size, x=0, y=0, id=None)`
- **Serialize to JSON:** `Base.to_json_string(list_dictionaries)`
- **Save to File (JSON):** `Base.save_to_file(list_objs)`
- **Load from File (JSON):** `Base.load_from_file()`
- **Draw Shapes:** `Base.draw(list_rectangles, list_squares)`

Explore the `models/` directory to understand the implementation details of the `Base`, `Rectangle`, and `Square` classes. The `tests/` directory contains unit tests that provide examples of how to use the classes and methods.

## Examples

### Creating Instances

Creating a new Rectangle:

```
from models.rectangle import Rectangle

rect = Rectangle(10, 7, 2, 8)
```

Creating a new Square:

```
from models.square import Square

sq = Square(5)
```

### Serialization to JSON

```
from models.rectangle import Rectangle

rect = Rectangle(10, 7, 2, 8)
rect_json_string = rect.to_json_string([rect.to_dictionary()])
```

### Save to File

```
Rectangle.save_to_file([rect])
```

### Draw Shapes

To draw shapes using the Turtle graphics module:

```
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10)]
list_squares = [Square(35), Square(15, 70, 50)]

Base.draw(list_rectangles, list_squares)
```

## Authors
Yassine Mtejjal
