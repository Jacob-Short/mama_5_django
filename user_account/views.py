from django.shortcuts import redirect, render, reverse
from django.views.generic import View, CreateView

# models
from user_account.models import User, Profile

# forms
from user_account.forms import (
    RegisterForm,
    LoginForm,
    CreateProfileForm,
)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class IndexView(View):
    """index page upon coming to site"""

    def get(self, request):

        signed_in_user = request.user
        template = "index.html"
        context = {"signed_in_user": signed_in_user}
        return render(request, template, context)

    def post(self, request):
        ...


class HomeView(View, LoginRequiredMixin):
    """index page upon coming to site"""

    def get(self, request):

        signed_in_user = request.user
        template = "home.html"
        context = {"signed_in_user": signed_in_user}
        return render(request, template, context)

    def post(self, request):
        ...


# class RegisterView(CreateView):
#     form_class = RegisterForm
#     template_name = 'generic_form.html'
#     success_url = '/login/'


class RegisterView(View):
    def get(self, request):

        signed_in_user = request.user
        template_name = "generic_form.html"
        form = RegisterForm()
        context = {"signed_in_user": signed_in_user, "form": form, "header": "sign-up"}

        return render(request, template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
            )

            try:
                messages.add_message(request, messages.SUCCESS, f"Login Successful")
                login(request, user)
                return redirect("createprofile")
            except Exception as ex:
                messages.add_message(request, messages.ERROR, f"Login Invalid")
                print("Something went wrong….", ex)
                return redirect(reverse("login"))


class LoginView(View):
    def get(self, request):

        signed_in_user = request.user
        template_name = "generic_form.html"
        form = LoginForm()
        context = {"form": form, "header": "Login", "signed_in_user": signed_in_user}
        return render(request, template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            logged_in_user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if logged_in_user:
                login(request, logged_in_user)
                messages.add_message(
                    request,
                    message="You have successfully logged in.",
                    level=messages.SUCCESS,
                )
                return redirect(reverse("home"))
            if logged_in_user is not None:
                login(request, logged_in_user)
                return redirect(reverse("generic_form.html"))
        else:
            messages.add_message(
                request,
                message="Credentials Invalid",
                level=messages.ERROR,
            )
            return redirect(reverse("login"))


def logout_view(request):
    logout(request)
    messages.add_message(
        request, message="You have sucessfully logged out.", level=messages.INFO
    )
    return redirect("/")


class UserView(View):
    """each users profile"""

    def get(self, request, id):

        signed_in_user = request.user
        target_user = User.objects.get(id=id)

        try:
            profile = Profile.objects.get(user=target_user)
        except Exception as err:
            print(err)
            profile = None
        # print(f"Picture: {target_user.profile_picture}")

        template = "profile.html"

        # breakpoint()
        context = {
            "signed_in_user": signed_in_user,
            "target_user": target_user,
            "profile": profile,
        }
        return render(request, template, context)

    def post(self, request):
        ...


class CreateProfileView(View):
    """create a profile upon signing up"""

    def get(self, request):

        target_user = User.objects.get(id=request.user.id)

        form = CreateProfileForm()
        template = "generic_form.html"
        context = {"form": form}
        return render(request, template, context)

    def post(self, request):

        target_user = User.objects.get(id=request.user.id)

        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile = Profile.objects.create(
                user=target_user,
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                # profile_picture=data["profile_picture"],
                bio=data["bio"],
            )
            return redirect('home')


# class EditProfileView(View):
#     """can edit your profile"""

#     def get(self, request, id):

#         template = "generic_form.html"
#         signed_in_user = request.user
#         try:
#             profile_user = Profile.objects.get(user=signed_in_user)
#             form = UserProfileEditForm(
#                 initial={
#                     "first_name": profile_user.first_name,
#                     "last_name": profile_user.last_name,
#                     "email": profile_user.email,
#                     "profile_picture": profile_user.profile_picture,
#                     "bio": profile_user.bio,
#                 }
#             )
#         except Exception as err:
#             print(err)
#             messages.add_message(
#                 request,
#                 message="You do not have a profile yet",
#                 level=messages.ERROR,
#             )
#             return redirect(reverse("profile", args=(id,)))
#         context = {
#             "signed_in_user": signed_in_user,
#             "form": form,
#             "profile_user": profile_user,
#         }
#         return render(request, template, context)

#     def post(self, request, id):

#         profile_user = User.objects.get(id=id)
#         form = UserProfileEditForm(request.POST, request.FILES)
#         try:
#             if form.is_valid():
#                 data = form.cleaned_data
#                 profile_user.first_name = data["first_name"]
#                 profile_user.last_name = data["last_name"]
#                 profile_user.email = data["email"]
#                 profile_user.profile_picture = data["profile_picture"]
#                 profile_user.bio = data["bio"]
#                 profile_user.password = data["password"]
#                 profile_user.save()
#                 messages.add_message(
#                     request,
#                     message="You have sucessful target_user.profile_picturely edited your profile.",
#                     level=messages.SUCCESS,
#                 )
#                 return redirect(reverse("profile", args=(id,)))
#         except Exception as err:
#             print(err)
#             messages.add_message(
#                 request,
#                 message="There was an error editing your profile.",
#                 level=messages.ERROR,
#             )
#             return redirect(reverse("profile", args=(id,)))


def about(request):
    template = "about.html"
    signed_in_user = request.user
    context = {"signed_in_user": signed_in_user}
    return render(request, template, context)
