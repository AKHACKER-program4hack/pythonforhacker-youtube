# s = set()
s_from_list = set([1,2,3])
# q = {1,2,3}
s_from_list.add(7)
s2 = s_from_list.union([6,8,9])
s3 = s2.intersection([1,2,3])
# print(s_from_list)
print(s3)