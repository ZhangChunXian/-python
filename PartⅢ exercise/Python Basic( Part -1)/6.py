"""
numbers_list = []
number_tuples = []

while True:
    for number in numbers_list:
        try:
            number = float(input("Please give me a number: "))
        except ValueError:
            if number == "q":
                break
            else:
                print("Please enter a number: ")
                continue
        else:
            numbers_list.append(number)

# 倒序输出
inverse_numbers_list = numbers_list[-1:-len(numbers_list)-1:-1]

# 输出列表
print("inverse_numbers_list")

# 以上代码运行异常
"""



# The Sample Solution
values = input("Input some comma separated numbers: ")
list = values.split(",")

tuple = tuple(list)

print('list: ', list)
print('Trple:', tuple)