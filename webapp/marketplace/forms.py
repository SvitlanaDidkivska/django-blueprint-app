from .models import Posts
from django.forms import ModelForm, TextInput, DateInput, Textarea


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'excerpt', 'body', 'published_at']

        # Blok widgets zajmuje się definicją pól w HTML. Tutaj można definiować typy wyświetlanych pół oraz zarządzać ich atrybutami.
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'excerpt': TextInput(attrs={'class': 'form-control', 'placeholder': 'Excerpt'}),
            'body': Textarea(attrs={'class': 'form-control', 'placeholder': 'Post body'}),
            'published_at': DateInput(attrs={'class': 'form-control', 'type':'date'}),
        }
