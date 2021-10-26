from django.shortcuts import redirect, render, reverse, HttpResponseRedirect
from .models import Message
from user_account.models import User
from user_message.forms import CreateMessageForm
from django.views.generic import View


from django.contrib import messages



def get_messages_count(logged_in_user):
    signed_in_user = logged_in_user
    user_messages = Message.objects.filter(recipient=signed_in_user)

    messages_count = len(user_messages)
    return messages_count

class CreateMessageView(View):
    '''send a message to another user'''

    def get(self, request, id):

        template = "generic_form.html"
        signed_in_user = request.user
        form = CreateMessageForm(request.POST)
        context = {'form': form, 'signed_in_user': signed_in_user, 'header': 'messages'}
    
        return render(request,template, context)

    def post(self, request, id):
        form = CreateMessageForm(request.POST)
        recipient = User.objects.get(id=id)
        if form.is_valid():
            data = form.cleaned_data
            message = Message.objects.create(
                message=data["message"], author=request.user, recipient=recipient
            )
            messages.add_message(
                request, message="Message sent.", level=messages.SUCCESS
            )
            return redirect(reverse("profile", args=(id,)))


class AllMessages(View):
    '''can view all messages'''

    def get(self, request, id):

        template = 'all_messages.html'
        signed_in_user = User.objects.get(id=id)
        user_messages = Message.objects.filter(recipient=signed_in_user)

        context = {
            "user_messages": user_messages,
            "signed_in_user": signed_in_user
        }
        return render(request, template, context)

    def post(self, request):
        ...


def delete_message(request, id):
    message = Message.objects.get(id=id)
    signed_in_user_id = request.user.id
    message.delete()
    messages.add_message(
                request, message="Message deleted.", level=messages.ERROR
            )
    return redirect(reverse("usermessages", args=(signed_in_user_id,)))