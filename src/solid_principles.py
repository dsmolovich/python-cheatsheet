# src: https://realpython.com/solid-principles-python/
import typing as t
from abc import ABC, abstractmethod
from unittest.mock import patch, call

#=======================================
# Single-responsibility principle (SRP)
#===
from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename: str) -> None:
        self.path = Path(filename)

    def read(self, encoding="utf-8") -> str:
        return self.path.read_text(encoding=encoding)
    
    def write(self, data: str, encoding="utf-8"):
        self.path.write_text(data=data, encoding=encoding)

class ZipManager:
    def __init__(self, filename: str) -> None:
        self.path = Path(filename)
    
    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)
    
    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

def test_file_manager():
    expected = "Some file contents"
    writer = FileManager("/tmp/contents.txt")
    writer.write("Some file contents")
    reader = FileManager("/tmp/contents.txt")
    actual = reader.read()
    assert actual == expected

def test_zip_manager():
    filename="/tmp/file_to_compress.txt"
    writer = FileManager(filename=filename)
    writer.write("AAAAAAAAAAAAAAAAAAA")
    zip_writer = ZipManager(filename=filename)
    zip_writer.compress()
    zip_reader = ZipManager(filename=filename)
    zip_reader.decompress()



#=======================================
# Open–closed principle (OCP)
#===
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__(shape_type="circle")
        self.radius = radius
    
    def calculate_area(self) -> float:
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__(shape_type="rectangle")
        self.width = width
        self.height = height
    
    def calculate_area(self) -> float:
        return self.width * self.height

def test_circle():
    circle = Circle(10)
    assert circle.shape_type == "circle"
    assert circle.calculate_area() == 314.1592653589793

def test_rectangle():
    rectangle = Rectangle(10, 10)
    assert rectangle.shape_type == "rectangle"
    assert rectangle.calculate_area() == 100



#=======================================
# Liskov substitution principle (LSP)
#===
def get_total_area(shapes: t.List[Shape]) -> float:
    return sum([shape.calculate_area() for shape in shapes])

def test_get_total_area():
    shapes = [Circle(10), Rectangle(10, 10)]
    assert get_total_area(shapes=shapes) == 414.1592653589793



#=======================================
# Interface segregation principle (ISP)
#===
class Printer(ABC):
    @abstractmethod
    def print(self, document: str) -> None:
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document: str) -> None:
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document: str) -> None:
        pass

class OldPrinter(Printer):
    def print(self, document: str) -> None:
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document: str) -> None:
        print(f"Printing {document} in colors in hi-res...")
    
    def fax(self, document: str) -> None:
        print(f"Faxing {document}...")
    
    def scan(self, document: str) -> None:
        print(f"Scanning {document}...")

@patch('builtins.print')
def test_old_printer(mock_print):
    printer = OldPrinter()
    printer.print("Some Document")
    mock_print.assert_called_with("Printing Some Document in black and white...")

@patch('builtins.print')
def test_new_printer(mock_print):
    printer = NewPrinter()
    printer.print("Some Document")
    printer.fax("Some Document")
    printer.scan("Some Document")
    mock_print.assert_has_calls([
        call("Printing Some Document in colors in hi-res..."),
        call("Faxing Some Document..."),
        call("Scanning Some Document..."),
    ])

#=======================================
# Dependency inversion principle (DIP)
#===
class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class DataBase(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"

class FrontEnd:
    def __init__(self, data_source: DataSource) -> None:
        self.data_source = data_source
    
    def display_data(self):
        print(f"Displaying data: {self.data_source.get_data()}")

@patch('builtins.print')
def test_display_data_from_database(mock_print):
    frontend = FrontEnd(DataBase())
    frontend.display_data()
    mock_print.assert_called_with("Displaying data: Data from the database")

@patch('builtins.print')
def test_display_data_from_api(mock_print):
    frontend = FrontEnd(API())
    frontend.display_data()
    mock_print.assert_called_with("Displaying data: Data from the API")
