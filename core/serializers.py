from rest_framework import serializers

class HomeSerilizer(serializers.Serializer):
    """ serializa un campo para probar en APIView """
    name = serializers.CharField(max_length = 10)