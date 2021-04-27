from django.urls import include, path
from rest_framework import routers
# from .views import ConceptViewSet
# from .views import VocabularyViewSet
# from .views import ConceptRelationshipViewSet
# from .views import ConceptAncestorViewSet
# from .views import ConceptClassViewSet
# from .views import ConceptSynonymViewSet
from .views import *

routers=routers.DefaultRouter()
routers.register(r'concepts', ConceptViewSet)
routers.register(r'vocabularies', VocabularyViewSet)
routers.register(r'conceptrelationships', ConceptRelationshipViewSet)
routers.register(r'conceptancestors', ConceptAncestorViewSet)
routers.register(r'conceptclasses', ConceptClassViewSet)
routers.register(r'conceptsynonyms', ConceptSynonymViewSet)
routers.register(r'domains', DomainViewSet)
routers.register(r'drugstrengths', DrugStrengthViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('api_auth/',include('rest_framework.urls',namespace='rest_framework')),
]