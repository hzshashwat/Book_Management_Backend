from django.shortcuts import render
from .serializer import BookSerializers, ChangeRecordSerializer, UpdateRecordSerializers
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
            return Response({"error": str(e)})

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
            return Response({"message": str(e)})

    elif request.method == 'DELETE' :
        try:
            book = Book.objects.all().delete()
            return Response({"message" : "All the book records have been deleted successfully."})
        except Exception as e:
            return Response({"error": str(e)})

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
            return Response({"error": str(e)})

@api_view(['GET'])
def UnavailableBooksView(request):
    if request.method == 'GET' :
        book = Book.objects.all().filter(inventory = 0)
        try:   
            bookjson = BookSerializers(book, many=True)
            return Response({"message" : [bookjson.data]})
        except Exception as e:
            return Response({"error": str(e)})

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def BookView(request):
    if request.method == 'GET' :
        try:
            book = Book.objects.get(isbn_no = request.query_params['isbn_no'])
            bookjson = BookSerializers(book, many=False)
            #if bookjson.is_valid() == True:
            return Response({"message" : [bookjson.data]})
            # else:
            #     return Response({"message": bookjson.errors,
            #     "status": "Failed"
            #     })
        except Exception as e:
            return Response({"error": str(e)})

    elif request.method == 'PUT' :
        book = Book.objects.get(isbn_no = request.query_params['isbn_no'])
        try :
            bookobj = ChangeRecordSerializer(book, data=request.data)
            if bookobj.is_valid():
                bookobj.save()
                return Response({"message" : "Book record replaced successfully."})
            else :
                return Response({"message": bookobj.errors,
                "status": "Failed"
                })
        except Exception as e:
            return Response({"message": str(e)})
    
    elif request.method == 'PATCH' :
        book = Book.objects.get(isbn_no = request.query_params['isbn_no'])
        try :
            bookobj = UpdateRecordSerializers(book, data=request.data)
            if bookobj.is_valid():
                bookobj.save()
                return Response({"message" : "Book record updated successfully."})
            else :
                return Response({"message": bookobj.errors,
                "status": "Failed"
                })
        except Exception as e:
            return Response({"message": str(e)})

    elif request.method == 'DELETE' :
        try:
            book = Book.objects.get(isbn_no = request.query_params['isbn_no']).delete()
            return Response({"message" : "The book record has been deleted successfully."})
        except Exception as e:
            return Response({"error": str(e)})

@api_view(['GET'])
def IssueBookView(request) :
    if request.method == 'GET':
        try:
            book = Book.objects.get(isbn_no = request.query_params['isbn_no'])
            book.inventory -= 1
            book.save()
            return Response({"message" : "Book issued successfully and Inventory updated."})
        except Exception as e:
            return Response({"error": str(e)})