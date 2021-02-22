
# Keeping this file in for later reference
# This file is not being used by the actual site.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question, Choice

from django.template import loader # This has to do with the HTML stuff
from django.http import Http404 # For 404 requests

from django.http import HttpResponseRedirect # Tutorial part 4, the vote POST stuff
from django.urls import reverse

# Create your views here.
def indexDummy(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Tutorial part 3 stuff now
def detailDummy(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def resultsDummy(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def voteOld(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def indexLongway(request):
    # Overall, this is the more complicated way to go about it.
    # Deprecated version of the method listed further below.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # output = ', '.join([q.question_text for q in latest_question_list])
    # This would hard-code the page.

    # This loads based on an HTML template.
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(output)
    return HttpResponse(template.render(context, request))

def index(request):
    # Just do this instead.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detailLongway(request, question_id):
    # Likewise...
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    # ...do this.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})