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