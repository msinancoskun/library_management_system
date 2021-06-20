id_password = {'admin': '123', 'Ahmet': '1234', 'Ayse': '4567'}

list_of_books = [
    {'Book id': '001', 'Book Name': 'Biology', 'Book Authors': ['Alice', 'Bob'], 'Number of Copies': '2'},
    {'Book id': '002', 'Book Name': 'Chemistry', 'Book Authors': ['Alice'], 'Number of Copies': '1'}
]

borrowed_books_by_student = {}


def list_books():
    print("***List of Books***")
    book_index = 0
    for index, book in enumerate(list_of_books):
        book_index += 1
        book_id = book['Book id']
        book_name = book['Book Name']
        book_authors = book['Book Authors']
        number_of_copies = book['Number of Copies']
        print("{0}.Book id: {1}, Book Name: {2}, Book Authors: {3}, Number of Copies: {4}".format(book_index, book_id,
                                                                                                  book_name,
                                                                                                  book_authors,
                                                                                                  number_of_copies))


def create_a_book():
    while True:
        input_book_name = input("What is the name of the book that you want to add?: ")
        input_book_id = input("What is the id that you want to give for %s book?: " % input_book_name)
        book_already_exists = False
        for book in list_of_books:
            book_id = book['Book id']
            book_name = book['Book Name']
            if book_id == input_book_id or book_name == input_book_name:
                book_already_exists = True
                break
        if book_already_exists:
            print("This id is already taken by another book!")
            continue
        input_book_author = input("What is the authors of {} book: ".format(input_book_name))
        input_number_of_copies = input("How many copies do you have for {} book: ".format(input_book_name))
        are_you_sure = input("Are you sure?(Y/N): ")
        if are_you_sure.upper() == 'Y':
            print("The following book is added to you library.")
            print("Book id: {0}, Book Name: {1}, Book Authors: [{2}], Number of Copies: {3}".format(
                input_book_id, input_book_name, input_book_author, input_number_of_copies))
            new_book = {"Book id": input_book_id, "Book Name": input_book_name,
                        "Book Authors": input_book_author,
                        "Number of Copies": input_number_of_copies}
            list_of_books.append(new_book)
            break


def clean_a_book():
    list_books()
    clean_a_book_by_id = input("What is the id of the book that you want to delete,(Enter 0 to go to main menu): ")
    while clean_a_book_by_id != '0':
        for book in list_of_books:
            if clean_a_book_by_id == book['Book id']:
                list_of_books.remove(book)
        list_books()
        break


def search_for_a_book_admin():
    search_book_name_or_author = input("Enter book name or author to search (Enter 0 to go to main menu)?: ")
    book_index = 0
    for book in list_of_books:
        book_index += 1
        book_id_search = book['Book id']
        book_name_search = book['Book Name']
        book_author_search = book['Book Authors']
        number_of_copies_search = book['Number of Copies']
        while search_book_name_or_author in book['Book Name'] or search_book_name_or_author in book['Book Authors']:
            if search_book_name_or_author == '0':
                break
            if search_book_name_or_author == book_name_search or search_book_name_or_author in book_author_search:
                print("{0}. Book id: {1}, Book Name: {2}, Book Authors: [{3}], Number of Copies: {4}".format(
                    book_index, book_id_search, book_name_search, book_author_search, number_of_copies_search))
                break


def change_num_of_copies():
    list_books()
    input_id_book = input("What is the id of the book for the change ?(Enter 0 to go to main menu): ")
    new_number_of_copy = int(input("Enter the new value for the no. of copies: "))
    for item in range(len(list_of_books)):
        if new_number_of_copy < len(id_password):
            print("%s user(s) is/are holding the book, try a larger number!" % len(id_password))
            break
        else:
            for book in list_of_books:
                if book['Book id'] == input_id_book:
                    book['Number of Copies'] = new_number_of_copy
                    print("The following book has been updated:")
                    print(book)
            break


def show_students_borrowed_a_book_by_id():
    input_id_of_book = input("What is the id of the book that you want to show, (Enter 0 to go to main menu)?: ")
    user_id_storage = []
    for book_id, user_id in borrowed_books_by_student.items():
        if input_id_of_book in book_id:
            user_id_storage.append(book_id)
    index = 0
    for book in list_of_books:
        if book['Book id'] in user_id_storage:
            index += 1
            print("Students borrowed book:")
            print("%s-%s" % (index, user_id))


def list_users_by_id():
    print("*** Current Users ***")
    index = 0
    for user_id in id_password:
        while user_id != 'admin':
            index += 1
            print("{}-{}".format(index, user_id))
            break


def create_user():
    name_of_the_user = input("What is the name of user that you want to create?: ")
    if name_of_the_user in id_password:
        print("This id already exists!")
        create_user()
    else:
        password_of_the_user = input("What is the password for the new account?: ")
        id_password.update({name_of_the_user: password_of_the_user})
        print("\nThe following user has been added: ")
        print('Name: ' + name_of_the_user + ', Password: ' + password_of_the_user)


def delete_user():
    list_users_by_id()
    user_to_delete = input("Which user do you want to delete?: ")
    while user_to_delete in id_password.keys():
        del id_password[user_to_delete]
        print("{} is deleted!".format(user_to_delete))
        list_users_by_id()
        break
    else:
        print("Provide a valid input!")
        delete_user()


def search_for_a_book_student():
    search_for_a_book_admin()


def add_a_book_to_my_books_list():
    while True:
        print("Avaliable books are: ")
        list_books()
        input_add_book_id = input("What is the id of a book that you want to add (Enter 0 to go to main menu)?: ")
        if input_add_book_id == '0':
            break
        selected_book = None
        for book in list_of_books:
            if input_add_book_id == book['Book id']:
                selected_book = book
                break
            if selected_book is None:
                print("This book is not found in the library!")
                continue
            if selected_book['Number of Copies'] == 0:
                print("There is no avaliable number of copies for this book.")
                continue
        students = borrowed_books_by_student.get(input_add_book_id)
        if students is not None and user_id in students:
            print("The book is already in your library.")
            continue
        if input_add_book_id in borrowed_books_by_student:
            borrowed_books_by_student[input_add_book_id].append(user_id)
        else:
            borrowed_books_by_student[input_add_book_id] = [user_id]
        print("The book added to your library.")
        return


def delete_a_book_from_my_books_list():
    while True:
        input_book_to_delete = input("What is the id of the book that you want to delete?: ")
        list_books()
        book_found = None
        if input_book_to_delete == '0':
            break
        for book in list_of_books:
            if input_book_to_delete == book['Book id']:
                book_found = book
                break
        if book_found:
            print("The following book has been selected: ")
            print(print("Book id: %s, Book Name: %s, Book Authors: %s, Number of Copies: %s" %
                        (book_found['Book id'], book_found['Book Name'], book_found['Book Authors'],
                         book_found['Number of Copies']))
                  )
        else:
            print("The id that you have provided is not in your library!")
            continue
        are_you_sure = input("Are you sure?(Y/N): ")
        if are_you_sure == 'Y':
            students = borrowed_books_by_student.get(input_book_to_delete)
            if students and user_id in students:
                students.remove(user_id)
                print("Book has returned back!")
        break


def show_my_borrowed_books():
    print("Your books: ")
    book_id_storage = []
    for book_id, id_of_users in borrowed_books_by_student.items():
        if user_id in id_of_users:
            book_id_storage.append(book_id)
    book_index = 0
    for book in list_of_books:
        if book['Book id'] in book_id_storage:
            book_index += 1
            print("%s.Book id: %s, Book Name: %s, Book Authors: %s, Number of Copies: %s" %
                  (book_index, book['Book id'], book['Book Name'], book['Book Authors'], book['Number of Copies']))


def exit_application():
    exit()


print("****Welcome to Library Management System****")
print("\tPlease provide login information")

user_id = input("\tID: ")
user_password = input("\tPassword: ")

while True:
    if user_id in id_password.keys() and user_password == id_password[user_id]:
        print("Successfully logged in!")

    else:
        print("Invalid id or password please try again!")
        user_id = input("\tID: ")
        user_password = input("\tPassword: ")

    while True:
        if user_id == 'admin':
            functions = {
                '1': list_books,
                '2': create_a_book,
                '3': clean_a_book,
                '4': search_for_a_book_admin,
                '5': change_num_of_copies,
                '6': show_students_borrowed_a_book_by_id,
                '7': list_users_by_id,
                '8': create_user,
                '9': delete_user,
                '10': exit_application
            }

            print("""Welcome Admin! What do you want to do?
1-List books
2-Create a book
3-Clean a book
4-Search for a book
5-Change number of copies of book by id
6-Show students borrowed a book by id
7-List Users by id
8-Create User
9-Delete User
10-Exit""")
        else:
            functions = {
                '1': search_for_a_book_student,
                '2': add_a_book_to_my_books_list,
                '3': delete_a_book_from_my_books_list,
                '4': show_my_borrowed_books,
                '5': exit_application
            }

            print("""Welcome %s what do you want to do ?
1-Search for a book
2-Add a book to my books list
3-Delete a book from my books list
4-Show my borrowed books
5-Exit""" % user_id)

        choice_of_user = input("Your choice: ")
        if choice_of_user in functions:
            func = functions[choice_of_user]
            func()
        elif choice_of_user == '5' or choice_of_user == '10':
            func = functions[choice_of_user]
            func()
        else:
            print("""You have entered bigger than 10. 
Your choice should be between 1-10!""")
