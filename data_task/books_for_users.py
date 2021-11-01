import json
from csv import DictReader

with open("initial_files/users.json", "r") as f:
    users = json.loads(f.read())

with open("initial_files/books.csv", "r") as f:
    books = []
    reader = DictReader(f)
    for row in reader:
        books.append(row)


def slice_list(input_list, size):
    input_size = len(input_list)
    slice_size = input_size // len(size)
    remain = input_size % len(size)
    result = []
    iterator = iter(input_list)
    for i in range(len(size)):
        result.append([])
        for j in range(slice_size):
            result[i].append(iterator.__next__())
        if remain:
            result[i].append(iterator.__next__())
            remain -= 1
    return result


books_for_users = []

for user in users:
    books_for_users.append(
        {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': slice_list(books, users)[users.index(user)]
        }
    )

with open("result.json", "w") as f:
    s = json.dumps(books_for_users, indent=4)
    f.write(s)
#
