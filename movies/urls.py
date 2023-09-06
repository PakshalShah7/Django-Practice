from django.urls import path
from .views import base_page, home_page, submit_page, MoviesListView, \
    MoviesUpdateView, PersonCreateView, MoviesCreateView, MoviesDeleteView, \
    upload_form, MovieDetailView, MovieDetailForm, MovieTemplateView, \
    MovieRedirectView, MovieArchiveView, set_session, upload_formset, MovieFormset, send_email_message

app_name = 'movies'
urlpatterns = [
    path('base/', base_page, name='base_page'),
    path('home/', home_page, name='home_page'),
    path('submit/', submit_page, name='submit_page'),
    path('person-form/', PersonCreateView.as_view(), name='person_form'),
    path('movies-form/', MoviesCreateView.as_view(), name='movies_create'),
    path('', MoviesListView.as_view(), name='movies_list'),
    path('delete/<int:pk>/', MoviesDeleteView.as_view(), name='movies_delete'),
    path('update/<int:pk>/', MoviesUpdateView.as_view(), name='movies_update'),
    path('movie-detail/<slug:slug>/', MovieDetailView.as_view(), name='movies_detail_slug'),
    path('movie-detail/<int:pk>/', MovieDetailView.as_view(), name='movies_detail_int'),
    path('form/', upload_form, name='form'),
    path('forms/', MovieDetailForm.as_view(), name='movies_form_view'),
    path('template/', MovieTemplateView.as_view(), name='movies_template_view'),
    path('redirect/', MovieRedirectView.as_view(), name='movies_redirect_view'),
    path('archive/', MovieArchiveView.as_view(), name='movies_archive'),
    path('set/', set_session, name='set_session'),
    path('formset/', upload_formset, name='formset'),
    path('form-set/', MovieFormset.as_view(), name='form-set'),
    path('email/', send_email_message, name='send_email'),
]
