# Python dictionaries deep merge

여러개의 딕셔너리들을 깊은 병합시켜주는 Python Module

## 깊은병합?

- 기존의 Python의 딕셔너리는 딕셔너리 안에 또다른 딕셔너리가 있을 경우 최상단의 부모를 merge시키면(update시키면) 내부의 딕셔너리들은 전부 덮어씌워지는 낮은 병합을 시켜줬습니다.
- 깊은 병합은 딕셔너리 안에 수많은 자식 딕셔너리가 있을 경우 최상단의 부모를 merge시키면 자식 딕셔너리 또한 같이 merge 시켜주는 병합입니다.

## 모듈명

`Python_dictionaries_deep_merge`

## 클래스명

`deep_merge_dicts`

## `deepmerge`와 차이점

- 여러개의 딕셔너리를 한번에 넣을 수 있습니다.

## 다운로드 방법

```bash
pip3 install git+https://github.com/hbcha0916/Python_dictionaries_deep_merge.git

pip3 install Python-dictionaries-deep-merge==1.0
```

## 사용 방법(예시 코드)

```python
import Python_dictionaries_deep_merge as pdm

dict1 = {"hi": "hello","array":[1,2,3]}
dict2 = {"new": "world","array":[4,5,3] , "newdict": {"Indict": 1, "Indict2": 2, "newnewDict": {"InIndict": "wow"}},"array2": ['a', 'b', 'c', 'd']}
dict3 = {"this": "test", "array":[7,8,9],"array2": ['a', 'b'],"newdict": {"Indict3": 3, "Indict4": 4, "newnewDict": {"InIndict2": "wow"}}}

merged_dict = pdm.deep_merge_dicts(dict1, dict2, dict3)
print(merged_dict.getResult())
```

결과

```python
{'hi': 'hello', 'array': [1, 2, 3, 4, 5, 3, 7, 8, 9], 'new': 'world', 'newdict': {'Indict': 1, 'Indict2': 2, 'newnewDict': {'InIndict': 'wow', 'InIndict2': 'wow'}, 'Indict3': 3, 'Indict4': 4}, 'array2': ['a', 'b', 'c', 'd', 'a', 'b'], 'this': 'test'}
```

## deepmerge와 비교

```python
import Python_dictionaries_deep_merge as pdm
from deepmerge import always_merger

dict1 = {"hi": "hello","array":[1,2,3]}
dict2 = {"new": "world","array":[4,5,3] , "newdict": {"Indict": 1, "Indict2": 2, "newnewDict": {"InIndict": "wow"}},"array2": ['a', 'b', 'c', 'd']}
dict3 = {"this": "test", "array":[7,8,9],"array2": ['a', 'b'],"newdict": {"Indict3": 3, "Indict4": 4, "newnewDict": {"InIndict2": "wow"}}}

# 해당 모듈
merged_dict = pdm.deep_merge_dicts(dict1, dict2, dict3) #여러개 추가 가능
print("this module      >",merged_dict.getResult())

# deepmerge 라이브러리
merged_dict_dm1 = always_merger.merge(dict1,dict2)
merged_dict_dm2 = always_merger.merge(merged_dict_dm1,dict3)
print("deepmerge lib    >",merged_dict_dm2)
```

결과

```python
this module      > {'hi': 'hello', 'array': [1, 2, 3, 4, 5, 3, 7, 8, 9], 'new': 'world', 'newdict': {'Indict': 1, 'Indict2': 2, 'newnewDict': {'InIndict': 'wow', 'InIndict2': 'wow'}, 'Indict3': 3, 'Indict4': 4}, 'array2': ['a', 'b', 'c', 'd', 'a', 'b'], 'this': 'test'}
deepmerge lib    > {'hi': 'hello', 'array': [1, 2, 3, 4, 5, 3, 7, 8, 9], 'new': 'world', 'newdict': {'Indict': 1, 'Indict2': 2, 'newnewDict': {'InIndict': 'wow', 'InIndict2': 'wow'}, 'Indict3': 3, 'Indict4': 4}, 'array2': ['a', 'b', 'c', 'd', 'a', 'b'], 'this': 'test'}
```
