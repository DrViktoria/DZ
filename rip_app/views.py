from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from rip_app.models import OfficesModel, MembersModel
from django.views.generic import TemplateView, DetailView, ListView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from rip_app.forms import LoginForm, SignupForm, OfficeForm, MemberForm, CreateForm
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

'''
class Offices(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        Offices = OfficesModel.objects.all()
        context = dict(Offices=Offices)
        return context
'''


class OfficesListView(ListView):
    template_name = 'include/office.html'
    model = OfficesModel
    context_object_name = 'Offices'
    paginate_by = 10

class Offices(OfficesListView):
    template_name = 'index.html'


class OfficeDetail(DetailView):
    template_name = 'members.html'
    model = OfficesModel

    def get_context_data(self, **kwargs):
        context = super(OfficeDetail, self).get_context_data()
        Members = context["object"].members.all()
        context = dict(Members=Members)
        return context


def index(request):
    return render(request, 'index.html')


def login(request):
    redirect_to = request.GET.get('next')
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            auth.login(request, form.cleaned_data['user'])
            if redirect_to:
                return redirect(redirect_to)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            u = form.save()
            auth.login(request, u)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def logout(request):
    redirect_to = request.GET.get('next')
    auth.logout(request)
    if redirect_to:
        return redirect(redirect_to)
    return redirect('/')


def office_new(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            office = OfficesModel()
            office.named = request.POST.get('Название')
            office.location = request.POST.get('Адрес')
            office.picture = request.FILES.get('Логотип')
            office.save()
            return redirect('Offices')
    else:
        form = CreateForm()
    return render(request, 'newOffice.html', {'form': form})


def listing(request):
    offices_list = OfficesModel.objects.all()
    paginator = Paginator(offices_list, 5)

    page = request.GET.get('page')
    try:
        offices = paginator.page(page)
    except PageNotAnInteger:
        offices = paginator.page(1)
    except EmptyPage:
        offices = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {"offices": offices})


def member_new(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            return redirect('Offices')
    else:
        form = MemberForm()
    return render(request, 'new_member.html', {'form': form})


def sub(request):
    member = request.user.member
    office = OfficesModel.objects.get(id=request.POST["office_id"])
    office.members.add(member)
    office.save()
    return redirect('/')
