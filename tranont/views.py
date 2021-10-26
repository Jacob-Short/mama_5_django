from django.shortcuts import redirect, render, reverse
from django.views.generic import View, CreateView

class TranontIndexView(View):
    '''tranont home page'''

    def get(self, request):
        template = 'tranont_index.html'

        context = {}
        return render(request, template, context)

    def post(self, request):
        ...
