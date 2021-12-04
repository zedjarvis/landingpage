from django.urls import path
from . import views as mainView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', mainView.index, name='index'),
    path('contact/', mainView.ContactForm.as_view(), name='contact'),
]
