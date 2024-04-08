# Xử lí File trong Py
# Mở File
open_file = open("Check.txt")
print(open_file)

# r mở để dọc
# r+ mở để đọc và ghi
# w mở để ghi và xoá hết nội dung file hiện có			// Nếu file không tồn tại sẽ tạo file theo tên của chúng ta truyền vào
# w mở để ghi, đọc và xoá hết nội dung file hiện có		//
# a mở để ghi 			// Nếu file không tồn tại sẽ tạo file theo tên của chúng ta truyền vào
# a+ mở để ghi, đọc		// .....

# read(n) đọc n kí tự trong file
read_file_1 = open_file.read(7)     # đọc hết - '-1'    // đọc n kí tự - '3,8,10'
read_file_2 = open_file.readline(3) # để số - đọc kí tự // none - đọc từng dòng
data = tuple(open_file)
open_file.close()			        # đóng file khi đọc xong

print(read_file_1)
print(read_file_2)
print(data)

oject_file = open('Check.txt', mode = 'a+')
read_data  = oject_file.write('Hom nay dep troi that')
open_file.close()
print(read_data)

# seek(n)   # đưa con trỏ về kí tự thứ n
# with()	# function file không cần phải close // Thực hiện được 1 function thôi
with open('Check.txt') as fobj:
    data = fobj.read()

