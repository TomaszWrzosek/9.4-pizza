import json

class pizza:
    def __init__(self):
        try:
            with open("C:\Kodilla\9.4\pizza.json", "r") as f:
                self.pizza = json.load(f)
        except FileNotFoundError:
            self.pizza = []

    def all(self):
        return self.pizza

    def save_all(self):
        with open("pizza.json", "w") as f:
            json.dump(self.pizza, f)

    def get(self, id):
        topping = [topping for topping in self.all() if topping['id'] == id]
        if topping:
             return topping[0]
        return []

    def create(self, data):
        self.pizza.append(data)
        self.save_all()

    def delete(self, id):
        topping = self.get(id)
        if topping:
            self.pizza.remove(topping)
            self.save_all()
            return True
        return False

    def update(self, id, data):
        topping = self.get(id)
        if topping:
            index = self.pizza.index(topping)
            self.pizza[index] = data
            self.save_all()
            return True
        return False


pizza = pizza()