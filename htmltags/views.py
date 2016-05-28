from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView


from htmltags.models import Tags
from django.core.urlresolvers import reverse


class ListTagsView(ListView):
    model = Tags
    template_name = 'tags_list.html'


class CreateTagView(CreateView):

    model = Tags
    template_name = 'edit_tag.html'

    def get_success_url(self):
        return reverse('tags-list')

    def get_context_data(self, **kwargs):
        context = super(CreateTagView, self).get_context_data(**kwargs)
        context['action'] = reverse('tags-new')


        return context

class UpdateTagsView(UpdateView):

    model = Tags
    template_name = 'edit_tag.html'

    def get_success_url(self):
        return reverse('tags-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateTagsView, self).get_context_data(**kwargs)
        context['action'] = reverse('tag-edit',
                                    kwargs={'pk': self.get_object().id})
        context['tag'] = self.get_object()

        return context

class DeleteTagView(DeleteView):

    model = Tags
    template_name = 'delete_tag.html'


    def get_success_url(self):
        return reverse('tags-list')

    def get_context_data(self, **kwargs):
        context = super(DeleteTagView, self).get_context_data(**kwargs)
        context['tag'] = self.get_object()

        return context


class MainTagsView(ListView):

    model = Tags
    template_name = 'main_tag.html'

    def get_context_data(self, **kwargs):
        context = super(MainTagsView, self).get_context_data(**kwargs)
        context['object_list'] = self.get_queryset()
        context['active_tag'] = context['object_list'] and context['object_list'][0] or None

        return context


class MainDetailsTagsView(DetailView):
    model = Tags
    template_name = 'main_tag.html'

    def get_context_data(self, **kwargs):
        context = super(MainDetailsTagsView, self).get_context_data(**kwargs)
        context['object_list'] = self.get_queryset()
        context['active_tag'] = self.get_object()

        return context
