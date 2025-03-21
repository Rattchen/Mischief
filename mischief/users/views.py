from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import User

class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        self.create_profiles(user)
        return super().form_valid(form)

    def create_profiles(self, user):
        if 'core' in settings.INSTALLED_APPS:
            print("Let's start some Mischief!") # Doesn't have its own Profile yet, but will have in the future
        if 'squeak' in settings.INSTALLED_APPS:
            print("Squeak!") # Doesn't have its own Profile yet, but will have in the future
        if 'nibble' in settings.INSTALLED_APPS:
            from nibble.models import NibbleProfile
            nibbleProfile = NibbleProfile.objects.create(user=user, handle=user.username)
            if 'scuffle' in settings.INSTALLED_APPS:
                from scuffle.models import ScuffleProfile
                ScuffleProfile.objects.create(nibbleProfile=nibbleProfile)
