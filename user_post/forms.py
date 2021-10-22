from django import forms


class CreateUserPostForm(forms.Form):

    title = forms.CharField(max_length=150)
    post = forms.CharField(widget=forms.Textarea)