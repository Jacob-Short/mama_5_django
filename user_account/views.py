from django.shortcuts import redirect, render, reverse
from django.views.generic import View, CreateView

# models
from user_account.models import User

# forms
from user_account.forms import RegisterForm, LoginForm, EditUserForm

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
                email=data.get("email"),
                password=data.get("password"),
            )

            try:
                messages.add_message(request, messages.SUCCESS, f"Login Successful")
                login(request, user)
                return redirect(reverse("home"))
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
                request, email=data.get("email"), password=data.get("password")
            )
            if logged_in_user is not None:
                login(request, logged_in_user)
                messages.add_message(
                    request,
                    message="You have successfully logged in.",
                    level=messages.SUCCESS,
                )
                return redirect(reverse("home"))
            else:
                messages.add_message(
                    request,
                    message="Credentials Invalid",
                    level=messages.ERROR,
                )
                return redirect(reverse("login"))

        else:
            messages.add_message(
                request, message="Invalid credentials.", level=messages.ERROR
            )
            return redirect("login")


def logout_view(request):
    logout(request)
    messages.add_message(
        request, message="You have sucessfully logged out.", level=messages.SUCCESS
    )
    return redirect("/")


class UserView(View):
    """each users profile"""

    def get(self, request, id):

        signed_in_user = request.user
        target_user = User.objects.get(id=id)

        print(f"Picture: {target_user.picture}")

        template = "profile.html"

        context = {"signed_in_user": signed_in_user, "target_user": target_user}
        # breakpoint()
        return render(request, template, context)

    def post(self, request):
        ...


class EditUserView(View):
    """can edit your profile"""

    def get(self, request, id):

        template = "generic_form.html"
        signed_in_user = request.user
        profile_user = User.objects.get(id=id)
        form = EditUserForm(
            initial={
                "first_name": profile_user.first_name,
                "last_name": profile_user.last_name,
                "email": profile_user.email,
                "picture": profile_user.picture,
                "bio": profile_user.bio,
            }
        )
        context = {
            "signed_in_user": signed_in_user,
            "form": form,
            "profile_user": profile_user,
        }
        return render(request, template, context)

    def post(self, request, id):

        profile_id = request.user.id
        profile_user = User.objects.get(id=id)
        form = EditUserForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                data = form.cleaned_data
                profile_user.first_name = data["first_name"]
                profile_user.last_name = data["last_name"]
                profile_user.email = data["email"]
                profile_user.picture = data["picture"]
                profile_user.bio = data["bio"]
                profile_user.password = data["password"]
                profile_user.save()
                messages.add_message(
                    request,
                    message="You have sucessfully edited your profile.",
                    level=messages.SUCCESS,
                )
                return redirect(reverse("profile", args=(id,)))
        except Exception as err:
            print(err)
            messages.add_message(
                request,
                message="There was an error editing your profile.",
                level=messages.ERROR,
            )
            return redirect(reverse("profile", args=(id,)))


def about(request):
    template = "about.html"
    signed_in_user = request.user
    context = {"signed_in_user": signed_in_user}
    return render(request, template, context)
