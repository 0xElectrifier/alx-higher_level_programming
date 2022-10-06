#!/usr/bin/python3
"""First Project"""
import json
import csv
import turtle


class Base:
    """Base class of all other classes in this project. It manages
    ``id`` attribute in all other classes, to avoid duplicating the
    same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Object

        Args:
            id (int): id of objects
        """
        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of @list_dictionaries

        Args:
            list_dictionaries (list): containing dictionaries to be converted
        """

        ld = list_dictionaries

        if ((list_dictionaries is []) or (list_dictionaries is None)):
            return ("[]")
        return (json.dumps(ld))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation

        Args:
            json_string (json): string representing a list of dictionaries
        """
        if json_string is None:
            return ([])

        return (json.loads(json_string))

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Uses the turtle module to draw the Object

        Args:
            list_rectangles (list): list of `Rectangle` instances
            lsit_squares (list): list of `Square` instances
        """
        wn = turtle.Screen()
        tobj = turtle.Turtle()

        wn.bgcolor("light green")
        tobj.color("blue")
        tobj.penup()
        tobj.backward(200)
        tobj.left(90)
        tobj.forward(200)
        tobj.pendown()

        for rect, square in list_rectangle, list_square:
            width = getattr(rect, "width")
            height = getattr(rect, "height")
            if (square):
                width = getattr(square, "width")
                height = getattr(square, "height")

            for i in range(4):
                tobj.forward(width)
                tobj.right(90)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes to a JSON file the json representation
        of list_objs

        Args:
            list_objs (obj): list of instances who inherits of ``Base`` class
        """
        filename = cls.__name__ + ".json"
        j_list = []

        if (list_objs is None):
            pass
        else:
            for obj in list_objs:
                b_dict = obj.to_dictionary()
                j_list.append(b_dict)

        j_str = Base.to_json_string(j_list)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(j_str)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            dictionary (dictionary): list of key/word arguments to be
            implemented into the instance
        """
        if (cls.__name__ == "Rectangle"):
            new_obj = cls(1, 1)
        else:
            new_obj = cls(1)
        new_obj.update(**dictionary)

        return (new_obj)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as f:
                j_list = cls.from_json_string(f.read())
        except FileNotFoundError:
            j_list = []
        rects = []
        for rect in j_list:
            rects.append(cls.create(**rect))
        return (rects)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes @list_objs into `csv` file"""

        filename = cls.__name__ + ".csv"
        if (cls.__name__ == "Rectangle"):
            field = ["id", "width", "height", "x", "y"]
        else:
            field = ["id", "size", "x", "y"]

        rows = []
        for obj in list_objs:
            row = []
            for attr in field:
                row.append(getattr(obj, attr))
            rows.append(row)

        with open(filename, "w", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(field)
            csv_writer.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        """Reads from `csv` file"""
        filename = cls.__name__ + ".csv"
        with open(filename, encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile)
            field = next(csv_reader)
            rows = []
            for row in csv_reader:
                rows.append(row)

        obj_list = []
        for row in rows:
            obj_dict = dict()
            for i in range(len(field)):
                obj_dict[field[i]] = int(row[i])

            new = cls.create(**obj_dict)
            obj_list.append(new)

        return (obj_list)
