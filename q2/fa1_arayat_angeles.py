class Publication:
    def __init__(self, author, title):
        self.__author = author
        self.__title = title

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(author, title)
        self.__number_pages = number_pages

    def get_number_of_pages(self):
        return self.__number_pages

    def set_number_of_pages(self, number_pages):
        if number_pages < 0:
            print("Number of pages must be positive.")
            return
        self.__number_pages = number_pages

    def display_info(self):
        super().display_info()
        print("Number of pages:", self.__number_pages)


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(author, title)
        self.__issue_number = issue_number

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        self.__issue_number = issue_number


pub1 = Publication("Ratchiff, R. & Van Dongen, H.", "Journal of Experimental Psychology")
book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information: ")
pub1.display_info()

print("\nBook Information: ")
book1.set_number_of_pages(-310)
book1.display_info()

print("\nMagazine Information: ")
mag1.display_info()
print("Issue Number:", mag1.get_issue_number())

