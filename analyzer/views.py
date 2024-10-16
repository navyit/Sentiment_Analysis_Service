import os
   import pickle
   import re
   import nltk
   from nltk.corpus import stopwords
   from nltk.tokenize import word_tokenize
   from django.http import JsonResponse
   from django.views import View
   from django.shortcuts import render

with open(os.path.join('model.p'), 'rb') as f:
       data = pickle.load(f)

   model = data['model']
   vectorizer = data['vectorizer']

   nltk.download('punkt')
   nltk.download('stopwords')
   stop_words = stopwords.words('english')
   stop_words.remove('not')

   def data_preprocessing(review):
       review = re.sub(re.compile('<.*?>'), '', review)
       review = re.sub('[^A-Za-z0-9]+', ' ', review)
       review = review.lower()
       tokens = word_tokenize(review)
       review = [word for word in tokens if word not in stop_words]
       return ' '.join(review)

   class ClassifyReview(View):
       def get(self, request):
           return render(request, 'analyzer/index.html')

       def post(self, request):
           text = request.POST.get('text', '')
           if text:
               processed_text = data_preprocessing(text)
               new_review_vectorized = vectorizer.transform([processed_text])
               prediction = model.predict(new_review_vectorized)
               rating = 10 if prediction[0] == 1 else 1  # Пример простого рейтинга
               return JsonResponse({
                   'status': 'positive' if prediction[0] == 1 else 'negative',
                   'rating': rating
               })
           return JsonResponse({'error': 'No review provided'}, status=400)