def get_count_char(str_):
    str_ = str_.split(" ") # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = "".join(str_)
    str_ = str_.lower()
    return str_
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dic = {}
DEFAULT_COUNT = 0
count = 0
for char in get_count_char(main_str):
    if char.isalpha() == True:
        dic[char] = (dic.get(char, DEFAULT_COUNT)) + 1
        count += 1
dic_ = dic
print(dic)

"""keys_ = dic_.keys()
print(dic_)
dic_ = dic.values()
print(dic_)
i = 0
for values in dic_:
    values = (values * 100) / count
    print(int(values))
    i = dic.items()
    print(i)
    print(list(dic.items()))
    print(list(dic.items())[0])
    dic_[keys_] = int(values)
    print(dic_)"""
