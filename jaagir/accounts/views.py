from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from blog.models import Post

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # inactive_user = send_verification_email(request, form)
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form':form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance= request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')


    else:
        u_form = UserUpdateForm(instance= request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {'u_form' : u_form, 'p_form' : p_form, 'user_post': Post.objects.filter(author=request.user)}
    return render(request, 'accounts/profile.html', context)
