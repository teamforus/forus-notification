# from django.core.exceptions import PermissionDenied
# from django.http import HttpResponse
# from rest_framework import generics, status
# from rest_framework.response import Response
#
# from apps.core.models import App
# from apps.core.sign_utils import SignUtil
#
#
# def get_error(message):
#     return HttpResponse(message, "application/json")
#
# def sign_request(function):
#     def wrap(request, *args, **kwargs):
#         # if request.POST:
#         #     public_key = request.POST.get('public_key', None)
#         #     if not public_key:
#         #         return get_error('Public key is empty')
#         #     sign = ''
#         #
#         #     try:
#         #         app = App.objects.get(public_key=public_key)
#         #     except:
#         #         return get_error('Public key not found')
#         #
#         #     sign_util = SignUtil(app.secrete_key)
#         #     data = dict()
#         #     for item in request.POST:
#         #         if item.lower() == 'csrfmiddlewaretoken':
#         #             continue
#         #         if item.lower() != 'sign':
#         #             data[item] = request.POST.get(item)
#         #         else:
#         #             sign = request.POST.get(item)
#         #
#         #     hash_value = sign_util.create_hash(data)
#         #     print(hash_value)
#         #     if sign != hash_value:
#         #         return get_error('Sign is not correct')
#
#         return function(request, *args, **kwargs)
#
#
#
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap
