from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello from core module!'
        return context