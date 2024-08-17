from django import forms


class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    active = forms.BooleanField()
    publish_date = forms.DateField()
