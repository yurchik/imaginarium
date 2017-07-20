from django import forms

from .models import Picture


class ImageForm(forms.ModelForm):
    img = forms.ImageField(required=True)
    desc = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Короткий опис картинки",
                "class": "form-control",
            },
        ),
    )

    class Meta:
        model = Picture
        fields = ['img', 'desc']
