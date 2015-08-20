from django.core.urlresolvers import reverse
from django.http import Http404
from django.views import generic
from django.shortcuts import render

from .models import News, NoteToPost
from .forms import AddNoteForm


class NewsList(generic.ListView):
    model = News
    paginate_by = 10
    context_object_name = 'news_list'
    queryset = News.objects.order_by('-posted_date', 'title')

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context['all_news'] = News.objects.order_by('-posted_date', 'title')
        context['all_notes'] = NoteToPost.objects.order_by('posted_date')

        return context


def add_note(request):
    form = AddNoteForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'add_comment.html', {'form': form.as_p()})


class NewsDetailView(generic.FormView):
    form_class = AddNoteForm
    template_name = 'news/news_detail.html'

    def get_success_url(self):
        slug = self.kwargs['slug']
        url = reverse('news-detail', kwargs={'slug': slug})
        return url

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return self.render_to_response(
            self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = AddNoteForm(request.POST or None)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        slug = self.kwargs['slug']
        return self.render_to_response(
            self.get_context_data(form=form, slug=slug))

    def get_context_data(self, **kwargs):
        kwargs = super(NewsDetailView, self).get_context_data(**kwargs)
        kwargs.update({'news': self.get_news()})
        return kwargs

    def get_news(self):
        slug = self.kwargs['slug']
        news = News.objects.filter(slug=slug).first()
        if news:
            return news
        else:
            raise Http404()
