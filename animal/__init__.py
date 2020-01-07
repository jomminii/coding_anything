# animal package가 어떤 모듈의 합인지

from .cat import Cat  # . <- "이 폴더에 있는 " cat.py라는 파일에서 Cat 이라는 클래스를 갖고 와줘
# from .cat import * 이렇게 하면 cat 모듈에 있는 모든 코드를 불러옴
from .dog import Dog

