class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Usage
dog = Dog()
print(dog.speak())  # Output: Woof!