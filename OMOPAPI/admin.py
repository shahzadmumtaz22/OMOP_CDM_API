from django.contrib import admin
# from .models import Concept
# from .models import Vocabulary
# from .models import ConceptRelationship
# from .models import ConceptAncestor
# from .models import ConceptClass
# from .models import ConceptSynonym
from .models import *
# Register your models here.
admin.site.register(Concept)
admin.site.register(Vocabulary)
admin.site.register(ConceptRelationship)
admin.site.register(ConceptAncestor)
admin.site.register(ConceptClass)
admin.site.register(ConceptSynonym)
admin.site.register(Domain)