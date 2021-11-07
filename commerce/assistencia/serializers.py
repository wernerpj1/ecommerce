from rest_framework import serializers

from .models import ServiceOrder, Sugestion



class ServiceOrderSerializer(serializers.ModelSerializer):    
    

    class Meta:
        model = ServiceOrder
        fields = (
            "id",
            "address",
            "zipcode",
            "place",  
            "phone",
            "product",
            "txService",
        )
class SugestionSerializer(serializers.ModelSerializer):    
    

    class Meta:
        model = Sugestion
        fields = (
            "id",
            "sugestao",
            "created_at",
        )
