from django.shortcuts import render, redirect

# Create your views here.
from feedback.forms import QuestionForm
from feedback.models import Question


def questionCreate(request):
    if request.method == 'POST':
        setForm = QuestionForm(request.POST)
        if setForm.is_valid():
            question = setForm.save(commit=False)
            question.visitorAccount = request.user
            setForm.save()
            return redirect('feedback:feedbackSNR')

    else:
        getQuestion = Question.objects.filter(visitorAccount=request.user)
        setForm = QuestionForm()
        return render(request, "feedback/feedbackSNR.html", {'form': setForm,
                                                             'questions': getQuestion})








