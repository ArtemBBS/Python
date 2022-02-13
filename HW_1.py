import math

item_1 = 8
item_2 = 9

result_sum = item_1 + item_2
print(result_sum)
result_subtr = item_1 - item_2
print(result_subtr)
result_multi = item_1 * item_2
print(result_multi)
result_exp = item_1 ** item_2
print(result_exp)
result_m_exp = math.pow(8 , 9)
print(result_m_exp)
result_s_root = item_2 // 3
print(result_s_root)
result_m_s_root = math.sqrt (item_2)
print(result_m_s_root)

item_1 = 25
item_2 = 4
result_division = item_1 / item_2
print(result_division)
result_m_floor =math.floor(6.25)
print(result_m_floor)
result_m_ceil = math.ceil(6.25)
print(result_m_ceil)
result_int = math.floor(6.25)
print(result_int)
print("Тип данных в result_int:", type(result_int))
result_no_division_loss = item_1 / item_2
print(result_no_division_loss ,int(result_no_division_loss))
result_division_loss = item_1 % item_2
#print(result_no_division_loss ,loss(result_no_division_loss))

item_3 = 10
item_3 += 10
print(item_3)
item_3 -= 5
print(item_3)
item_3 *= 3
print(item_3)
item_3 /= 2
print(item_3)
item_3 **= 2
print(item_3)
item_3 **= 0.5
print(item_3)
item_3 %= 2
print(item_3)

b_item_t = True
b_item_f = False
b_item_result_sum = b_item_f + b_item_t
print(b_item_result_sum)
b_item_result_subtr = b_item_t - b_item_f
print(b_item_result_subtr)
b_item_result_multi = b_item_t * b_item_f
print(b_item_result_multi)
b_item_tint = int(b_item_t)
b_item_fint = int(b_item_f)
print(b_item_tint)
print(b_item_fint)
