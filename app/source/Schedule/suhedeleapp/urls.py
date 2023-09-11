from django.urls import path
from .views import testView, signupView, formView, createView, loginView

app_name = 'suhedeleapp'
urlpatterns = [
    path("test/", testView, name='test'),
    path("signup/", signupView, name='signup'),
    path("form/", formView, name='form'),
    path("create/", createView, name='create'),
    path("login/", loginView, name='login'),
]