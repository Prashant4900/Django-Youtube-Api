from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, get_user_model, login, logout


# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'error': 'Invalid email or password'})
        except Exception as e:
            return render(request, 'login.html', {'error': e})


class RegisterView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        try:
            user = get_user_model().objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            login(request, user)
            return redirect('/')
        except Exception as e:
            return render(request, 'signup.html', {'error': e})


def logout_view(request):
    logout(request)
    return redirect('/')
