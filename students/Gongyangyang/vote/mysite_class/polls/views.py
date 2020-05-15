#from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic

from .models import  Question,Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

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
    
        