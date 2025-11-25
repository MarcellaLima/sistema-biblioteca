from datetime import date, timedelta

users = []
books = []
loans = []  

def next_id(coll):
    return len(coll) + 1

def add_user(name, contact, user_type='Aluno'):
    user = {'id': next_id(users), 'name': name, 'contact': contact, 'type': user_type, 'fines': 0.0}
    users.append(user)
    return user

def get_user(user_id):
    return next((u for u in users if u['id']==user_id), None)

def add_book(title, author, year, genre, copies=1):
    book = {'id': next_id(books), 'title': title, 'author': author, 'year': year, 'genre': genre, 'copies_total': copies, 'copies_available': copies}
    books.append(book)
    return book

def search_books(q):
    q_low = q.lower()
    return [b for b in books if q_low in b['title'].lower() or q_low in b['author'].lower() or q_low in b['genre'].lower()]

def get_book(book_id):
    return next((b for b in books if b['id']==book_id), None)

def borrow_book(user_id, book_id, days=14):
    user = get_user(user_id); book = get_book(book_id)
    if not user or not book: 
        raise ValueError('Usuário ou livro não encontrado')
    if book['copies_available'] <= 0:
        return None  
    due = date.today() + timedelta(days=days)
    loan = {'loan_id': next_id(loans), 'user_id': user_id, 'book_id': book_id, 'due_date': due, 'returned_date': None}
    loans.append(loan)
    book['copies_available'] -= 1
    return loan

def return_book(loan_id, return_date=None):
    return_date = return_date or date.today()
    loan = next((l for l in loans if l['loan_id']==loan_id), None)
    if not loan:
        raise ValueError('Empréstimo não encontrado')
    if loan['returned_date'] is not None:
        raise ValueError('Livro já devolvido')
    loan['returned_date'] = return_date
    book = get_book(loan['book_id'])
    book['copies_available'] += 1

    overdue_days = (return_date - loan['due_date']).days
    if overdue_days > 0:
        fine = overdue_days * 1.0
        user = get_user(loan['user_id'])
        user['fines'] += fine
        return fine
    return 0.0

def pay_fine(user_id, amount):
    user = get_user(user_id)
    if not user:
        raise ValueError('Usuário não encontrado')
    paid = min(user['fines'], amount)
    user['fines'] -= paid
    return paid

def seed_sample_data():
    users.clear(); books.clear(); loans.clear()
    add_user("Marcella L. Azevedo", "marcella@gmail.com", "Aluno")
    add_user("João V. Cruz", "joao@gmail.com", "Bibliotecário")
    add_book("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, "Fantasia", copies=2)
    add_book("As Crônicas de Nárnia – O Leão, a Feiticeira e o Guarda-roupa", "C.S. Lewis", 1950, "Fantasia", copies=2)
    add_book("O Hobbit", "J.R.R. Tolkien", 1937, "Fantasia", copies=1)
    add_book("Jogos Vorazes", "Suzanne Collins", 2008, "Distopia", copies=2)
    add_book("Percy Jackson e o Ladrão de Raios", "Rick Riordan", 2005, "Aventura", copies=2)
