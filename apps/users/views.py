from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, logout, login
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .serializers import UserSerializer, ProfileSerializer
from .forms import UserForm, ProfileForm
from .models import Profile
from apps.lot.models import Lot
from apps.auction.models import Auction

User = get_user_model()


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)



class UserProfileUpdateView(UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ('created_at',)

    def get_queryset(self):
        queryset = User.objects.exclude(pk=self.request.user.pk)

        queryset = queryset.order_by(*self.ordering)

        return queryset


def sign_in(request):
    context = {}

    if request.method == 'GET':
        context['title'] = 'Sign in'
        context['user'] = ""
        return render(request, 'users/sign_in.html', context=context)
    elif request.method == 'POST':
        # Get data from form
        user_login = request.POST.get('email')
        user_password = request.POST.get('password')
        print(f"{user_login=}")
        print(f"{user_password=}")
        # Check user
        user = authenticate(request, username=user_login, password=user_password)
        # AnonymusUser
        print(f"{user=}")
        if user is None:
            context['title'] = 'User or password not found'
            context['color_x'] = 'color:red'
            context['user'] = ""
            return render(request, 'users/sign_in.html', context=context)
        else:
            login(request, user)
            context['title'] = 'Authorization report'
            context['user'] = user

        return render(request, 'users/sign_in.html', context=context)


def sign_up(request, user_id=0):
    context = {}
    context['form2'] = ProfileForm()
    if request.method == 'GET':
        if user_id == 0:
            form = UserForm()
            title = 'Create user'
        else:
            user_request = request.user
            user = get_object_or_404(User, id=user_id)
            if user_request.id != user.id:
                return redirect(reverse('user_details', args=[user.id]))
            form = UserForm(instance=user)
            form2 = ProfileForm(instance=user.profile)

            title = 'Update user'
            context['form2'] = form2
        context['form'] = form
        context['title'] = title

        return render(request, 'users/sign_up.html', context=context)
    elif request.method == 'POST':
        if not user_id:
            form = UserForm(request.POST)
            form2 = ProfileForm(request.POST)
            title = 'Create user'
        else:
            user_request = request.user
            user = get_object_or_404(User, id=user_id)
            if user_request.id != user.id:
                return redirect(reverse('user_details', args=[user.id]))
            form = UserForm(request.POST, instance=user)
            form2 = ProfileForm(request.POST, instance=user.profile)
            title = 'Update user'
        if form.is_valid() and form2.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = 1
            if 'password' in form.cleaned_data:
                new_user.password = make_password(form.cleaned_data['password'])
            new_user.save()
            new_profile = form2.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            profile = Profile.objects.filter(user=new_user.id).first()
            if not profile:
                profile = Profile.objects.create(user=new_user)
                # profile.name = form.cleaned_data['name']
                # profile.surname = form.cleaned_data['surname']
                profile.save()
            return redirect(reverse('user_details', args=[new_user.id]))
        else:
            context = {'form': form,
                       'form2': form2,
                       'title': title}
            return render(request, 'users/sign_up.html', context=context)


def sign_out(request):
    logout(request)
    context = {}
    context['title'] = 'Sign out'
    return render(request, 'users/sign_out.html', context=context)


def user_detail(request):
    pass


def user_list(request):
    pass


def password_reset(request):
    pass


def user_details(request, user_id=None):
    user = request.user
    if user.is_anonymous:
        return redirect('/users/sign_in/')
    # user1 = User.objects.get(pk=user_id)
    context = {}
    context['title'] = 'User details'
    context['user'] = user
    profile = Profile.objects.filter(user=user.id).first()
    if not profile:
        profile = Profile.objects.create(user=user)
    context['profile'] = profile
    context['first_name'] = profile.name
    context['last_name'] = profile.surname
    context['phone'] = profile.phone
    context['avatar'] = profile.avatar
    context['lots'] = Lot.objects.filter(owner=user.id)

    return render(request, 'users/user_details.html', context)
