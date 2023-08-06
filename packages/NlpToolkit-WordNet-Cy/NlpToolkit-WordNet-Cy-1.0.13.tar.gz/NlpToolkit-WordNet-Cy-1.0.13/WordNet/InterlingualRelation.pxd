from WordNet.Relation cimport Relation


cdef class InterlingualRelation(Relation):

    cdef object __dependency_type

    cpdef object getType(self)
    cpdef str getTypeAsString(self)
