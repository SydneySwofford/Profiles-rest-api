from rest_framework.views import APIView
from rest_framework.response import Response 

class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'Uses HTTP methods as function(get, post, patch,put, delete)',
            'Is similar to traditional Django view',
            'gives you most conrol over app logic',
            'is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})