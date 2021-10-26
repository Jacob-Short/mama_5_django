from django.shortcuts import redirect, render, reverse
from django.views.generic import View, CreateView

from user_account.models import User

class TranontIndexView(View):
    '''tranont home page'''

    def get(self, request):
        template = 'tranont_index.html'

        signed_in_user = request.user
        target_user = User.objects.get(id=signed_in_user.id)

        context = {'signed_in_user': signed_in_user}
        return render(request, template, context)

    def post(self, request):
        ...
