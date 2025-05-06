class UpperAttrMetaclass(type):
    """A metaclass that converts all class attributes to uppercase."""

    def __new__(cls, name, bases, attrs):
        uppercase_attrs = {}
        for name, value in attrs.items():
            if not name.startswith("__"):
                uppercase_attrs[name.upper()] = value
            else:
                uppercase_attrs[name] = value

        return super().__new__(cls, name, bases, uppercase_attrs)


class MyClass(metaclass=UpperAttrMetaclass):
    """A class that uses the UpperAttrMetaclass."""

    attribute_one = "hello"
    attribute_two = 123


# Example usage
obj = MyClass()
print(obj.ATTRIBUTE_ONE)  # Output: hello
print(obj.ATTRIBUTE_TWO)  # Output: 123

print(
    MyClass.__dict__
)  # print the dictionary of the class to show the attributes are now uppercase.
