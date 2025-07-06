from rest_framework.views import APIView
from rest_framework.response import Response

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "status": "ok"
        })

health_view = HealthView.as_view()

class BookView(APIView):
    """ List all books, or create a new book """
    
    def get(self, request, *args, **kwargs):
        return Response({
            "hello": "django"
        })

book_view = BookView.as_view()