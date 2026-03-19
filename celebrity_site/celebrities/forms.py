from django import forms

from celebrities.models import Category, Tag
class CreateCelebForm(forms.Form):
    name = forms.CharField()
    bio = forms.CharField()
    birth_date  = forms.CharField()
    image = forms.ImageField()
    content = forms.CharField()

    def clean(self):
        data = self.cleaned_data 
        if data.get("name") == data.get("bio"):
            raise forms.ValidationError("Title and author must be different")
        return data 

    def clean_neme(self):
        data = self.cleaned_data.get("name")
        if data == "name":
            raise forms.ValidationError("Title must be different")
        return data
    
    def clean_bio(self):
        data = self.cleaned_data.get("bio")
        if data == "bio":
            raise forms.ValidationError("Author must be different")
        return data
    

class SearchForm(forms.Form):
  
    search = forms.CharField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False) # динамичный одиночные выбор
    # author = forms.ChoiceField(choices=author_choice, required=False) # статичный одиночные выбор
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False) # динамичный множественный выбор
    # example = forms.MultipleChoiceField(choices=author_choice, required=False)