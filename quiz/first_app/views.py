from django.shortcuts import get_object_or_404, render, Http404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Question,User,Choice,VoteReason
from .forms import UserForm, Questions, Choices, Questions1
from django.contrib.admin.views.decorators import staff_member_required
#@staff_member_required


# Create your views here.

def index(request):
    # from Question set class find all categories and make a distinguish according to status.
    question_list1 = Question.objects.filter(status=Question.Status_Draft)
    question_list2 = Question.objects.filter(status=Question.Status_Voting)
    question_list3 = Question.objects.filter(status=Question.Status_End)
    question_list4 = Question.objects.filter(status=Question.Status_Deleted)

    context = {
            'question_list1': question_list1,
            'question_list2': question_list2,
            'question_list3': question_list3,
            'question_list4': question_list4,
        }
    
    return render(request,'first_app/index.html', context)

def question_status_modify(request, question_id):
    question = Question.objects.get(pk=question_id)
    vote_reason_list = VoteReason.objects.all()
    if request.method == "POST":
        print(question)
        # Fetch list of items to delete, by ID
        items_to_delete = request.POST.getlist('delete_items')
        print(request.POST)
        print(items_to_delete)
        # Delete those items all in one go
        choice_to_delete = Choice.objects.filter(pk__in=items_to_delete)
        choice_to_delete.delete()

        question_form = Questions(request.POST,instance=question,initial={'question': question})
        
        if question_form.is_valid():
            question_form.save()
            # messages.success(request,_('success!'))
            messages.success(request, ' Question updated.')
           
            print(question_form.cleaned_data)
            # return render(request,'first_app/index1.html', {'question':question})
        else:
            # the form was invalid if this else gets called.
            print(question_form.errors)
    else: 
        question_form = Questions(instance=question,initial={'question': question})
        # choice_form = Choices() 
    return render(request,'first_app/question_status_modify.html',
                         {'question_form':question_form, 'question': question,'vote_reason_list': vote_reason_list})
    
    # if question.status == 0:
    #     if request.method == 'POST':
    #         question.question_text = request.POST.get('question_text')
    #         question.status = request.POST.get('status')
    #         question.save()
    #         question = Question.objects.get(pk=question_id)

    #         choice = Choice()
    #         choice.question = question
    #         choice.voter = request.user
    #         choice.choice_text = request.POST.get('choice_text')
    #         choice.save()

    #         # Fetch list of items to delete, by ID
    #         items_to_delete = request.POST.getlist('delete_items')
    #         # Delete those items all in one go
    #         # Choice.objects.filter(pk__in=items_to_delete).delete()
    #         choice_to_delete = Choice.objects.filter(pk__in=items_to_delete)
    #         choice_to_delete.delete()
            
    #         print(question.status)
    #         # if choice_to_delete is None:
    #         #     print(1)
    #         # else:
    #         #     print(2)

        # else:
        #     render(request,'first_app/index.html',)
    
    
    # return HttpResponse('Error')
            # choice = Choice()
            # question.question = request.POST['choice_text']



def question_modify_interval(request,choice_id):
    choice = Choice.objects.get(pk=choice_id)
    voter = request.user
    # selected_choice = question.choice_in_question.get(pk=request.POST['choice'])
    # choice_text = Choice.objects.filter(question=question)
    if request.method == "POST":
        choice_form = Choices(data = request.POST,instance=choice,initial={'choice': choice})
        
        if choice_form.is_valid():
            choice_form.save()
            
            print(choice_form.cleaned_data)
            question_list1 = Question.objects.filter(status=Question.Status_Draft)
            question_list2 = Question.objects.filter(status=Question.Status_Voting)
            question_list3 = Question.objects.filter(status=Question.Status_End)
            question_list4 = Question.objects.filter(status=Question.Status_Deleted)

            context = {
                'question_list1': question_list1,
                'question_list2': question_list2,
                'question_list3': question_list3,
                'question_list4': question_list4,
            }
        
            return render(request,'first_app/index.html', context)
        else:
            # the form was invalid if this else gets called.
            print(choice_form.errors)
    else: 
        choice_form = Choices(instance=choice, initial={'choice': choice}) 
    return render(request,'first_app/question_modify_interval.html',
                         {'choice_form':choice_form, 'choice_text':choice})

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    
    if request.method == "POST":
        print(question)
        question_form = Questions1(request.POST,instance=question,initial={'question': question})
        
        if question_form.is_valid():
            question_form.save()
           
            print(question_form.cleaned_data)
            # return render(request,'first_app/index1.html', {'question':question})
        else:
            # the form was invalid if this else gets called.
            print(question_form.errors)
    else: 
        question_form = Questions1(instance=question,initial={'question': question})
        # choice_form = Choices() 
    return render(request,'first_app/detail.html',
                         {'question_form':question_form, 'question': question})
    
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist") 
    # return render(request, 'first_app/detail.html', {'question': question})

def detail1(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request,'first_app/detail1.html',
                         {'question': question})

def detail3(request, question_id):
    question = Question.objects.get(pk=question_id)
    print(question)
    return render(request,'first_app/detail3.html',
                         {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


@login_required
def vote(request, question_id): 
    question = Question.objects.get(pk=question_id)
    # choice = get_object_or_404(Choice, pk=choice_id)
    user = request.user
    # reason0 = VoteReason.objects.filter(choice=choice, voter=user)
    # print(reason0)
    # if reason0 is None:
    #if Vote.objects.filter(question=question,voter=request.user).exists():
    #if UserProfileInfo.objects.filter(user=request.user).exists() and Choice.objects.filter(question=question).exists():

    if request.method == "POST": 
        
        reason = VoteReason()
        reason.choice = question.choice_in_question.get(pk=request.POST['choice'])
        reason.voter = user

        reason_text = request.POST.get('reason') 
        reason.reason = reason_text
        reason.save()
        try:
            selected_choice = question.choice_in_question.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'first_app/detail.html', {
                            'question': question,
                            'error_message': "You didn't select a choice.",
                        })
        else:
            selected_choice.votes += 1
            selected_choice.voter = user
            selected_choice.save()
        
    # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
            # return render(request, 'first_app/index.html',)
            return HttpResponse('Voted successfully')
 
def register(request):
    registered = False
    if request.method == "POST":
        print(request.POST)
        user_form = UserForm(data=request.POST)
        # print(user_form)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            print(user_form.cleaned_data)
            registered = True
            # print(user_form.username)
            
            # print(user_form.password)
        else:
            # the form was invalid if this else gets called.
            print(user_form.errors)
    else: 
        user_form = UserForm()
    return render(request,'first_app/registration.html',
                         {'user_form':user_form,
                          'registered':registered})
                           

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone try to login and failed, which means the authentication not pass")
            print("Username{},password{}".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'first_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def state_draft(request, question_id):
    if question.status == 0:
        pass