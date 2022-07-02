class Name:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError("Value must not be empty")


class Automobile:
    manufacturer_name = Name("manufacturer_name")
    model_name = Name("model_name")

    def __init__(self, manufacturer_name: str, model_name: str, model_year: int):
        self.model_year = model_year
        self.model_name = model_name
        self.manufacturer_name = manufacturer_name

    @property
    def description(self):
        return f"{self.model_year} {self.manufacturer_name} {self.model_name}"


print(Automobile("Chevrolet", "Impala", 1957).description)


class MyString:
    __slots__ = ("value",)

    def __init__(self, value: str):
        self.value = value

    def append(self, character: str):
        self.value += character

    def concatenate(self, other: str):
        self.value += other

    def character_at(self, index):
        return self.value[index]

    def remove(self, start, count):
        if count < 0 or len(self.value[start:]) < count:
            raise ValueError("Invalid number of characters to remove")
        self.value = self.value[:start] + self.value[start + count:]

    def __getitem__(self, item):
        return self.character_at(item)

    def __setitem__(self, key, value):
        self.value = self.value[:key] + value + self[key + 1:]

    def __str__(self):
        return self.value


my_string = MyString("I")
my_string.append(" ")
my_string.concatenate("like pancakes")

print(my_string.character_at(10))
print(my_string[10])
print(my_string)

my_string.remove(0, 5)
print(my_string)
