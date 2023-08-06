from NamedEntityRecognition.Gazetteer cimport Gazetteer


cdef class AutoNER:

    cdef Gazetteer person_gazetteer, organization_gazetteer, location_gazetteer
