#!/usr/bin/python3
"""
Base model class


"""

import json
import csv
import turtle


class Base:
    """Represent a base model

    base for all classes in 0x0C* project

    Attributes:
        __nb_objects (int): instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes new Base.

        Args:
            id (int): identity of new Base.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethods
    def to_json_string(list_dictionaries):
        """converts a list of dictionaries to JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            JSON serialization of a list of dictionaries
        """

    if list_dictionaries is None or list_dictionaries == []:
        return "[]"
    return json.dumps(list_of_dictionaries)


    @classmethod
    def save_to_file(cls, list_of_objects):
        """Saves the JSON serialization of a list of objects to a file.

        Args:
            lists_obj(list) - list of inherited Base inheritance
        """

    filename = cls.__name__ + ".json"

    with open(filename, "w") as jsonfile:
        if not list_of_objects:
            jsonfile.write("[]")
        else:
            list_dicts = [o.to_dictionary() for o in list_of_objects]
            jsonfile.write(Base.to_json_string(list_dicts))



    @staticmethod
    def from_json_string(json_str):
        """Deserialize a JSON string.

        Args:
            json_str (str): A JSON string representing a list of dictionaries.
        Returns:
            If json_str is None or empty - an empty list.
            Otherwise - the Python list represented by json_str.
        """
        if not json_str or json_str == "[]":
            return []
        return json.loads(json_str)

    
    @classmethod
    def create(cls, **dictionary):
        """Create an instance of the class with attributes from a dictionary.
            
        Args:
            **attributes (dict): Key/value pairs of attributes for initialization.
        """

        if not dictionary or dictionary == {}:
            return None

        if dictionary:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a file containing JSON strings.
        Reads from `<cls.__name__>.json`.

        Returns:
            If the file doesn't exist or there's an issue - an empty list.
            Otherwise - a list of instantiated instances.
        """

        try:
            with open(cls.__name__ + ".json", "r") as file:
                list = cls.from_json_string(file.read())
                return [cls.create(**dic) for dic in list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.

        Args:
            list_objects (list): list of inherited Base instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `cls.__name__`.csv`.

        Returns:
            If the file does not exist - an empty list
            Otherwise - a list of instantiated classes.
        """

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="")as csvfile:
                if cls.__name__ == "Rectangle":
                    #depends on classname,deff fieleldnames
                    #for reading data from csv file
                   fieldnames = ["id", "width", "height", "x", "y"]
               else:
                   fieldnames = ["id", "size", "x", "y"]
                
                #read data fromcsv file
                list = csv.DictReader(file, fieldnames=fieldnames)

                #convert read dict into list dict
                list = [dict({k, int(v)} for k, v in d.items())
                        for d in list]
                return [cls.create(**d) for d in list]
            except FileNotFoundError:
                return []

        @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        t = turtle.Turtle()
        t.screen.bgcolor("#b7312c")
        t.pensize(2)
        t.shape("turtle")
        t.speed(0)

        t.color("#ffffff")
        #draw rectangle
        for rect in list_rectangles:
            t.showturtle()
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.color("#b5e3d8")
        #draw square
        for square in list_squares:
            t.showturtle()
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for i in range(4):
                .forward(square.width)
                t.left(90)
            t.hideturtle()

        turtle.exitonclick()
