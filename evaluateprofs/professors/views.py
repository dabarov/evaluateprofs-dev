import requests
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Professor
from .forms import CommentForm


def professor_profile(request, id):
    professor = get_object_or_404(Professor, id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid() and request.user.is_authenticated:
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''
        if result['success']:
            comment = form.save(commit=False)
            comment.author = request.user
            comment.professor = professor
            comment.score = calculate_score(comment)
            professor.comments_number += 1
            professor.communication = ((professor.communication *
                                       (professor.comments_number - 1) +
                                       comment.communication) /
                                       professor.comments_number)
            professor.marking = ((professor.marking * (professor.comments_number -
                                 1) + comment.marking) / professor.comments_number)
            professor.objectivity = ((professor.objectivity *
                                     (professor.comments_number - 1) +
                                     comment.objectivity) /
                                     professor.comments_number)
            professor.quality = ((professor.quality * (professor.comments_number -
                                 1) + comment.quality) / professor.comments_number)
            professor.score = calculate_score(professor)
            professor.save()
            comment.save()
            return redirect(request.path)
    context = {'professor': professor, 'comment': form}
    return render(request, 'professor_profile.html', context)


def professors_list(request):
    query_set = Professor.objects.order_by('-score')
    query = request.GET.get('q')
    if query:
        for word in query.split():
            query_set = query_set.filter(Q(name__icontains=word) |
                                         Q(school__icontains=word) |
                                         Q(department__icontains=word) |
                                         Q(title__icontains=word))
    paginator = Paginator(query_set, 100)
    page = request.GET.get('page')
    query_set = paginator.get_page(page)
    context = {'professors': query_set, 'page_title': 'Top of professors'}
    return render(request, 'top.html', context)


def home_page(request):
    # UNCOMMENT when you add at least one prof
    # professor_score = Professor.objects.order_by('-score')[0]
    # professor_comments = Professor.objects.order_by('-comments_number')[0]
    # context = {'page_title': 'Home', 'professor_score': professor_score,
    #            'professor_comments': professor_comments}
    context = {'page_title': 'Home'}
    return render(request, "index.html", context)


def about_page(request):
    return render(request, "about.html", {'page_title': 'About'})


def terms_page(request):
    return render(request, "terms.html", {'page_title': 'Terms of service'})


def calculate_score(instace):
    return (instace.communication + instace.marking +
            instace.objectivity + instace.quality) / 4
