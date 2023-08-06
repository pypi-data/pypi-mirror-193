from Dictionary.Word cimport Word
from NamedEntityRecognition.NamedEntityType import NamedEntityType


cdef class NamedEntityWord(Word):

    cdef object __named_entity_type
