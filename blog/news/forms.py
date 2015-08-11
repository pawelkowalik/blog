
class AddNoteForm(forms.ModelForm):
    class Meta:
        model=models.NoteToPost
        fields = ['post_id', 'text', 'author']
