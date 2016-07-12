from django import forms
from dispPoc.models import Text

class TextForm(forms.ModelForm):
    head = forms.CharField(widget=forms.Textarea(attrs={'cols':70, 'rows': 40}),help_text='header')
    body = forms.CharField(widget=forms.Textarea(attrs={'cols':70, 'rows': 40}),help_text='body')
    filePaths = forms.CharField(widget=forms.Textarea(attrs={'cols':70, 'rows': 40}),help_text='File Paths')
    class Meta:
        model=Text;
        fields=('head','body','filePaths')
