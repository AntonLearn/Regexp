import csv
import re


# Читаем адресную книгу в формате CSV в список contacts_list
def read_csv(file_name):
    with open(file_name) as file:
        rows = csv.reader(file, delimiter=",")
        c_l = list(rows)
    return c_l


# Сохраняем получившиеся данные в другой файл в формате CSV:
def write_csv(file_name, c_l_o):
    with open(file_name, "w") as file:
        datawriter = csv.writer(file, delimiter=',')
        datawriter.writerows(c_l_o)


def correct_list(c_l):
    len_contacts_list = len(c_l)
    for i in range(len_contacts_list-1):
        ind_i = i + 1
        name = c_l[ind_i][0]+" "+c_l[ind_i][1]+" "+c_l[ind_i][2]
        name_list = name.split()
        len_name_list = len(name_list)
        for j in range(len_name_list):
            c_l[ind_i][j] = name_list[j]
        str_phone = c_l[ind_i][5]
        if str_phone != "":
            pattern = r"\d+"
            str_phone_list = re.findall(pattern, str_phone)
            str_phone = "".join(str_phone_list)
            pattern = r"^7|^8"
            repl = r"+7"
            str_phone = re.sub(pattern, repl, str_phone)
            base_number = str_phone[:2]+"("+str_phone[2:5]+")"+str_phone[5:8]+"-"+str_phone[8:10]+"-"+str_phone[10:12]
            len_str_phone = len(str_phone)
            if len_str_phone > 12:
                add_number = str_phone[-4:]
                str_phone = base_number + " доб." + add_number
            else:
                str_phone = base_number
            c_l[ind_i][5] = str_phone
    return c_l


def erase_duplicate(c_l):
    for contact in c_l:
        for contact_fill in c_l:
            if contact[0] == contact_fill[0] and contact[1] == contact_fill[1]:
                if len(contact[2]) > len(contact_fill[2]):
                    contact_fill[2] = contact[2]
                if len(contact[2]) < len(contact_fill[2]):
                    contact[2] = contact_fill[2]
                if len(contact[3]) > len(contact_fill[3]):
                    contact_fill[3] = contact[3]
                if len(contact[3]) < len(contact_fill[3]):
                    contact[3] = contact_fill[3]
                if len(contact[4]) > len(contact_fill[4]):
                    contact_fill[4] = contact[4]
                if len(contact[4]) < len(contact_fill[4]):
                    contact[4] = contact_fill[4]
                if len(contact[5]) > len(contact_fill[5]):
                    contact_fill[5] = contact[5]
                if len(contact[5]) < len(contact_fill[5]):
                    contact[5] = contact_fill[5]
                if len(contact[6]) > len(contact_fill[6]):
                    contact_fill[6] = contact[6]
                if len(contact[6]) < len(contact_fill[6]):
                    contact[6] = contact_fill[6]
    c_l_o = list()
    for contact in c_l:
        if contact not in c_l_o:
            c_l_o.append(contact)
    return c_l_o