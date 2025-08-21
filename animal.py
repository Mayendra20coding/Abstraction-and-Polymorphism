from abc import ABC, abstractmethod 
class animal(ABC):
    def move(self):
     pass
class Human(animal):
    def move(self):
        print('I can walk and run.')
class Snake(animal):
    def move(self):
        print('I can crawl.')
class dog(animal):
    def move(self):
        print('I can bark.')
class Lion(animal):
    def move(self):
        print('I can roar.')
R=Human()
R.move()
k=Snake()
k.move()
R=dog()
R.move()
k=Lion()
k.move()