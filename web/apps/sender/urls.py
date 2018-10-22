from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from apps.sender import views

urlpatterns = [

    url(r'^mobile/push', views.PushNotificationView.as_view(), name='mobile-send-push'),
    # url(r'^products$', views.ProductList.as_view(), name='product.py-list'),
    url(r'^vouchers/new_fund$', views.NewFund.as_view(), name='new-fund-email'),
    url(r'^vouchers/new_fund_created$', views.NewFundCreated.as_view(), name='new-fund-created-email'),
    url(r'^vouchers/provider_approved', views.ProviderApprovedView.as_view(), name='provider-approved-email'),
    url(r'^vouchers/provider_applied', views.ProviderAppliedView.as_view(), name='provider-applied-email'),
    url(r'^vouchers/new_product_added', views.NewProductAddedView.as_view(), name='new-product-added-email'),
    url(r'^vouchers/provider_rejected', views.ProviderRejectedView.as_view(), name='provider-rejected-email'),

    url(r'^login/login_via_email', views.LoginViaEmail.as_view(), name='login-via-email'),


    url(r'^sponsors/you_added_as_validator', views.SponsorAddYouAsValidatorApi.as_view(), name='you-added-as-validator'),
    url(r'^validations/new_validation_request', views.NewValidationRequestApi.as_view(),
        name='new-validation-request'),

 ]

urlpatterns = format_suffix_patterns(urlpatterns)