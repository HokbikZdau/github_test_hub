strA = "Howcanihelpyou?"
strB = strA[-2] 		# >> u 

# Lấy chữ cái / của chuỗi[tại vị trí ]
strD = strA[len(strA) - 1]

# Cắt chuỗi  / của chuỗi A[vị trí bắt đầu : vị trí dừng]
strH = strA[1:7]
# Cắt tại chuỗi A
#	[vị trí bắt đầu : vị trí dừng : bước]
strO = strA[None:1:-2]
# Kiểm tra hàm B có trong hàm A không?
strC = strB in strA
strUI = strA[None:5:2]


# Đổi kiểu dữ liệu/ ép thành int/str/float
StrA = float("6.8") + 3.2


# Tách chuỗi bằng split
strP = " Python là số một"
# biến.split(kí tự cắt, số lần)
k = strP.split(" ",1)				# >> K.q: [" " "Python là số một"]

# %s thay thế cho 1 str
k1 = "%s" %("Hôm nay") 	# >> "Hôm nay"
# %r giống %s dùng để thay thế
# %d chỉ thay thế cho số nguyên 1,2,3,4
k2 = "%d" %(2.4) 		# >> 2
# %f thay thế cho số thực được
k3 = "%f" %(4.3332) 	# >> 4

# Thay thế biến trong chuỗi bằng f{tên biến}
name = " Minh Trí"											 #  >> Tên của bạn là Minh Trí
adress = " Đà Nẵng"											 #	   Địa chỉ: Đà Nẵng
Phone = " 220333"											 #     Phone: 220333
k4 = f"Tên của bạn là {name}\nĐịa chỉ {adress}\nPhone: {Phone}"	


# Sử dụng format tạo bảng
row1 = "| {:_<6} | {:_^15} | {:_>10} |".format('','','')
#		    ID    Họ&Tên   N.sinh 
row2 = "| {:<6} | {:^15} | {:^10} |".format('ID','Họ và tên','Nơi sinh')
row3 = "| {:<6} | {:^15} | {:^10} |".format('233','N.Thanh Trà','Đà Nok')
row4 = "| {:<6} | {:^15} | {:^10} |".format('2494','Đào Mĩ Hạnh','Japan')
row5 = "| {:<6} | {:^15} | {:^10} |".format('2728s','Hồng Nhung','Ja Kan Da')
row6 = "| {:_<6} | {:_^15} | {:_>10} |".format('','','')

soud = "/a"

print("\n"*2 + row1)
print(row2)
print(row3)
print(row4)
print(row5)
print(row6)

# .capitalize() >> In Hoa chữ cái đầu
# .upper()  	>> In hoa toàn bộ
# lower()	    >> In thường
# swapcase() 	>> Hoa, thường trao đổi
# title()		>> 
# center(with,[fillchar]) >> Chữ cái ở giữa cách hai bên with đơn vị bằng các kí tự fillchar
# rjust/ljust 	>> Căn phải/căn trái
# join(["1","2","3"])	  >> Lập lại các kí tự 1co gi hot 2co gi hot 3co gi hot 
# replace ("chữ đc thay thế","thay thành")
# strip("str")	>> Cắt kí tự ở hai đầu, cuối
# tương tự, ta cs lstrp/rstrip
# removeprefix  >> Xoá kí tự ở đầu chuỗi ( không phải toàn như strip)
# removesuffix  >> Xoá kí tự ở cuối chuỗi( không phải toàn như strip)

# cắt chuỗi     >> quy vễ kiểu list
a = "Làm gì vậy"
b = a.split(" ",1)
# partition     >> cắt chuỗi quy về kiểu tuple
c = a.partition("g")
# count         >> đếm số lần xuất hiện của str trong a
d = a.count("v",0,10)
# startswith    >> str a có bắt đầu bằng chữ L hay ko? Tương tự có endswith
e = a.startswith("L",0,9)
# find    		>> tìm vị trí chữ cái đó
# isupper		>> kiểm tra có phải toàn bộ upper không
# isdigit		>> Kiểm tra 1 tk có phải 1 số hay không
