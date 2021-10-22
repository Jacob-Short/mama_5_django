from django.shortcuts import render
from django.views.generic import View

class IndexView(View):
    '''index page upon coming to site'''
    def get(self, request):

        signed_in_user = request.user
        template = 'index.html'
        context = {'signed_in_user': signed_in_user}
        return render(request, template, context)


    def post(self, request):
        ...
