
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance




@singleton
class Clase:
    def __init__(self, valor):
        self.some_data = valor
    def some_business_logic(self):
        pass
