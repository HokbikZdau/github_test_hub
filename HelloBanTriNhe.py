# Ghi chú;
# Câu lệnh in ra màn hình;

print("Hello World");
print("# Đây là comment")

a = 10;
b = 20;
h = a - b *30;
print("Đáp án là:",h);
print("Kiểu dữ liệu của",h,"là",type(h))

# Lấy toàn bộ nội dung của thư viện decimal
from decimal import*
# lấy tối đa 30 chữ số phần nguyên và phần thập phân
getcontext().prec = 30
a1 = Decimal(10) / 3
print(a1)	# K/q: 4,33333333333333333


# Kiểu dữ liệu chuyển đổi số thập phân thành phân số
from fractions import*
frac1 = Fraction(3.5)
print(frac1) # K/q: 7/2

# Lấy phần thức/ảo của số thực
com = complex(2,5)
print(com)
print(com.real)
print(com.imag)

# /a phát ra tiếng bíp
# /b mất chữ cái phía trước
# /n xuống dòng
# /t tab một khoảng
# // /' /" hiện ra dấu / ; ' ; "