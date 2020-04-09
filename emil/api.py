# import json
# import inspect
#
# from django.views import View
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.http.response import JsonResponse
# from django.utils.decorators import method_decorator
# from django.http import HttpResponse, HttpResponseBadRequest
# from django.contrib.auth.decorators import login_required, permission_required
# from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
#
# from emil import forms as emil_forms
# from emil import models as emil_models
#
# from django.contrib.auth import get_user_model
# User = get_user_model()
#
#
# extended_perms = [
#     login_required,
#     user_passes_test(lambda u: u.is_superuser, login_url='forbidden'),
# ]
#
# @method_decorator(extended_perms, name='dispatch')
# class ExtendedAPI(View):
#     related_delimiter = '.'
#     delimiter = ','
#     k_v_delimiter = ':'
#     model = None
#
#     # e.g. /transactions/?filter=user__gt:1,cost__lt:0
#     def filter(self, request, queryset):
#         if not request.GET.get('filter'): return queryset
#
#         raw_filters = request.GET.get('filter').split(self.delimiter)
#         filters = []
#
#         for raw_f in raw_filters:
#             k, v = raw_f.split(self.k_v_delimiter)[0], raw_f.split(self.k_v_delimiter)[1]
#             filters.append({k: v})
#
#         for filter in filters:
#             queryset = queryset.filter(**filter)
#
#         return queryset
#
#     # e.g. /transactions/?order_by=user__id,cost
#     def order_by(self, request, queryset):
#         if not request.GET.get('order_by'): return queryset
#         ordering = request.GET.get('order_by').split(self.delimiter)
#         return queryset.order_by(*ordering)
#
#     # e.g. /transactions/?order_by=user__id|cost
#     def fields(self, request, queryset):
#         if not request.GET.get('fields'):
#             return [ {k:v for (k,v) in t.__dict__.items() if not k.startswith('_') } for t in queryset ]
#
#         fields = request.GET.get('fields').split(self.delimiter)
#         return [ {k:v for (k,v) in t.__dict__.items() if k in fields } for t in queryset ]
#
#
#     # Risky. Calling methods is not good
#     def special_fields(self, request, queryset):
#         if not request.GET.get('fields'):
#             return [ {k:v for (k,v) in t.__dict__.items() if not k.startswith('_') } for t in queryset ]
#
#         fields = request.GET.get('fields').split(self.delimiter)
#
#         data = []
#         for t in queryset:
#             r = {}
#             for f in fields:
#                 current = t
#                 for related in f.split(self.related_delimiter): # self.account.user. etc
#                     current = getattr(current, related)
#
#                 # WARNING
#                 # if inspect.ismethod(current):
#                 #     current = current()
#
#                 r[f] = current
#
#             data.append(r)
#         return data
#
#     def parsed(self, request):
#         try:
#             queryset = self.model.objects.all()
#             queryset = self.filter(request, queryset)
#             queryset = self.order_by(request, queryset)
#             queryset = self.limit(request, queryset)
#             return queryset
#         except Exception as e:
#             print(e)
#             return HttpResponseBadRequest()
#
#     def limit(self, request, queryset):
#         n = request.GET.get('from')
#         m = request.GET.get('to')
#         if n: n = int(n)
#         if m: m = int(m)
#         return queryset[n:m]
#
#
#     def get(self, request):
#         queryset = self.parsed(request)
#         data = self.special_fields(request, queryset)
#         return JsonResponse(data, safe=False, json_dumps_params={'indent': 3}) # safe=False allows other types than dict
#
#     # TODO: Implement
#     def delete(self, request):
#         pass
