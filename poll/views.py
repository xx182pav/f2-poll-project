from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RadioPollForm, CheckboxPollForm, UserRegistrationForm
from .models import RadioPoll, CheckboxPoll

@login_required(login_url='/login/')
def home(request):
    polls = RadioPoll.objects.all()
    pollsed = CheckboxPoll.objects.all()
    context = {
        'polls' : polls,
        'pollsed' : pollsed
    }
    return render(request, 'poll/home.html', context)



@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        form = RadioPollForm(request.POST, request.FILES)
        foo = CheckboxPollForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            if foo.is_valid():
                foo.save() 
           
        return redirect('home')
    else:
        form = RadioPollForm()
        foo = CheckboxPollForm()
        context = {
            'form' : form,
            'foo' : foo
        }
    return render(request, 'poll/create.html', context)


   
@login_required(login_url='/login/')
def radio_vote(request, radio_id):

    poll = RadioPoll.objects.get(pk=radio_id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        elif selected_option == 'option4':
            poll.option_four_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('radio_results', poll.radio_id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/radio_vote.html', context)

@login_required(login_url='/login/')
def checkbox_vote(request, checkbox_id):

    po = CheckboxPoll.objects.get(pk=checkbox_id)
    if request.method == 'POST':
        select_opt = request.POST['po']
        if select_opt == 'opt1':
            po.opt_one_count += 1
        elif select_opt == 'opt2':
            po.opt_two_count += 1
        elif select_opt == 'opt3':
            po.opt_three_count += 1
        elif select_opt == 'opt4':
            po.opt_four_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        po.save()

        return redirect('checkbox_results', po.checkbox_id)

    context = {
        'po' : po
    }
    return render(request, 'poll/checkbox_vote.html', context)

@login_required(login_url='/login/')
def radio_results(request, radio_id):
    poll = RadioPoll.objects.get(pk=radio_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/radio_results.html', context)

@login_required(login_url='/login/')
def checkbox_result(request, checkbox_id):
    po = CheckboxPoll.objects.get(pk=checkbox_id)
    context = {
        'po' :po
    }
    return render(request, 'poll/checkbox_results.html', context)


# def urload_field(request):
#     if request.method == 'POST':
#         fo = UrloadFieldForm(request.POST, request.FILES)
#         if fo.is_valid():
#             fo.save()
#     else:
#         fo = UrloadFieldForm()
#     return render(request, 'index.html', {'fo': fo})

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Не правильное имя пользователя или пароль')

    return render(request, 'poll/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email=email, password=password)
            messages.success(request, 'Спасибо за регистрацию {}'.format(user.username))
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'poll/register.html', {'form': form})
