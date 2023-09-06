from django.core.mail import send_mail
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, \
    UpdateView, DetailView, FormView, RedirectView, TemplateView, ArchiveIndexView
from .forms import MoviesForm, PersonForm, movies_formset
from .models import Movie


def website_page(request):
    return render(request, 'website.html')


def home_page(request):
    return render(request, 'home.html')


def submit_page(request):
    return render(request, 'submit.html')


def base_page(request):
    return render(request, 'base.html')


class PersonCreateView(CreateView):
    template_name = 'form.html'
    form_class = PersonForm
    success_url = reverse_lazy('movies:submit_page')


class MoviesCreateView(CreateView):
    template_name = 'form.html'
    form_class = MoviesForm
    success_url = reverse_lazy('movies:submit_page')


class MoviesListView(ListView):
    model = Movie
    template_name = 'movies_list.html'
    queryset = Movie.objects.all()
    context_object_name = 'movies'


class MoviesDeleteView(DeleteView):
    model = Movie
    template_name = 'movies_confirm_delete.html'
    success_url = reverse_lazy("movies:submit_page")


class MoviesUpdateView(UpdateView):
    model = Movie
    fields = ['title', 'release_date', 'description']
    template_name = 'form.html'
    success_url = reverse_lazy("movies:submit_page")


def upload_form(request):
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'submit.html')
    else:
        form = MoviesForm()
        return render(request, 'form.html', {'form': form})


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies_detail.html'
    context_object_name = 'movie'


class MovieDetailForm(FormView):
    template_name = 'form.html'
    form_class = MoviesForm
    success_url = reverse_lazy("movies:submit_page")


class MovieTemplateView(TemplateView):
    template_name = 'movie_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Movie.objects.annotate(Count('title')).order_by('-title__count')[:5]
        return context


class MovieRedirectView(RedirectView):
    pattern_name = 'movies:home_page'


class MovieArchiveView(ArchiveIndexView):
    model = Movie
    template_name = 'movies_archive.html'
    queryset = Movie.objects.all()
    context_object_name = 'movies'
    date_field = 'release_date'
    allow_future = True


def set_session(request):
    request.session['name'] = 'Pakshal'
    return render(request, 'setsessions.html')


def form_set(request):
    # movies_formset = formset_factory(MoviesForm, extra=2)
    form = movies_formset()
    return render(request, 'submit.html', {'form': form})


def upload_formset(request):
    if request.method == 'POST':
        form = movies_formset(request.POST)
        if form.is_valid():
            print("Hi")
            print("Hi")
    else:
        form = movies_formset()
    return render(request, 'formset.html', {'formset': form})


class MovieFormset(TemplateView):
    template_name = 'formset.html'

    def get(self, request, *args, **kwargs):
        formset = movies_formset(queryset=Movie.objects.none())
        return self.render_to_response({'formset': formset})

    def post(self, request):
        formset = movies_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("movies:submit_page"))
        return self.render_to_response({'formset': formset})


def send_email_message(request):
    # email = EmailMessage('hello', 'this is body part', 'pakshal.shah@trootech.com', ['pakshal.shah1992@gmail.com'])
    # email.attach()
    send_mail('Email', 'Hello there!', 'pakshal.shah@trootech.com', ['pakshal.shah1992@gmail.com'], fail_silently=False)
    return render(request, 'submit.html')
