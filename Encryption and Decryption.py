def encrypt(string):
    divide_mark_num = 0
    addition_mark_num = 0
    divide_marks = ["%", "^", "&", "*"]
    addition_marks = ["!", "@", "#", "$"]
    result = []
    nums = [ord(c) for c in string]
    for i in range(len(nums)):
        if i == 0:
            result.append(nums[i])
        else:
            diff = nums[i] - nums[i-1]
            if diff > 0:
                result.append(addition_marks[addition_mark_num])
                addition_mark_num += 1
            if addition_mark_num > 3:
                addition_mark_num = 0
            elif diff < 0:
                result.append(divide_marks[divide_mark_num])
                divide_mark_num += 1
            if divide_mark_num > 3:
                divide_mark_num = 0
            if diff == 0:
                result.append("=")
            result.append(abs(diff))
    result[0] = str(result[0] - 65)
    result = [str(x) for x in result]
    return "".join(result)
def decrypt(encode_string, addition_marks, divide_marks):
    result = ""
    mark_lst = []
    int_lst = []
    uncrypted_lst = []
    new_ch = 0
    for c in encode_string:
        if c not in addition_marks and c not in divide_marks:
            result += c
        else:
            result+=" "+c+" "
            mark_lst.append(c)
    seperated_lst = result.split(" ")
    for i in seperated_lst[0::2]:
        int_lst.append(int(i))
    int_lst[0] = int_lst[0]+65
    new_ch = int_lst[0]
    uncrypted_lst.append(chr(int_lst[0]))
    for j in range(1,len(seperated_lst), 2):
        if seperated_lst[j] in divide_marks:
            new_ch = new_ch-int(seperated_lst[j+1])
        if seperated_lst[j] in addition_marks:
            new_ch = new_ch+int(seperated_lst[j+1])
        uncrypted_lst.append(chr(new_ch))
    uncypted_str = "".join(uncrypted_lst)
    return uncypted_str




addition_marks = ["!", "@", "#", "$"]
divide_marks = ["%", "^", "&", "*"]
encode_string1 = encrypt(input("Enter encryption sentence: "))
result = print(decrypt(encode_string1, addition_marks, divide_marks))
print(encode_string1)


