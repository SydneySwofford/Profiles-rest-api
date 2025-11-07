from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status #status codes for returning from API 
from profiles_api import serializers
from rest_framework import viewsets

class HelloAPIView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializer

    def get(self, request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'Uses HTTP methods as function(get, post, patch,put, delete)',
            'Is similar to traditional Django view',
            'gives you most conrol over app logic',
            'is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self,request):
        """Create a Hello Message with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message': message})
        else: 
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """"Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete objects in database"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class=serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset=['users actions(list, create, retreive, upadate, partial update)',
        'Automatically maps to URLS using routers',
        'provides more fucntionality with less code',]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message=f'Hello{name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    
    def retreive(self, request,pk=None):
        """Handle getting an objedct by ID"""
        return Respone({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self,response,pk=None):
        """Handle updating parial object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object"""
        return Response({'http_methd': 'DELETE'})




