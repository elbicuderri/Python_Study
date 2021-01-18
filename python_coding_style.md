# Coding Style For Python
- 변수와 함수는 소문자이면서 snake 스타일.
```python
first_df = pd.read_csv(first_file_path)
def sn_from_csv(path: str): 
  ...
```

- 클래스는 단어 첫글자는 대문자이고 Camel 스타일.
```python
def RoadData():
  def __init__(self, path):
    self.path = path
    ...
```

- 함수와 클래스에 대한 주석은 윗쪽에. 너무 긴 경우 단락 주석으로.
```python
# csv파일로부터 serial number 읽기
def sn_from_csv(path: str):
  ...
```

- 코드와 변수에 대한 주석은 오른쪽에. 너무 긴 경우 밑 쪽에 단락 주석으로.
```python
op40["SN"] = op40["SN"].map(lambda x : np.nan if x == '' else x) 
"""
해당 셀이 빈 문자열('')이면 np.nan(결측치)로 채우고 아니면 그대로 둔다.
"""
```

- , 은 앞에는 붙이고 뒤에는 한 칸 띄기.
```python
a=[1, 2, 3, 4, 5]
```
  
- = 가 함수나 클래스의 변수에 쓰일때는 붙이기.
```python
op40.drop(columns=op40_drop_col_list, inplace=True)
```

- 대입인 경우에는 상관 없음. 오히려 한 칸 씩 띄우는 것 권장.
```python
op_null_ratio_dict = dict(op.isnull().sum() / op.shape[0]) # OK
```


- 빈 줄은 두 줄 까지만 가능.
```python
a_x = 3



b_y = 4 # not allowed
```

- utils 폴더에 함수들은 utils.py 파일에 저장, 클래스는 클래스.py 파일에 저장 권장.
```python
from utils import utils
from utils import LSTMEncoder
from utils import TanoGan
```
