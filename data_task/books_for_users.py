import json
from csv import DictReader

with open("initial_files/users.json", "r", encoding='UTF-8') as f:
    users = json.loads(f.read())

with open("initial_files/books.csv", "r", encoding='UTF-8') as f:
    books = []
    reader = DictReader(f)
    for row in reader:
        books.append(row)


def distribute_books_to_users(books_list, users_list):
    minimum_chunk_length = len(books_list) // len(users_list)
    remain_books_count = len(books_list) % len(users_list)
    result = []
    iterator = iter(books_list)
    for i in range(len(users_list)):
        result.append([])
        for j in range(minimum_chunk_length):
            result[i].append(iterator.__next__())
        if remain_books_count:
            result[i].append(iterator.__next__())
            remain_books_count -= 1
    return result


books_for_users = []

for user in users:
    books_for_users.append(
        {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': distribute_books_to_users(books, users)[users.index(user)]
        }
    )

with open("result.json", "w", encoding='UTF-8') as f:
    s = json.dumps(books_for_users, indent=4)
    f.write(s)
#
