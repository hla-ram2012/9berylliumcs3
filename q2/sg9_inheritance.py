class Publication:
    #This class represents a publication with its respective title and author.
    def __init__(self, title, author):
        self.title = title
        self.author = author
    #This method returns the title of the publication.
    def get_title(self):
        print(f'Title: {self.title}')
        return self.title
    #This method returns the author of the publication.
    def get_author(self):
        print(f'Author: {self.author}')
        return self.author
    #This method sets or changes the title of the publication.
    def set_title(self, title):
        self.title = title
        return self.title
    #This method sets or changes the author of the publication.
    def set_author(self, author):
        self.author = author
        return self.author
    #This method displays the title and author of the publication.
    def display_info(self):
        print(f'Title: {self.title} \nAuthor: {self.author}')

#This class represents a book, and it inherits from the Publication class (Title and Author).
class Book(Publication):
    def __init__(self, title, author, number_pages):
        #The super() function is used to somewhat inherit the attributes of the parent class, Publication, and then the number of pages is added as an additional attribute.
        super().__init__(title, author)
        self.number_pages = number_pages
    #This method returns the number of pages in the book.
    def get_number_of_pages(self):
        return self.number_pages
    #This method sets or changes the number of pages in the book while ensuring that the number of pages is a positive integer.
    def set_number_of_pages(self, number_pages):
        #Ensures that the number of pages is a positive integer.
        if number_pages > 0:
            self.number_pages = number_pages
            return self.number_pages
        #If the number of pages is not positive, it prints an error message.
        else:
            print("The number of pages must be positive")
    #This method displays the title, author, and number of pages of the book.
    def display_info(self):
        print(f'Title: {self.title} \nAuthor: {self.author} \nNumber of pages: {self.number_pages}')

#This class represents a magazine, and it inherits from the Publication class (Title and Author) like the class book.
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        #Similar to the class book, the super() function is used to somewhat inherit the attributes of the parent class, Publication, and then the issue number is added as an additional attribute.
        super().__init__(title, author)
        self.issue_number = issue_number
    #This method returns the issue number of the magazine.
    def get_issue_number(self):
        return self.issue_number
    #This method sets or changes the issue number of the magazine while ensuring that the issue number is a positive integer.
    #The code of this method is identical to the class book because it has the same limitation (The issue number of the magazine and the number of pages of the book must be a positive integer)
    def set_issue_number(self, issue_number):
        #Ensures that the issue number is a positive integer.
        if issue_number > 0:
            self.issue_number = issue_number
            return self.issue_number
        #If the issue number is not positive, it prints an error message.
        else:
            print("The issue number must be positive")
    #This method displays the title, author, and issue number of the magazine.
    def display_info(self):
        print(f'Title: {self.title} \nAuthor: {self.author} \nIssue number: {self.issue_number}')

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()

print("\nMagazine Information:")
mag1.display_info()
