def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")

hint_username("Ti")

number = 10
if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)

print(100*100)

# Tạo hàm đếm số lần của chữ cái đó xuất hiện
# Khởi tạo 1 hàm gồm 2 biến (số lần xuất hiện, nơi hoạt động)
# Tạo for chữ cái có trong hàm rồi + 1 lần xuất hiện
def find_char(char_to_find, input_str):
    count = 0
    for char in list(input_str):
        if char == char_to_find:
            count += 1

    if count > 0:
        print(f"Số lần xuất hiện của chữ '{char_to_find}' trong câu là {count}")
    else:
        print(f"Chữ cái '{char_to_find}' không tồn tại trong câu!")

check_str = "Hom nay la ngay gi vay?"
find_char('a', check_str)


#for x in range(10):
#    for y in range(x):
#       print(y)

def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {:.1f} km".format(miles,km)
    return result


print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

str_txt = "Rainfall"
result_char_f = []
i_find_char_f = str_txt.index("f")
result_char_f.append(str_txt[:i_find_char_f])
for char_sent in result_char_f:
   print(char_sent)


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
      new_filenames.append(filename[:-2] + "h")
    else:
      new_filenames.append(filename)

print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        pig_word = word[1:] + word[0] + "ay"
        say = say + pig_word + " "
    # Turn the list back into a phrase
    return say.strip()

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

def format_address(address_string):
    house_number = ""
    street_name = ""


    # Separate the house number from the street name.
    address_parts = address_string.split()
    
    for address_part in address_parts:
       # Complete the if-statement with a string method.  
       if address_part.isdigit():
         house_number = address_part
       else:
         street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.strip()
 
    # Use a string method to return the required formatted string.
    return "House number {} on a street named {}".format(house_number,street_name)

print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"


def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return string.count(" ") + 1


print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4



def sort_distance(distances):
    distances.sort() # Sort the list
    distances.reverse() # Reverse the order of the list
    return distances


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]

import os
# 1 
files = os.listdir("E:/File test Py") 
for i, file in enumerate(files, start=1):
    print(str(i) + ". " + file)

# 2
files = os.listdir("E:/File test Py") 
for i, file in enumerate(files, start=1):
    print(str(i) + ". " + file)

# csv
import csv
f = open("E:/File test Py/csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()



# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, newline='') as file_name:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file_name)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))



# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, newline='') as file:
    # Read the rows of the file
    rows = csv.reader(file)
    # Skip the header row
    next(rows)
    # Process each row
    for row in rows:
      name, color, ty = row
      # Format the return string for data rows only
      return_string += "a {} {} is {}\n".format(color, name, ty)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))
