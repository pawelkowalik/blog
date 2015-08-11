from django import forms

from . import models


class AddNoteForm(forms.ModelForm):

    class Meta:
        model = models.NoteToPost
        fields = ['post_id', 'text', 'author']
