# Khác vs cout của str// count của list sẽ đếm số phần tử đó xuất hiện bao nhiêu lần
a = [ 1,1,1,1,3,0]
c = a.count(1) # count(...) Nhập 1,2,3 sễ tự đếm số lần xuất của biến trong đó
print(c)

# index() >> vị trí của biến đó 
d= a.index(0)
print(d)

# copy() >> copy sang biến khác
e = a.copy()  # >> e = [ 1,1,1,1,3,0]

# clear() >> xoá toàn bộ biến trong list
f = a.clear() # >> f = []

# append() >> thêm biến vào list
h = a.append(1) # >> thêm 1 vào a

# extend() >> lấy từng phần tử trg () vào list
u = a.extend([3,6]) # >> lấy biến trong list thêm vào ném vào list

# insert(in,i) >> thêm biến i ở vị trí in 

# pop(i) bỏ đi phần tử thứ i trong list 
# remove(x) >> bỏ biến x có trong list


