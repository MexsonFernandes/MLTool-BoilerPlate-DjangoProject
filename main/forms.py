from django import forms
from . import models


# model form has been used
class getFileForm(forms.ModelForm):
    class Meta:
        model = models.PeptideStructureData
        fields = ['email', 'sequence', 'file']
