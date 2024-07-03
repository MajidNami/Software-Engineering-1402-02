from django.shortcuts import render, redirect
from .models import Question, Choice, UserResult
from .forms import UserForm, QuestionForm, ChoiceForm

def home(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        #if form.is_valid():
            #user = form.cleaned_data['user']
        user = request.user
        print(user)
        questions = Question.objects.all()
        return render(request, 'questions.html', {'questions': questions, 'user': user})
    else:
        form = UserForm()
    return render(request, 'home.html', {'form': form})

def submit_answers(request):
    if request.method == "POST":
        #user = request.POST['user']
        user = request.user
        print(user)
        score = 0
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = key.split('_')[1]
                question = Question.objects.get(id=question_id)
                selected_choice = Choice.objects.get(id=value)
                if selected_choice.is_correct:
                    score += 1
        UserResult.objects.create(user=user, score=score)
        return render(request, 'result.html', {'user': user, 'score': score, 'total_questions': Question.objects.count()})
    return redirect('start_quiz')

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_choice')
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})

def add_choice(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_choice')
    else:
        form = ChoiceForm()
    return render(request, 'add_choice.html', {'form': form})
