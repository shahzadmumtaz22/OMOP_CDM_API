from rest_framework import serializers
# from .models import Concept
# from .models import Vocabulary
# from .models import ConceptRelationship
# from .models import ConceptAncestor
# from .models import ConceptClass
# from .models import ConceptSynonym
from .models import *

class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Concept
        fields='__all__'
        
class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model=Vocabulary
        fields='__all__'
        
class ConceptRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model=ConceptRelationship
        fields='__all__'
        
class ConceptAncestorSerializer(serializers.ModelSerializer):
    class Meta:
        model=ConceptAncestor
        fields='__all__'      
                  
class ConceptClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=ConceptClass
        fields='__all__'                        

class ConceptSynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model=ConceptSynonym
        fields='__all__'     
                           
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model=Domain
        fields='__all__'  
              
class DrugStrengthSerializer(serializers.ModelSerializer):
    class Meta:
        model=DrugStrength
        fields='__all__'        