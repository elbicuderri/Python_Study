# SoyNet Coding Guide For Python
>
> 작성목적: Python에서의 코딩 가이드를 제시하여 소이넷 내에서 효율적인 작업환경을 구축하기<br>
> 위해 이 문서는 작성되었다. 이 문서가 절대적인 기준은 아니지만 가이드라인을 제시해준다.
><br><br>
> 활용방법: 작성한 Python 코드 위에 이 문서의 버전을 표기한다.
```python
"""
SoyNet Coding Guide For Python version 0.2
"""
```
> 
> 문서변경방법: 소이넷 직원 2명 이상이 합의하여 이 문서의 사항을 변경할 수 있고, 업데이트 내역을 기록하여야<br>
> 하며 이전 버전은 backup해두어야 한다. 그리고 그 버전의 작성자는 수정한 사람들의 이름들로 업데이트한다.<br> 업데이트 내용을 공지하고, 업데이트한 문서를 공유하여야 한다.

<br>

> 작성자: 백승환
>
> 작성일: 2021년 1월 18일
>
> version : 0.2 (demo)

<br>

## Start

0. 코드 맨 위에 이 문서에 없는 기준이라도 자신이 사용한 기준이 존재한다면 전부 적어라.
```python
"""
1. 이 코드에서 모든 변수는 단수로 쓴다.
2. 동사는 모두 현재형으로 쓴다.
...
"""
```

1. 변수와 함수는 소문자이면서 snake 스타일.<br> 변수를 **매우 강조**하고 싶으면 대문자 가능. 함수는 비권장. 숫자로 시작하면 안된다.
```python
first_df = pd.read_csv(first_file_path)

def sn_from_csv(path: str) -> int: 
  ...

VERY_IMPORTANT_VARIABLE = "soynet"

# Wrong
31_ice_cream = "delicious" 
```

2. 클래스는 단어별 첫글자는 대문자이고 Camel 스타일.
```python
class SoyNetClass:
  def __init__(self, person: str):
    self.person = person
    ...
```

2. 함수와 클래스에 대한 주석은 윗쪽에. 두줄 이상인 경우 단락 주석으로.
```python
"""
csv파일로부터 serial number를 읽는 함수
path : 파일 경로(string)
serial_number : 고유 값(int)
"""
def sn_from_csv(path: str) -> int:
    import pandas as pd # pandas : csv같은 data파일을 다루는 library

    df = pd.read_csv(path) # 파일 경로로부터 DataFrame를 불러온다.
    serial_number = df["SN"][0] # 첫번째 고유 값을 가져온다.

    return serial_number
```

3. 코드와 변수에 대한 짧은 주석은 오른쪽에. 두 줄 이상인 경우 윗 쪽에 단락 주석으로.
```python
"""
map : 모든 셀에 lambda 함수를 실행
lambda : 한 셀에 대해 해당 셀이 빈 문자열('')이면 np.nan(결측치)로 채우고 아니면 그대로 둔다.
"""
df["SN"] = df["SN"].map(lambda x : np.nan if x == '' else x) 
```

4. ,은 앞에는 붙이고 뒤에는 한 칸 띄기.
```python
a = [1, 2, 3, 4, 5]
```
  
5. = 가 함수나 클래스의 변수에 쓰일때는 붙이기.
```python
df.drdf(columns=df_drop_col_list, inplace=True)
```

6. =가 대입인 경우에는 앞 뒤로 한 칸 씩 띄우기.
```python
df_null_dict = dict(df.isnull().sum() / df.shape[0]) 
```

7. /, //, +=, -=, *=, /=, ==, % 같은 모든 산술연산자는 앞 뒤로 한 칸 씩 띄우기.
```python
r = p // q
g += 3
```

8. 가독성을 위해 빈 줄을 두는 경우 두 줄 까지만 허용.
```python
a_x = 3
#
#
#
b_y = 4 # not allowed
```

9. 프로젝트 폴더 구성시 함수들은 하나의 py파일에 저장, class는 class이름.py에 저장 권장.
```python
"""
현재 main.py 안.
utils라는 폴더와 그 밑에 utils.py, AutoEncoder.py, Work42.py 존재.
utils -> 폴더 이름에 따라 교체. 밑에는 예시.
"""
from utils import utils # utils.py 안에 함수 구성.
from utils import AutoEncoder # AutoEncoder.py 안에 class 구성.
from utils import Work42 # Work42.py 안에 Work42 class 구성.

z1 = utils.func1(...)
z2 = utils.func2(...)

AutoEncoder = AutoEncoder.AutoEncoder(...)
AutoEncoder.fit(...)

Work42 = Work42.Work42(...)
Wokr42.show(...)
```

10. f-문자열 포매팅(파이썬 3.6 이상부터) 권장.
```python
names = ["John", "Aily", "Chris", "Trump"]
ages = [12.31, 34.123, 23.0, 65]
for name, age in zip(names, ages):
  print(f"{name} is {float(age):.1f} years old.")
```

11. import는 한 줄에 하나씩만.
```python
# Correct
import os
import sys

# Wrong
import os, sys 
```

12. from을 사용할 경우 * 사용 비권장.
```python
from math import *
a = sqrt(3) # 이 경우는 명확하나 복잡한 경우 어느 곳에서 import한지 헷갈림

import math
b = math.sqrt(3) # 이것이 권장됨

from math import sqrt
c = sqrt(3) # not bad
```

13. type 검사법.
```python
# Correct 
if instance(obj, int):

# Wrong
if type(obj) is type(1):
```

14. sequence(string, list, tuple) 이 비어있는지 아닌지 검사법.
```python
# Correct
if not sequence:
if sequence:

#Wrong
if len(sequence):
if not len(sequence):
```

15. boolean 값을 == 로 비교하지 마라.
```python
# Correct
if guilty:

# Wrong
if guilty == True:
```


## 업데이트 내역
- 2021년 1월 18월: version 0.1 by 백승환
- 2021년 1월 18월: version 0.2 by 백승환
    * 변경사항: 6번 
        > ~~=가 대입인 경우에는 상관 없음. 오히려 한 칸 씩 띄우는 것 권장.~~<br>
        > 👉 =가 대입인 경우에는 앞 뒤로 한 칸 씩 띄우기.


<br>

참조: [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/#id24)
