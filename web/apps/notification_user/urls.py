from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from apps.notification_user import views

urlpatterns = [
    # url(r'^products$', views.ProductList.as_view(), name='product.py-list'),
    url(r'^connections/add/$', views.AddConnectionView.as_view(), name='add-connections'),
    url(r'^connections/add/$', views.AddConnectionView.as_view(), name='add-connections'),
 ]

urlpatterns = format_suffix_patterns(urlpatterns)