from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

#BT - This view is still using Django. It has not use any views from rest framework yet.

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    #BT - Very simple, just check to see which request.method is, then
    #     process it accordingly.
    if request.method == 'GET':
        #BT - Get all the records from our database.
        snippets = Snippet.objects.all()
        #BT - Pass it to Serializer class so that it can convert from the object instance
        #     to Python data type.
        serializer = SnippetSerializer(snippets, many=True)
        #BT - Then send it out to the user.
        #Notes: JsonResponse will render the data to json format and send it out to user
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        #BT - Parse the incoming request data to Python data type.
        data = JSONParser().parse(request)
        #BT - Pass it into the Serializer class to convert it back to object instance.
        serializer = SnippetSerializer(data=data)
        #BT - Check to make sure it is valid before save it to the database.
        if serializer.is_valid():
            #BT - Save it to database.
            serializer.save()
            #BT - Return JsonResponse back to the user with status == 201 Created successful
            return JsonResponse(serializer.data, status=201)
        #BT Otherwise, send out an error.
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    #BT - Get a record from the database based on the pk input.
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        #BT - Passed it to the Serializer for converting from object instance to Python data type
        serializer = SnippetSerializer(snippet)
        #BT - Render it in json format and send it out. Notes: Always use JsonResponse
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        #BT - Parse the incoming data to Python data type.
        data = JSONParser().parse(request)
        #BT - Pass in the new data from the PUT to our existing record and have the Serializer converts it
        #     to the object instance before save it the database.
        serializer = SnippetSerializer(snippet, data=data)
        #BT - Check to make sure the conversion is valid.
        if serializer.is_valid():
            #BT - Save it to our database.
            serializer.save()
            #BT - Send out a JsonResponse back to the user.
            return JsonResponse(serializer.data)
        #BT - Otherwise, error.
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        #BT - Just delete the record.
        snippet.delete()
        #BT - Send out Response.
        return HttpResponse(status=204)

        
