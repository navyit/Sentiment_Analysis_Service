import os
from django.shortcuts import render
import pickle
import numpy as np
from .forms import ReviewForm
from .models import Review

# Получение пути к текущему файлу
current_dir = os.path.dirname(__file__)

# Путь к модели и векторизатору
model_path = os.path.join(current_dir, 'models', 'model.pkl')
vectorizer_path = os.path.join(current_dir, 'models', 'vectorizer.pkl')

# Загрузка модели и векторайзера
with open(model_path, 'rb') as model_file:
    clf = pickle.load(model_file)

with open(vectorizer_path, 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def classify_review(review_text):
    new_review_vectorized = vectorizer.transform([review_text])
    prediction = clf.predict(new_review_vectorized)
    
    # Подсчет рейтинга
    rating = np.random.randint(1, 11) if prediction[0] == 1 else np.random.randint(1, 6)
    
    return "Positive" if prediction[0] == 1 else "Negative", rating

def review_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            status, rating = classify_review(text)
            review = Review(text=text, status=status, rating=rating)
            review.save()
            return render(request, 'reviews/review_result.html', {'status': status, 'rating': rating})
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})