from django.shortcuts import render
from django.views import generic
from news import models
from django.shortcuts import render
from django import forms



class NewsList(generic.ListView):
    model = models.News
    paginate_by = 10
    context_object_name = 'news_list'
    queryset = models.News.objects.order_by('-posted_date', 'title')

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context['all_news'] = models.News.objects.order_by('-posted_date', 'title')
        context['all_notes'] = models.NoteToPost.objects.order_by('posted_date')

        return context

news_list = NewsList.as_view()

class AddNoteForm(forms.ModelForm):
    class Meta:
        model=models.NoteToPost
        fields = ['post_id', 'text', 'author']


def add_note(request):
    form = AddNoteForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'add_comment.html', {'form': form.as_p()})

class NewsDetailView(generic.DetailView):
    model = models.News

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['all_news'] = models.News.objects.order_by('-posted_date', 'title')
        context['all_notes'] = models.NoteToPost.objects.order_by('posted_date')
        context['form'] = AddNoteForm()
        return context



news_detail = NewsDetailView.as_view()




