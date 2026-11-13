from csv import reader


output = open('bibliographic.txt', 'w')

counter_1 = 0
counter_bigliographic = 0
author = "*"
author = input()
all_books = []
found_books = []
# filename = "books-en.csv"
filename = "books.csv"
with open(filename, 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')

    for row in table:
        if row[0] != "ISBN" and row[0]!="ID":
            all_books.append(row)
        counter_bigliographic += 1
        book_title = row[1]
        if filename == 'books-en.csv':
            year_of_publication = row[3]
            book_author = row[2]
        else:
            book_author = row[3]
            year_of_publication = row[6].split()[0][-4:]
        if 1 < counter_bigliographic <= 21:
            output.write(
                f"{counter_bigliographic - 1}. {book_author}. {book_title} - {year_of_publication}\n")

        # publisher=row[4]
        # downloads=row[5]
        # price=row[6]
        if len(book_title) > 30:
            counter_1 += 1
        if author == book_author:
            found_books.append(row)
if len(found_books) == 0:
    found_books = "not found"
print(found_books)
print(counter_1)
if filename == 'books-en.csv':
    print(sorted(all_books, key=lambda x: int(x[5]))[-20:])
else:
    print(sorted(all_books, key=lambda x: int(x[8]))[-20:])

output.close()
