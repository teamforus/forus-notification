# import django
# from django.http import JsonResponse
#
# from apps.core.sign_utils import SignUtil
#
#
# class AuthAppMiddleware(django.utils.deprecation.MiddlewareMixin):
#     def process_request(self, request):
#         if request.POST:
#             sign_util = SignUtil('dwadwadwa')
#             sign = ''
#             data = dict()
#             for item in request.POST:
#                 if item.lower() != 'sign':
#                     data[item] = request.POST.get(item)
#                 else:
#                     sign = request.POST.get(item)
#
#             hash_value = sign_util.create_hash(data)
#
#             if sign != hash_value:
#                 return JsonResponse({'auth_error': 'Autherror'}, status=401)