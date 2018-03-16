#from django.core.urlresolvers import reverse
from django.urls import reverse

from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class LandingPage(TemplateView, LoginRequiredMixin):
    template_name = 'landing.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'landing.html'
    
    def get(self, request, *args, **kwargs):

        if request.user.has_perm('accounts.tutor_participant') or request.user.has_perm('accounts.is_tutor_admin') :
            return HttpResponseRedirect(reverse("tutor:dashboard"))
            # elif request.user.has_perm('accounts.bible_study_participant') or request.user.has_perm('accounts.is_bible_study_admin') :
            # 	return return HttpResponseRedirect(reverse("tutor:dashboard"))
        else :
            return super().get(request, *args, **kwargs)

class ThanksPage(TemplateView):
	template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("landing"))
        return super().get(request, *args, **kwargs)
    	

