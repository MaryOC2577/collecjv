from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = "base.html"


class CguView(TemplateView):
    template_name = "legalpage.html"


class ContactView(TemplateView):
    template_name = "contact.html"
