import pandas as pd

class Library_book:
    def __init__(self):
        self.Book_available = ['A-book', 'B-book', 'C-book', 'D-book']
        self.Btaken_dict = {'Man1':'E-book', 'Man2':'F-book', 'Man3':'G-book'}

    def available_book(self):
        print('Available books are- ')
        for i, book in enumerate(self.Book_available, 1):
            print(i, book)
        print('\n')

    def lend_book(self):
        '''for key in (self.Btaken_dict):
            print(f"{key} has been taking {self.Btaken_dict[key]} taht book now. ")'''
        name = list(self.Btaken_dict.keys())
        books = list(self.Btaken_dict.values())
        c =list([name] + [books])
        df = pd.DataFrame(c, index= ['Customer Name:', 'Book name:'])
        print(df)
        print('\n')


    def donate_book(self):
        book_name = input('Enter the book name: ')
        self.Book_available.append(book_name)
        print('\n')

    def taken_book(self):
        customer_name = input('Enter your name: ')
        Book_take = input('Which book you want to take: ')
        self.Book_available.remove(Book_take)
        self.Btaken_dict[customer_name] = Book_take
        print('\n')
        
    '''def return_book(self):
        book_name1 = input('Enter the return book name: ')
        for key in (self.Btaken_dict):
            if (self.Btaken_dict[key] == book_name1):
                del(self.Btaken_dict[key])
        print('\n')'''


obe1 = Library_book()


while True:
    print('\n')

    print("Welcome to Saiakt Library")
    '''print('1@: Check which books are available now in library. WRITE CODE: SPBS\n'
          '2@: If you see this book is present, then you can request for taking the book.WRITE CODE: WTT\n'
          '3@: If you want to return the book, WRITE CODE: RB\n'
          'Other Thing you could do.\n'
          '1#: You can donate book. WRITE CODE: D\n'
          '2#: You can see who took your desire book. WRITE CODE: WHO\n'
          '3#: WRITE CODE: Thankyou --- for exit the library.')
    print('\n')'''

    dictli = {'Purpose': ['Available Book', 'Want to take', 'Return the book', 'Donate book.', 'Who took book',
                          'for exit library.'], 'Write Code': ['SPBS', 'WTT', 'RB', 'D', 'WHO', 'THU']}

    df = pd.DataFrame(dictli)

    print(df)



    '''
    FULL FROM.
    SPBS= 'see present books',
    WTT = 'want to take'
    RB = 'Return the book'
    D = 'donate or return the book'
    WHO = 'who's one taken my desire book'
    '''

    mode = input('What you want to do? : ')
    if mode=='SPBS':
        obe1.available_book()
    elif mode == 'WTT':
        obe1.taken_book()
    elif mode == 'D':
        obe1.donate_book()

    elif mode == 'WHO':
        obe1.lend_book()
    elif mode == 'THU':
        break

