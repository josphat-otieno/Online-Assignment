from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from .models import *
from .forms import *
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required


# @login_required(login_url='/accounts/login/')
class QuizListView(ListView):
    model = Quiz 
    template_name = 'quizes/main.html'

@login_required(login_url='/accounts/login/')
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {'obj': quiz})

@login_required(login_url='/accounts/login/')
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

def save_quiz_view(request, pk):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
            
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})

def create_quiz(request):
    user =request.user
    if request.method=='POST':
        question_form = QuestionForm(request.POST)
        quiz_form = QuizForm(request.POST)
        answer_form = AnswerForm(request.POST)
        if question_form.is_valid() and quiz_form.is_valid() and answer_form.is_valid():
            # question = question_form.save(commit=False)
            # quiz =quiz_form.save(commit=False)
            # answer = answer_form.save(commit =False)
            # question.user, quiz.user, answer.user = user
            # question.save()
            # quiz.save()
            # answer.save()
            quiz_form.save()
            quiz_form.save()
            answer_form.save()

            return redirect("main-view")

    else:
        question_form = QuestionForm()
        quiz_form = QuizForm()
        answer_form = AnswerForm()
    return render(request, 'quizes/question.html',{"question_form":question_form, "quiz_form":quiz_form, "answer_form":answer_form})


@login_required(login_url='/accounts/login/')
def profile_view(request):
    user = request.user
    user = User.objects.get(username = user.username)

    return render (request, 'awards/profile.html', {"user":user})

@login_required(login_url='/accounts/login/')
def search(request):
    if 'quizes' in request.GET and request.GET["quizes"]:
        search_term = request.GET.get("quizes")
        searched_quizes = Quiz.search_project(search_term)
        message = f"{search_term}"

        return render(request, 'quizes/search.html',{"message":message,"quizes": searched_quizes})

    else:
        message = "You haven't searched for any quiz"
        return render(request, 'quizes/search.html',{"message":message})

