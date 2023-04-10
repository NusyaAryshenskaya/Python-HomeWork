#class Human:
#    name: str
 #   age: int
  #  weight: float
   # height: float

#    def __init__ (self, name: str, age: int, weight: float = 100, height: float = 170 ):
 #       self.name  = name
  #      self.age = age
   #     self.weight = weight
    #    self.height = height
    
   # def hello(self):
    #    return f"Тебя приветствует {self.name}"

#kirill = Human ("Женя", 38, height=210)
#print(kirill.hello())

class Contact:

    def __init__ (self, name: str, phone: str, comment: str = ""):
        self.name  = name
        self.phone = phone
        self.comment = comment

    def edit(self, new_contact: name: str, phone: str, comment: str ):
        self.name  = name if name else self.name
        self.phone = phone
        self.comment = comment
    # доделать
    def cnt_to_str(self):
        # 54 мин


    def __str__(self):
        return  f"{self.name} {self.phone} {self.comment}"
    
class PhoneBook:
    def __init__ (self, path: str):
        self.path  = path
        self.phone_book: list[Contact] = []
        self.original_book = list[Contact] = []

    def open_file(self);
 # 45 минута и тд

    def save_file(self):
    #54 мин

    def get(self):
        return self.phone_book
    
    def add(self, new_contact: Contact) -> None:

