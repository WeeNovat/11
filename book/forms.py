from django import forms
from django.core.exceptions import ValidationError

class BookForm(forms.Form):
    GENRE_CHOICES = [
        ('fiction', 'Художня література'),
        ('tech', 'Технічна література'),
        ('sci-fi', 'Наукова фантастика'),
    ]
    
    title = forms.CharField(max_length=150, label="Назва книги")
    author = forms.CharField(max_length=100, label="Автор")
    genre = forms.ChoiceField(choices=GENRE_CHOICES, label="Жанр книги")
    description = forms.CharField(widget=forms.Textarea, label="Опис / Анотація")

    # Кастомна валідація бізнес-правила
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title.split()) < 2:
            raise ValidationError("Назва книги повинна містити щонайменше два слова!")
        return title
