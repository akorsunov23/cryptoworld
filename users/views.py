from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from users.models import News


class MainView(ListView):
	"""Главная страница с выводом новостей о криптовалюте."""
	model = News
	template_name = 'users/main.html'
	paginate_by = 4
	context_object_name = 'news'


class LoginUserView(LoginView):
	"""Аутентификация пользователя"""
	template_name = 'users/login.html'


class LogoutUserView(LogoutView):
	"""Выход из аккаунта пользователя"""
	template_name = 'users/logout.html'


class RegisterView(CreateView):
	"""
	Регистрация пользователя. При методе POST, функция сохраняет полученные данные в стандартной модели User.
	:return: После регистрации, пользователь аутентифицируется и переадресовывается на главную страницу.
	"""
	template_name = 'users/register.html'
	form_class = UserCreationForm

	def get_queryset(self):
		return User.objects.all()

	def form_valid(self, form):
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(self.request, user)
		return redirect('/')
