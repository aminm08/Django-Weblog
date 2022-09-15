from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import CustomUserChangeForm


def profile_view(request):
    form = CustomUserChangeForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, _('Your profile updated successfully'))
        return redirect('profile')

    return render(request, 'account/profile.html', {'form': form})
