from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookForm

# Тимчасове сховище в пам'яті (імітація БД з Модуля 2)
BOOKS_DB = [
    {'title': "1984", 'author': "Джордж Орвелл", 'genre': "Художня література", 'description': "Роман-антиутопія."},
    {'title': "Чистий Код", 'author': "Роберт Мартін", 'genre': "Технічна література", 'description': "Посібник з написання якісного коду."}
]

def home(request):
    context = {
        'page_title': "Головна сторінка",
        'books_count': len(BOOKS_DB),
        'books': BOOKS_DB
    }
    return render(request, 'home.html', context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Зберігаємо дані в нашу імпровізовану БД
            BOOKS_DB.append(form.cleaned_data)
            messages.success(request, f"Книгу '{form.cleaned_data['title']}' успішно додано до каталогу!")
            return redirect('home')
    else:
        form = BookForm()
        
    return render(request, 'add_book.html', {'form': form})
