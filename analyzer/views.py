from django.shortcuts import render
import os
import re
import nltk
import pickle
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from sklearn.feature_extraction.text import TfidfVectorizer

with open(os.path.join(settings.AISENTIMENTANALYZER, 'model.p'), 'rb') as f:
    data = pickle.load(f)
model = data['model']
vectorizer = data['vectorizer']

class ClassifyReview(View):
    def get(self, request):
        
        return render(request, 'analyzer/index.html')  
    
    def post(self, request):
        text = request.POST.get('text', '')
        if text:
            new_review_vectorized = vectorizer.transform([text])
            prediction = model.predict(new_review_vectorized)
            rating = self.calculate_rating(prediction[0])
            return JsonResponse({
                'status': 'positive' if prediction[0] == 1 else 'negative',
                'rating': rating
            })
        return JsonResponse({'error': 'No review provided'}, status=400)
    
    def calculate_rating(self, sentiment):
        return 10 if sentiment == 1 else 1  