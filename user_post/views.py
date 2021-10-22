from django.shortcuts import render, redirect
from django.views.generic import View
from user_post.models import UserPost
from user_post.forms import CreateUserPostForm

from user_account.models import UserAccount


from django.contrib import messages


class CreateUserPostView(View):
    """can create a post on a game in db"""

    def get(self, request, id):
        template = "generic_form.html"
        signed_in_user = request.user

        form = CreateUserPostForm()
        context = {
            "form": form,
            "signed_in_user": signed_in_user,
        }
        return render(request, template, context)

    def post(self, request, id):
        form = CreateUserPostForm(request.POST)
        signed_in_user = request.user

        if form.is_valid():
            data = form.cleaned_data
            review = UserPost.objects.create(
                title=data["name"],
                text=data["text"],
                user_created=signed_in_user,
            )
            messages.add_message(
                request, message="Post created.", level=messages.SUCCESS
            )
            return redirect("home")


class AllPostsView(View):
    """displays all posts"""

    def get(self, request):

        signed_in_user = request.user

        reviews = UserPost.objects.all()

        template = "all_reviews.html"
        context = {"reviews": reviews, "signed_in_user": signed_in_user}
        return render(request, template, context)

    def post(self, request):
        ...


class PostDetailView(View):
    def get(self, request, id):


        template = "post_detail.html"
        signed_in_user = request.user
        post = UserPost.objects.get(id=id)


        context = {
            "post": post,
            "signed_in_user": signed_in_user,
        }

        return render(request, template, context)

    def post(self, request):
        ...



def delete_post(request, id):
    post = UserPost.objects.get(id=id)
    post.delete()
    messages.add_message(request, message="Review deleted.", level=messages.ERROR)
    return redirect("home")
