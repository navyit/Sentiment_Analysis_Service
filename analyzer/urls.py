from django.urls import path
   from .views import ClassifyReview

   urlpatterns = [
       path('classify/', ClassifyReview.as_view(), name='classify'),
   ]