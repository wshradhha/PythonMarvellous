class BookStore:
    NoOfBook = 0
    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBook = BookStore.NoOfBook + 1

    def Display(self):
        print(f"{self.Name} by {self.Author} No of Books : {BookStore.NoOfBook}")

def main():
    Dobj1 = BookStore("abc","AbcAuthor")
    Dobj1.Display()
    Dobj2 = BookStore("xyz","xyzAuthor")
    Dobj2.Display()


if __name__ == "__main__":
    main()