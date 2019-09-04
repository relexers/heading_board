from django.shortcuts import render
from .models import Bb, Rubric
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import BbForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    paginator = Paginator(bbs,5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'bbs': page.object_list, 'rubrics': rubrics, 'page': page}
    return render(request, 'newboard/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'newboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'newboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def add_and_save(request):
    if request.method == 'POST':
        bbf = BbForm(request.POST)
        if bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(reverse('newboard:by_rubric',
                    kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
        else:
            context = {'form':bbf}
            return render (request, 'newboard/create.html', context)
    else:
        bbf = BbForm()
        context = {'form':bbf}
        return render(request, 'newboard/create.html', context)


class BbDetailView(DetailView):
    model = Bb

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context



