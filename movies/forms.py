from django import forms
from django.forms import modelformset_factory
from .models import Movie, Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"

    # def clean(self):
    #     if self.cleaned_data['person_name'].name == self.cleaned_data['title']:
    #         raise ValidationError('Person name and movie title should not be same')

    # def clean(self):
    #     title = self.cleaned_data['title']
    #     if Person.objects.filter(name=title).exists():
    #         raise ValidationError('Person name and movie title should not be same')
    #     return self.cleaned_data

    def clean(self):
        if Movie.objects.filter(title=self.cleaned_data['title']).exists():
            raise forms.ValidationError('One person cannot create two same title')
        return self.cleaned_data


movies_formset = modelformset_factory(Movie, form=MoviesForm, extra=2, can_delete=True)
# movies_inline_formset = inlineformset_factory(Movie, Person,)
