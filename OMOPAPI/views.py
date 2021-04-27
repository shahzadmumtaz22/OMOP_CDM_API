from django.shortcuts import render
from rest_framework import viewsets
#from .serializers import ConceptSerializer, VocabularySerializer, ConceptRelationshipSerializer, ConceptAncestorSerializer, ConceptClassSerializer, ConceptSynonymSerializer
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

#from .models import Concept, Vocabulary, ConceptRelationship, ConceptAncestor, ConceptClass, ConceptSynonym 
from .models import *
# Create your views here.
class ConceptViewSet(viewsets.ModelViewSet):
    queryset=Concept.objects.all()
    serializer_class=ConceptSerializer

class VocabularyViewSet(viewsets.ModelViewSet):
    queryset=Vocabulary.objects.all()
    serializer_class=VocabularySerializer

class ConceptRelationshipViewSet(viewsets.ModelViewSet):
    queryset=ConceptRelationship.objects.all()
    serializer_class=ConceptRelationshipSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['concept_id_1', 'concept_id_2', 'relationship_id']

class ConceptAncestorViewSet(viewsets.ModelViewSet):
    queryset=ConceptAncestor.objects.all()
    serializer_class=ConceptAncestorSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['ancestor_concept_id', 'descendant_concept_id']
    
class ConceptClassViewSet(viewsets.ModelViewSet):
    queryset=ConceptClass.objects.all()
    serializer_class=ConceptClassSerializer

class ConceptSynonymViewSet(viewsets.ModelViewSet):
    queryset=ConceptSynonym.objects.all()
    serializer_class=ConceptSynonymSerializer

class DomainViewSet(viewsets.ModelViewSet):
    queryset=Domain.objects.all()
    serializer_class=DomainSerializer

class DrugStrengthViewSet(viewsets.ModelViewSet):
    queryset=DrugStrength.objects.all()
    serializer_class=DrugStrengthSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['drug_concept_id', 'ingredient_concept_id']
    