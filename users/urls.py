from django.urls import path
from users.views import RegisterView, MainView, LoginUserView, LogoutUserView

app_name = 'users'

urlpatterns = [
	path('', MainView.as_view(), name='main_page'),
	path('register/', RegisterView.as_view(), name='register_user'),
	path('login/', LoginUserView.as_view(), name='login_user'),
	path('logout/', LogoutUserView.as_view(), name='logout_user')

]
