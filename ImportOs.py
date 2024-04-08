import re
import os

pattern = r"^\w+\.txt$"
path = "E:\\sssx"  # Đảm bảo sử dụng hai dấu gạch chéo khi chỉ định đường dẫn
for filename in os.listdir(path):
    if re.match(pattern, filename):
        os.remove(os.path.join(path, filename))