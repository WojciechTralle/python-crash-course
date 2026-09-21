file_path = 'C:/Users/wtralle/OneDrive - University of Tampa-Spartans.ut/Documents/GitHub/python-crash-course/ch10/pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()

print(contents)