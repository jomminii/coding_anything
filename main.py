from animal import dog  # animal 패키지에서 dog라는 모듈을 갖고 와줘
from animal import cat

from animal import *


d = dog.Dog()  # instance
d.hi()

c = cat.Cat()
c.hi()

# animal 패키지가 갖고 있는 모듈을 다 불러와

# 이렇게 하면
d = Dog()
c = Cat()
d.hi()
c.hi()
