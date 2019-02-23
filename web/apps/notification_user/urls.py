from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from apps.notification_user import views

urlpatterns = [
    # url(r'^products$', views.ProductList.as_view(), name='product.py-list'),
    url(r'^connections/add', views.AddConnectionView.as_view(), name='add_connections'),
    url(r'^connections/remove', views.RemoveConnectionView.as_view(), name='remove_connections'),
 ]

urlpatterns = format_suffix_patterns(urlpatterns)