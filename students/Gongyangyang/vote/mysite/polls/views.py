#from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.urls import reverse

from .models import  Question,Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html',context)

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return render(context,request))

    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    
def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    #return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html',{'question':question})

def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

    # respose = "You're looking at the results of question %s."
    # return HttpResponse(respose % question_id)

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        
        
        
   # return HttpResponse("You're voting on question %s." % question_id)