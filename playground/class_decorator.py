def decorator(cls):
    class WrappedClass:
        def __init__(self, *args, **kwargs):
            print(f"Creating instance of {cls.__name__}", *args, **kwargs)
            self._wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self._wrapped, name)

        def __str__(self):
            return f"Wrapped class: {self._wrapped}"

    return WrappedClass

@decorator
class ExampleClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

# Usage
example = ExampleClass(10)
example.display()
print(example)