from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^user/$', CreateView.as_view(
        # template_name='registration/register.html',
        # form_class=UserCreationForm,
        # success_url='/accounts/register/done'
    # )),
    # url(r'^done/$', TemplateView.as_view(template_name='registration/register_done.html')),
]
