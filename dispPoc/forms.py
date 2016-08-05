from django import forms
from dispPoc.models import Text

class TextForm(forms.ModelForm):
    head = forms.CharField(widget=forms.Textarea(attrs={'cols':80, 'rows': 35}),help_text='Header')
    body = forms.CharField(widget=forms.Textarea(attrs={'cols':80, 'rows': 35}),help_text='Body')
    filePaths = forms.CharField(widget=forms.Textarea(attrs={'cols':80, 'rows': 35}),help_text='File Paths')
    class Meta:
        model=Text;
        fields=('head','body','filePaths')
