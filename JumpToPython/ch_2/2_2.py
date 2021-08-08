###
### 02_2 문자열 자료형
###

# 문자열(string) 이란 문자, 단어 등으로 구성된 문자들의 집합을 말함

# 파이썬에서 문자열을 만드는 방법 4가지 
#  "Hello World"
#  'Python is fun'
#  """Life is too short, You need python"""
#  '''Life is tod short, You need python'''

##
## 문자열 안에 작은따옴표나 큰따옴표를 포함시키기고 싶을때

# 1. 문자열에 작은따옴표(') 포함 시키기
# Python's favorite food is perl
# 위와 같은 문자열을 food 변수에 저장하고 싶다고 가정하자. 문자열 중 Python's에 작은 따옴표(')가 포함되어 있다.
# 이럴 때는 다음과 같이 문자열을 큰따옴표(")로 둘러싸야 한다. 큰따옴표 안에 들어 있는 작은 따옴표는 
# 문자열을 나타내기 위한 기호로 인식되지 않는다.
food = "Python's favorite food is perl"
print(food)

# 2. 문자열에 큰따옴표(") 포함 시키기
# "Python is very easy." he says.
say = '"Python is very easy." he says.'
print(say)

# 3. 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
food = "Python\'s favorite food is perl"
say = "\"Python is very easy.\" he says."

