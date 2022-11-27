from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', HomeView, name = 'homeview'),
    path('books/find_books_needed/', NeededBooksView, name= 'neededbooks'),
    path('books/unavailable_books/', UnavailableBooksView, name= 'unavailablebooks'),
    path('book/', BookView, name= 'bookview'),
    path('book/issue_book/', IssueBookView, name= 'issuebook')
]