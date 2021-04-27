# CoConnect_OMOP_CDM_API

An API to access OMOP CDM contents.

Example API URLs for accessing OMOP CDM Contents:

Markup: 
  1:  API Root: http://127.0.0.1:8000/
  2:  Concept Table: http://127.0.0.1:8000/concepts/1/
  3:  Vocabulary Table: http://127.0.0.1:8000/vocabularies/Cost/
- Concetp Relationship Table: http://127.0.0.1:8000/conceptrelationships/?concept_id_1=5&concept_id_2=58&relationship_id=Concept%20replaced%20by (instead of accessing through primary key in the URL, it works with content filter feature of Django with query terms)
Concept Ancestor Table: http://127.0.0.1:8000/conceptancestors/262/
Concept Class Table: http://127.0.0.1:8000/conceptclasses/10th%20level/
Concept Synonym Class: http://127.0.0.1:8000/conceptsynonyms/2/
Domain Table: http://127.0.0.1:8000/domains/Condition/
Drug Strength Table: http://127.0.0.1:8000/drugstrengths/?drug_concept_id=32763&ingredient_concept_id=32763





