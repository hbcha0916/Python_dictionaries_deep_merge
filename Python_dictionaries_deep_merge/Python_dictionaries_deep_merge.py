class deep_merge_dicts:
    result = {}
    def __init__(self,*dicts):
        self.result = self.merge_nested_dicts(*dicts)

    def merge_dicts(self,dict1, dict2):
        # 두 딕셔너리를 병합하는 함수
        for key in dict2:
            if key in dict1 and isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                # 두 값이 모두 딕셔너리인 경우, 재귀적으로 합침
                self.merge_dicts(dict1[key], dict2[key])
            elif key in dict1 and isinstance(dict1[key], list) and isinstance(dict2[key], list):
                # 두 값이 모두 리스트인 경우, 합치기
                dict1[key] = dict1[key]+dict2[key]
            else:
                # 두 값 중 하나가 딕셔너리가 아닌 경우, 값을 덮어씀
                dict1[key] = dict2[key]
        return dict1

    def merge_nested_dicts(self,*dicts):
        # 중첩된 딕셔너리를 합치는 함수
        merged_dict = {}
        for dictionary in dicts:
            merged_dict = self.merge_dicts(merged_dict, dictionary)
        return merged_dict

    def getResult(self):
        return self.result


# 중첩된 딕셔너리 합치기
if __name__ =="__main__":
    dict1={"hi":"hello"}
    dict2={"new":"world","newdict":{"Indict":1, "Indict2":2,"newnewDict":{"InIndict":"wow"}},"array":['a','b','c','d']}
    dict3={"this":"test","array":['a','b'],"newdict":{"Indict3":3, "Indict4":4,"newnewDict":{"InIndict2":"wow"}}}

    merged_dict = deep_merge_dicts()
    merged_dict.targetDicts(dict1, dict2, dict3)
    print(merged_dict.getResult())