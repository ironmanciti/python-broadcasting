"""
다음의 주민번호 리스트에서 남, 녀 별로 90 년생 이후 출생자를 골라내라.
"""
id_list = ['920801-1041798', '800902-2048746', '971010-1023987', '871203-2014987',
         '820801-1041798', '900902-2048746', '941010-1023987', '971203-2014987']

man = []
lady = []

for id in id_list:
    if id[:2] >= '90' and id[7] == '1':
        man.append(id)
    else:
        lady.append(id)

print('남성 =', man)
print('여성 =', lady)
