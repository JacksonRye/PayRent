from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404, reverse

from .forms import LoginForm, UserRegistrationForm
from .models import Profile, User
from houses.models import House
from django.views.generic import DetailView

def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:dashboard')

    else:
        user_form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': user_form})


@login_required
def dashboard(request):
    # return reverse('accounts:profile', args=[request.user.username])
    house_list = House.objects.all()
    return render(request,
                  'houses/list.html',
                  {'house_list': house_list}
                  )

class ProfileView(DetailView):

    model = User
    template_name = 'accounts/user/profile.html'
    context_object_name = 'user'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProfileView, self).get_context_data(*args, **kwargs)
    #     context['house'] = House.objects.filter()

