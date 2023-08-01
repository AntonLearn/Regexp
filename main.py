from modules_phonebook import read_csv, write_csv, correct_list, erase_duplicate


def main():
    contacts_list = read_csv("phonebook_raw.csv")
    contacts_list = correct_list(contacts_list)
    contacts_list_out = erase_duplicate(contacts_list)
    write_csv("phonebook.csv", contacts_list_out)


if __name__ == '__main__':
    main()









