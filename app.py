"""This is the beginning of python."""

# student_count = 200
# class_name = "        Python class"
# amount = 200.49

# print(len(class_name))
# print(class_name[0])
# print(class_name[0:9])
# print(class_name[:3])
# print(class_name[:])
# print(class_name.title())
# print(class_name.strip())
# print(class_name.upper())
# print(class_name.find("P"))
# print("py" in class_name)
# print("Py" in class_name)
# print("wy" not in class_name)


input_num = input("Enter any number here:")
print(type(input_num))

def odd_or_even(input):
    if input % 2 == 0:
        print("even")
    else:
        print("odd")


odd_or_even(int(input_num))
print("End")