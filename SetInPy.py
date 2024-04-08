# kiểu dữ liệu set sài (<dữ liệu 1>, <dữ liệu 2>,....)
# Các p.tử của set không trùng lặp
# Set không nhận list, nhận tuple/str ( vì là hashable)
# Hashable là địa_chỉ|giá trị >> 0x2234|"minh trí"      >> id của "minh trí"   là 0x2234
#							  >> 0x2334|("Hôm nay là")  >> id của "Hôm nay là" là 0x2334
# Các kiểu dữ liệu hashable luôn có id khác nhau //
# Các kiểu dữ liệu unhashable có id cố định 

set_1 = {1,2,3,4, "Mỉnhtri"}
set_2 = {"Minhtri",}
print(set_1)
print(set_2)

