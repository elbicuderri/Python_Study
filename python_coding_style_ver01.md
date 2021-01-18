# SoyNet Coding Guide For Python
>
> 작성목적: Python에서의 코딩 스타일을 통일시켜 소이넷 내에서 통일적인 작업환경을 구축하기<br>
> 위해 이 문서를 작성하였다. 이 문서가 절대적인 기준은 아니지만 가이드라인을 제시해준다.
><br><br>
> 활용방법: 작성한 Python 코드 위에 이 문서의 버전을 표기한다.
```python
"""
SoyNet Coding Guide For Python version 0.1
"""
```
> 
> 문서변경방법: 소이넷 직원 3명 이상이 합의하여 이 문서의 사항을 변경할 수 있고, 업데이트 내역을 기록하여야<br>
> 하며 이전 버전은 backup해두어야 한다. 그리고 그 버전의 작성자는 수정한 사람들의 이름들로 업데이트한다.

<br>

> 작성자: 백승환
>
> 작성일: 2021년 1월 18일
>
> version : 0.1

<br>

## Start

0. 변수와 함수는 소문자이면서 snake 스타일. **매우 강조**하고 싶으면 대문자 변수 가능.
```python
first_df = pd.read_csv(first_file_path)

def sn_from_csv(path: str) -> int: 
  ...

VERY_IMPORTANT_VARIABLE = 0
```

2. 클래스는 단어 첫글자는 대문자이고 Camel 스타일.
```python
class RoadData:
  def __init__(self, path: str):
    self.path = path
    ...
```

1. 함수와 클래스에 대한 주석은 윗쪽에. 두줄 이상인 경우 단락 주석으로.
```python
"""
csv파일로부터 serial number를 읽는 함수
path : 파일 경로(string)
serial_number : 고유 값(int)
"""
def sn_from_csv(path: str) -> int:
    import pandas as pd # pandas : csv를 다루는 library

    df = pd.read_csv(path) # 파일 경로로부터 DataFrame를 불러온다.
    serial_number = df["SN"][0] # 첫번째 고유 값을 가져온다.

    return serial_number
```

2. 코드와 변수에 대한 주석은 오른쪽에. 두 줄 이상인 경우 밑 쪽에 단락 주석으로.
```python
op["SN"] = op["SN"].map(lambda x : np.nan if x == '' else x) 
"""
map : 모든 셀에 lambda 함수를 실행
lambda : 한 셀에 대해 해당 셀이 빈 문자열('')이면 np.nan(결측치)로 채우고 아니면 그대로 둔다.
"""
```

3. ,은 앞에는 붙이고 뒤에는 한 칸 띄기.
```python
a = [1, 2, 3, 4, 5]
```
  
4. = 가 함수나 클래스의 변수에 쓰일때는 붙이기.
```python
op.drop(columns=op_drop_col_list, inplace=True)
```

5. =가 대입인 경우에는 상관 없음. 오히려 한 칸 씩 띄우는 것 권장.
```python
op_null_dict = dict(op.isnull().sum() / op.shape[0]) # OK
```


6. 가독성을 위해 빈 줄을 두는 경우 두 줄 까지만 가능.
```python
a_x = 3



b_y = 4 # not allowed
```

7. 프로젝트 폴더 구성시 함수들은 utils.py 파일(하나의 파일)에 저장, 클래스는 클래스.py 파일에 저장 권장.
```python
# utils -> 적당한 이름으로 교체 가능. 밑에는 예시.
from utils import utils # utils.py 안에 함수 구성.
from utils import AutoEncoder # AutoEncoder.py 안에 class 구성.
from utils import Work42 # Work42.py 안에 Work42 class 구성.
```


## 업데이트 내역
- 2021년 1월 18월: version 0.1 by 백승환

