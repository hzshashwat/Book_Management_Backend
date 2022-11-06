from django.shortcuts import render
from .serializer import BookSerializers
from catalog.models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def HomeView(request):
    if request.method == 'GET' :
        book = Book.objects.all()
        try:
            bookjson = BookSerializers(book, many=True)
            return Response({"message" : [bookjson.data]})
        except Exception as e:
            return({"error":e})

    elif request.method == 'POST' :
        #bookdata = request.data
        try :
            bookdata = request.data
            print(bookdata)
            bookobj = BookSerializers(data = bookdata)
            if bookobj.is_valid() == True:
                bookobj.save()
                return Response({"message": "Your data is saved successfully",
                "status": "Success"
                })
            else :
                return Response({"message": bookobj.errors,
                "status": "Failed"
                })
        except Exception as e:
            return Response({"message": e})

    elif request.method == 'DELETE' :
        try:
            book = Book.objects.all().delete()
            return Response({"message" : "All the book records have been deleted successfully."})
        except Exception as e:
            return({"error":e})

@api_view(['GET'])
def NeededBooksView(request):
    if request.method == 'GET' :
        limit = int(request.query_params['n'])
        print(limit)
        book = Book.objects.all().filter(inventory__lt = limit)
        try:
            bookjson = BookSerializers(book, many=True)
            return Response({"message" : [bookjson.data]})
        except Exception as e:
            return({"error":e})

@api_view(['GET'])
def UnavailableBooksView(request):
    if request.method == 'GET' :
        book = Book.objects.all().filter(inventory = 0)
        try:
            bookjson = BookSerializers(book, many=True)
            return Response({"message" : [bookjson.data]})
        except Exception as e:
            return({"error":e})

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def BookView(request):
    if request.method == 'GET' :
        book = Book.objects.get(isbn_no = request.query_params['isbn_no'])
        try:
            bookjson = BookSerializers(book, many=False)
            return Response({"message" : [bookjson.data]})
        except Exception as e:
            return({"error":e})

    elif request.method == 'PUT' :
        #bookdata = request.data
        try :
            bookdata = request.data
            print(bookdata)
            bookobj = BookSerializers(data = bookdata)
            if bookobj.is_valid() == True:
                bookobj.save()
                return Response({"message": "Your data is saved successfully",
                "status": "Success"
                })
            else :
                return Response({"message": bookobj.errors,
                "status": "Failed"
                })
        except Exception as e:
            return Response({"message": e})

    elif request.method == 'DELETE' :
        try:
            book = Book.objects.all().delete()
            return Response({"message" : "All the book records have been deleted successfully."})
        except Exception as e:
            return({"error":e})