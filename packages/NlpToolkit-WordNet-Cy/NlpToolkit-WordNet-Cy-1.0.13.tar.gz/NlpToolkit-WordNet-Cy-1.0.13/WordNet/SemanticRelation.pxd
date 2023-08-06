from WordNet.Relation cimport Relation


cdef class SemanticRelation(Relation):

    cdef object __relation_type
    cdef int __to_index

    cpdef int toIndex(self)
    cpdef object getRelationType(self)
    cpdef setRelationType(self, object relationType)
    cpdef str getTypeAsString(self)
