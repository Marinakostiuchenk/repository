def delete(list_, index=None): #print(list(set(list_)))
    if index not in list_:
        del list_[-1]
    else:
        del list_[index]
    return list_
print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

#слайсировнаие: del list_[index:index+1]
