from django.shortcuts import render

from reviews.sentiment import analyze_sentiment
from .forms import ReviewForm

# Create your views here.
def home(request):
    results = None
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            label,score = analyze_sentiment(review.text)
            review.sentiment = label
            review.score = score
            review.save()
            results = {
                'label': label,
                'score': score,
                'text': review.text
            }
    else:
        form = ReviewForm()
    return render(request, 'reviews/home.html', {'form': form, 'results': results})