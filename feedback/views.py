from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.http import HttpResponse

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

def thank_you_view(request):
    return render(request, 'feedback/thank_you.html')

def home(request):
    return render(request, 'home.html')
