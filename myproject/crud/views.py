from django.views.generic import TemplateView

# Create your views here.
class TopView(TemplateView):
    template_name = "top.html"