from rest_framework import serializers

from .models import ServiceOrder, Sugestion



class ServiceOrderSerializer(serializers.ModelSerializer):    
    

    class Meta:
        model = ServiceOrder
        fields = (
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
            "user",
            "sugestao",
            "created_at",
        )
