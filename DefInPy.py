# Sử dụng {}
# Các phần tử là một cặp key-value
# Các cặp value phân cách bằng dấu " : "
# { "key_1 : value_1", "key_2 : value_2", "key_3 : value_3"}
# Để kiểu str,int đều được

dic = {'Name': "Minh Trí","Age":"18"}
print(dic)

# Không thay đổi biến của Name_1,Age_1 chỉ lấy nó làm key
# để tạo key cho một dict
Name_1 = "Linh"
Age_1 = "20"
dic_1 = dict(name="Trí", Age=18)
print(dic_1)
print(Name_1)
print(Age_1)

# Phương thức formkeys
# dict fromkey(iteralbe,value)
inter_o = ("Name","Age",True,69)
dic_f = dict.fromkeys(inter_o,"Hoàn thành ")
print(inter_o)
print(dic_f)

# Lấy value = yourdic
print(dic_f["Name"])
print(dic_f["Age"])

# Thêm thủ công value vào
dic["Name"] = dic["Name"] + " Đào Linh" 
print(dic["Name"])











