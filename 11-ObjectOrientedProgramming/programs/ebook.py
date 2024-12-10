class e_book:
    def __init__(self,title,author,number_of_pages):
        self.title=title
        self.author=author
        self.number_of_pages=number_of_pages
        self.current_page=0
        self.is_open=False
    def open(self):
        self.is_open=True
    def close(self):
        self.is_open=False
    def next_page(self):
        if self.is_open:
            if self.current_page<self.number_of_pages:
                self.current_page+=1
        else:
            print("can't change page when the book is closed")
    def previous_page(self):
        if self.is_open:
            if self.current_page>0:
                self.current_page-=1
        else:
            print("can't change page when the book is closed")
    
    def display_status(self):
        print("My E-Book")
        print("Title:\t\t",self.title)
        print("Author:\t\t",self.author)
        print("Pages:\t\t",self.number_of_pages)
        if self.is_open:
            print("Current page: \t",self.current_page)
        else:
            print(f"Book is closed\t ({self.current_page})")
    
