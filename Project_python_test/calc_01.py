price = 6
num_01 = 12458.771
num_02 = 12460.232
num_03 = 12473.320
d_01 = 26
d_02 = 27
d_03 = 30+4
#test
del_num = num_02-num_01
score_month_01 = (num_02-num_01)/(d_02-d_01)
score_month_02 = (num_03-num_02)/(d_03-d_02)

print(f'За 27 инюня потрачено {round(num_02-num_01,1)} м3')
print('Тогда траты за месяц')
print(f'        {round(score_month_01*30,1)} м3 газа')
print(f'        {int(score_month_01*30*price)} руб/м')
print()
print(f'С 27 июня по 4 июля потрачено {round(num_03-num_02,1)} м3')
print('Тогда траты за месяц')
print(f'        {round(score_month_02*30,1)} м3 газа')
print(f'        {int(score_month_02*30*price)} руб/м')
