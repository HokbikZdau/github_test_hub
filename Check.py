strA = "{} {}".format("Hôm","Nay")
Hd = "\n\n\t\t\t\t\t\t\t\t\t\t {:^35}".format("DANH SACH BAN HANG")
row1 = "\t\t\t\t\t\t\t\t\t\t. {:_<3} . {:_^12}. {:_>10}.".format("","","")
row2 = "\t\t\t\t\t\t\t\t\t\t| {:^3} | {:^12}| {:^10}|".format("STT","Họ","Tên")
row3 = "\t\t\t\t\t\t\t\t\t\t| {:^3} | {:^12}| {:^10}|".format("1", "Nguyễn Lê","Minh Trí")
row4 = "\t\t\t\t\t\t\t\t\t\t| {:^3} | {:^12}| {:^10}|".format("2", "Phạm Văn", "Vượng")
row5 = "\t\t\t\t\t\t\t\t\t\t| {:^3} | {:^12}| {:^10}|".format("3","Nguyễn Văn","Linh")
row6 = "\t\t\t\t\t\t\t\t\t\t. {:_<3} . {:_^12}. {:_>10}.".format("","","")

tab1 = "\n\n\t\t\t\t\t\t\t\t\t\t" "{:^30}".format("DANH SACH DOI TUYEN BONG DA")
tab2 = "+ {:-<3} + {:-^10} + {:-^8} + {:-^5} + {:-^10} + {:->12} +".format("","","","","","")
#		   STT	    Họ      Tên     Lớp   Ngàysinh  Mã.SV
tab3 = "| {:^3} | {:^10} | {:^8} | {:^5} | {:^10} | {:>12} |".format("STT","Họ","Tên","Lớp","Ngày sinh","Mã sinh viên")
tab4 = "| {:^3} | {:^10} | {:^8} | {:^5} | {:^6} | {:>12} |".format("1","Phạm Văn","Hùng","23DT2","13/09/2005","23114823123")
tab5 = "| {:^3} | {:^10} | {:^8} | {:^5} | {:^6} | {:>12} |".format("2","Cấn Hân","Viên","23DT1","03/04/2005","231148293423")
tab6 = "| {:^3} | {:^10} | {:^8} | {:^5} | {:^6} | {:>12} |".format("3","Phục Lộc","Tài","23DL3","14/12/2005","23119283958")
tab7 = "| {:^3} | {:^10} | {:^8} | {:^5} | {:^6} | {:>12} |".format("4","Trịnh Công","Bình","23DT1","27/04/2005","23199231227")
tab8 = "| {:^3} | {:^10} | {:^8} | {:^5} | {:^6} | {:>12} |".format("5","Đặng Ngọc","Linh","23ST2","04/08/2005","23114892325")
tab9 = "+ {:-<3} + {:-^10} + {:-^8} + {:-^5} + {:-^10} + {:->12} +".format("","","","","","")

aliCt="\t"*5

print(Hd)
print(row1)
print(row2)
print(row3)
print(row4)
print(row5)
print(row6)

print(aliCt + tab1)
print(aliCt + tab2)
print(aliCt + tab3)
print(aliCt + tab4)
print(aliCt + tab5)
print(aliCt + tab6)
print(aliCt + tab7)
print(aliCt + tab8)
print(aliCt + tab9)

tk1 = "\t"
tk2 = "*"
print(tk1*2 + tk2)
print(tk1*2 + tk2*3)
print(tk1*2 + tk2*5)

rx1 = "+ %s + %s + %s +"
rx2 = "| %s | %s | %s |"
ltab1 = " "*40

r0 = ltab1 + "\t" + " Danh sách học sinh"
r1 = ltab1 + rx1 %("-"*5,"-"*8,"-"*7)
r2 = ltab1 + rx2 %("ID ".center(5," "), "Họ".center(8," "),     "Tên".center(7," "))
r3 = ltab1 + rx2 %("001".center(5," "), "Nguyễn".center(8," "), "Trí".center(7," "))
r4 = ltab1 + rx2 %("002".center(5," "), "Đăng".center(8," "),   "Trâm".center(7," "))
r5 = ltab1 + rx1 %("-"*5,"-"*8,"-"*7)
spc = "\n"*2

print(r0)
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(spc)

strT = "Trí Nguyễn".encode()
print(strT)

sk = 11**2
print(sk)

s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
s1 = s.lstrip("aAo").rstrip("a").title()
print(s1)

key1 = 'aAao'
key2 = 'a'
tx = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
fid = tx.lstrip(key1).rstrip(key2).title()
print(fid)


ts = "Ha Noi Viet Nam"
for i in ts:
	print(i.strip(" "),end=",")
print("\n")

# Tạo bảng Cửu chương >> =))) Thành công
listNm = [1,2,3,4,5,6,7,8,9,10]
for i in range(1,10):
	for k in listNm:
		print(i,"*",k,"=",i*k)
print("\n")

s = 'aaaaaaaAAAAAaaa//123123//000000//&&TTT%%abcxyznontqfadf'
# Lấy mật mã của s nằm giữa && và %%
# Tìm các key " && " và "%%"
findKey1 = s.find("&&")
findKey2 = s.find("%%")
s = s[ findKey1 + 2: findKey2]
print(s)

# Viết chương trình Python để in ra tất cả các ký tự trong một xâu ký tự.
getTx = 'Kteam'
for i in getTx:
	print(i)

# Viết chương trình Python để đảo ngược một xâu ký tự.
Text_1 = "Kteam"
getText_1 = Text_1[::-1]
print(getText_1)

# Viết chương trình Python để tìm số lần xuất hiện của một chuỗi con trong một xâu ký tự.
Text_in_Text = "Kteam qua la Kteam thi sao ha nao?"
#for i in Text_in_Text:
#	print("Kí tự",i,"xuất hiện",i.count(i),"Lần")

Text_text = "Matthutucuabanla&&13.2%%vaylaxongroido"
print(Text_text)
inf = Text_text.split("&&")[-1].split("%%")[-2]
print("Kết quả giải:",inf)

lst = [[1, 2], ["abc", "def"]]
lst.pop(1)
print(lst)
lst_list = lst.sort(key=str,reverse=False)
print(lst_list)

# Bài tập Tuple 
tup = tuple((1,2, 3) + ([3, 4],))
print(tup)

tup = (1,)
print(tup)

tup = (1,)
print(tup)

tup = (1, 2)
print(tup)

#test id
id_tst = (1,2,"kteam")
print(id(id_tst))

a = {1, 2}
b = a.copy()
b.clear()
print(a)

dict1 = {'key': 6969}
dict2 = dict1.copy()
dict2['key'] = 'changed'
print(dict1)
print(dict2)

tst_key = {}
key_value = {"a":3, 43:100}
tst_key.update(key_value)
print(tst_key)
print(type(tst_key))
tst_key[0] = "hashable"
print(tst_key)


get_item1 = 10 # int(input("Số thứ nhất:"))
get_item2 = 30 # int(input("Số thứ hai:"))
get_item3 = 50 # int(input("Số thứ ba:"))

if get_item1 > get_item2 and get_item1 > get_item3:
    print("Số lớn nhất là:", get_item1)
elif get_item2 > get_item1 and get_item2 > get_item3:
    print("Số lớn nhất là:", get_item2)
elif get_item3 > get_item1 and get_item3 > get_item2:
    print("Số lớn nhất là:", get_item3)

it1 = 20
it2 = 2
it3 = 30
slit = [ int(digit) for digit in str(it1 + it2 + it3)]
print("Số lớn nhất là", max(slit))

print(max(30,40,5))

with open("draft.txt", mode='a+') as Draf:
	Draf.seek(0)
	
	content = Draf.read()
print(content)

result_test = "Ham 1 bien thoi"

print(list(result_test))


def quantity_words():
    print("Chào bạn đến với chương trình đếm số từ trong câu!!")
    while True:
        char = input("Nhập câu cần đếm từ vào: ")
        word_count = len(char.split())
        print("Số từ trong câu là:", word_count)
        continue_input = input("Bạn có muốn tiếp tục hay không? (Y/N): ")
        if continue_input.lower() != "y":
            print("Cảm ơn bạn đã sử dụng chương trình!!")
            break

quantity_words()


# Học kiến trúc máy tính// học 
