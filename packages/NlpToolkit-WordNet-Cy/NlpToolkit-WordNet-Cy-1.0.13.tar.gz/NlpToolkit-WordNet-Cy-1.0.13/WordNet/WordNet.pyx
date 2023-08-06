import xml.etree.ElementTree
from collections import OrderedDict

import pkg_resources
from Dictionary.ExceptionalWord cimport ExceptionalWord
from Dictionary.Pos import Pos
from WordNet.InterlingualRelation cimport InterlingualRelation
from WordNet.Relation cimport Relation
from WordNet.SemanticRelationType import SemanticRelationType


cdef class WordNet:

    def __init__(self,
                 fileName: str = None,
                 exceptionFileName: str = None):
        """
        Constructor that initializes the SynSet list, literal list, reads exception.

        PARAMETERS
        ----------
        fileName : str
            Resource to be read for the WordNet.
        """
        cdef SynSet current_syn_set
        cdef str interlingual_id
        cdef list syn_set_list
        cdef Literal current_literal
        self.__exception_list = {}
        if fileName is None:
            fileName = pkg_resources.resource_filename(__name__, 'data/turkish_wordnet.xml')
        elif exceptionFileName is not None:
            self.readExceptionFile(exceptionFileName)
        self.__interlingual_list = {}
        self.__syn_set_list = OrderedDict()
        self.__literal_list = OrderedDict()
        root = xml.etree.ElementTree.parse(fileName).getroot()
        current_syn_set = None
        for syn_set_node in root:
            for part_node in syn_set_node:
                if part_node.tag == "ID":
                    current_syn_set = SynSet(part_node.text)
                    self.addSynSet(current_syn_set)
                elif part_node.tag == "DEF":
                    current_syn_set.setDefinition(part_node.text)
                elif part_node.tag == "EXAMPLE":
                    current_syn_set.setExample(part_node.text)
                elif part_node.tag == "WIKI":
                    current_syn_set.setWikiPage(part_node.text)
                elif part_node.tag == "BCS":
                    current_syn_set.setBcs(int(part_node.text))
                elif part_node.tag == "POS":
                    if part_node.text == "a":
                        current_syn_set.setPos(Pos.ADJECTIVE)
                    elif part_node.text == "v":
                        current_syn_set.setPos(Pos.VERB)
                    elif part_node.text == "b":
                        current_syn_set.setPos(Pos.ADVERB)
                    elif part_node.text == "n":
                        current_syn_set.setPos(Pos.NOUN)
                    elif part_node.text == "i":
                        current_syn_set.setPos(Pos.INTERJECTION)
                    elif part_node.text == "c":
                        current_syn_set.setPos(Pos.CONJUNCTION)
                    elif part_node.text == "p":
                        current_syn_set.setPos(Pos.PREPOSITION)
                    elif part_node.text == "r":
                        current_syn_set.setPos(Pos.PRONOUN)
                elif part_node.tag == "SR":
                    if len(part_node) > 0 and part_node[0].tag == "TYPE":
                        type_node = part_node[0]
                        if len(part_node) > 1 and part_node[1].tag == "TO":
                            to_node = part_node[1]
                            current_syn_set.addRelation(SemanticRelation(part_node.text, type_node.text, int(to_node.text)))
                        else:
                            current_syn_set.addRelation(SemanticRelation(part_node.text, type_node.text))
                elif part_node.tag == "ILR":
                    if len(part_node) > 0 and part_node[0].tag == "TYPE":
                        type_node = part_node[0]
                        interlingual_id = part_node.text
                        if interlingual_id in self.__interlingual_list:
                            syn_set_list = self.__interlingual_list[interlingual_id]
                        else:
                            syn_set_list = []
                        syn_set_list.append(current_syn_set)
                        self.__interlingual_list[interlingual_id] = syn_set_list
                        current_syn_set.addRelation(InterlingualRelation(interlingual_id, type_node.text))
                elif part_node.tag == "SYNONYM":
                    for literal_node in part_node:
                        current_literal = None
                        for child_node in literal_node:
                            if child_node.tag == "SENSE":
                                current_literal = Literal(literal_node.text, int(child_node.text), current_syn_set.getId())
                                current_syn_set.addLiteral(current_literal)
                                self.addLiteralToLiteralList(current_literal)
                            elif child_node.tag == "SR":
                                type_node = child_node[0]
                                if len(child_node) > 1 and child_node[1].tag == "TO":
                                    to_node = child_node[1]
                                    current_literal.addRelation(
                                        SemanticRelation(child_node.text, type_node.text, int(to_node.text)))
                                else:
                                    current_literal.addRelation(SemanticRelation(child_node.text, type_node.text))

    cpdef readExceptionFile(self, str exceptionFileName):
        """
        Method constructs a DOM parser using the dtd/xml schema parser configuration and using this parser it
        reads exceptions from file and puts to exceptionList HashMap.

        PARAMETERS
        ----------
        exceptionFileName : str
            Exception file to be read
        """
        cdef str word_name, root_form
        cdef list word_list
        root = xml.etree.ElementTree.parse(exceptionFileName).getroot()
        for word_node in root:
            word_name = word_node.attrib["name"]
            root_form = word_node.attrib["root"]
            if word_node.attrib["pos"] == "Adj":
                pos = Pos.ADJECTIVE
            elif word_node.attrib["pos"] == "Adv":
                pos = Pos.ADVERB
            elif word_node.attrib["pos"] == "Noun":
                pos = Pos.NOUN
            elif word_node.attrib["pos"] == "Verb":
                pos = Pos.VERB
            else:
                pos = Pos.NOUN
            if word_name in self.__exception_list:
                wordList = self.__exception_list[word_name]
            else:
                wordList = []
            wordList.append(ExceptionalWord(word_name, root_form, pos))
            self.__exception_list[word_name] = wordList

    cpdef addLiteralToLiteralList(self, Literal literal):
        """
        Adds a specified literal to the literal list.

        PARAMETERS
        ----------
        literal : Literal
            literal to be added
        """
        cdef list literals
        if literal.getName() in self.__literal_list:
            literals = self.__literal_list[literal.getName()]
        else:
            literals = []
        literals.append(literal)
        self.__literal_list[literal.getName()] = literals

    cpdef list synSetList(self):
        """
        Returns the values of the SynSet list.

        RETURNS
        -------
        list
            Values of the SynSet list
        """
        return list(self.__syn_set_list.values())

    cpdef list literalList(self):
        """
        Returns the keys of the literal list.

        RETURNS
        -------
        list
            Keys of the literal list
        """
        return list(self.__literal_list.keys())

    cpdef addSynSet(self, SynSet synSet):
        """
        Adds specified SynSet to the SynSet list.

        PARAMETERS
        ----------
        synSet : SynSet
            SynSet to be added
        """
        self.__syn_set_list[synSet.getId()] = synSet

    cpdef removeSynSet(self, SynSet synSet):
        """
        Removes specified SynSet from the SynSet list.

        PARAMETERS
        ----------
        synSet : SynSet
            SynSet to be removed
        """
        self.__syn_set_list.pop(synSet.getId())

    cpdef changeSynSetId(self,
                         SynSet synSet,
                         str newId):
        """
        Changes ID of a specified SynSet with the specified new ID.

        PARAMETERS
        ----------
        synSet : SynSet
            SynSet whose ID will be updated
        newId : str
            new ID
        """
        self.__syn_set_list.pop(synSet.getId())
        synSet.setId(newId)
        self.__syn_set_list[newId] = synSet

    cpdef SynSet getSynSetWithId(self, str synSetId):
        """
        Returns SynSet with the specified SynSet ID.

        PARAMETERS
        ----------
        synSetId : str
            ID of the SynSet to be returned

        RETURNS
        -------
        SynSet
            SynSet with the specified SynSet ID
        """
        if synSetId in self.__syn_set_list:
            return self.__syn_set_list[synSetId]
        else:
            return None

    cpdef SynSet getSynSetWithLiteral(self,
                                      str literal,
                                      int sense):
        """
        Returns SynSet with the specified literal and sense index.

        PARAMETERS
        ----------
        literal : Literal
            SynSet literal
        sense : int
            SynSet's corresponding sense index

        RETURNS
        -------
        SynSet
            SynSet with the specified literal and sense index
        """
        cdef list literals
        cdef Literal current
        if literal in self.__literal_list:
            literals = self.__literal_list[literal]
            for current in literals:
                if current.getSense() == sense:
                    return self.getSynSetWithId(current.getSynSetId())
        return None

    cpdef int numberOfSynSetsWithLiteral(self, str literal):
        """
        Returns the number of SynSets with a specified literal.

        PARAMETERS
        ----------
        literal : Literal
            literal to be searched in SynSets

        RETURNS
        -------
        int
            The number of SynSets with a specified literal
        """
        if literal in self.__literal_list:
            return len(self.__literal_list[literal])
        else:
            return 0

    cpdef list getSynSetsWithPartOfSpeech(self, object pos):
        """
        Returns a list of SynSets with a specified part of speech tag.

        PARAMETERS
        ----------
        pos : Pos
            Part of speech tag to be searched in SynSets

        RETURNS
        -------
        list
            A list of SynSets with a specified part of speech tag
        """
        cdef list result
        cdef SynSet syn_set
        result = []
        for syn_set in self.__syn_set_list.values():
            if syn_set.getPos() is not None and syn_set.getPos() == pos:
                result.append(syn_set)
        return result

    cpdef list getLiteralsWithName(self, str literal):
        """
        Returns a list of literals with a specified literal String.

        PARAMETERS
        ----------
        literal : Literal
            literal String to be searched in literal list

        RETURNS
        -------
        list
            A list of literals with a specified literal String
        """
        if literal in self.__literal_list:
            return self.__literal_list[literal]
        else:
            return []

    cpdef addSynSetsWithLiteralToList(self,
                                      list result,
                                      str literal,
                                      object pos):
        """
        Finds the SynSet with specified literal String and part of speech tag and adds to the given SynSet list.

        PARAMETERS
        ----------
        result : list
            SynSet list to add the specified SynSet
        literal : str
            literal String to be searched in literal list
        pos : Pos
            part of speech tag to be searched in SynSets
        """
        cdef Literal current
        cdef SynSet syn_set
        for current in self.__literal_list[literal]:
            syn_set = self.getSynSetWithId(current.getSynSetId)
            if syn_set is not None and syn_set.getPos() == pos:
                result.append(syn_set)

    cpdef list getSynSetsWithLiteral(self, str literal):
        """
        Finds SynSets with specified literal String and adds to the newly created SynSet list.

        PARAMETERS
        ----------
        literal : Literal
            literal String to be searched in literal list

        RETURNS
        -------
        list
            Returns a list of SynSets with specified literal String
        """
        cdef list result
        cdef Literal current
        cdef SynSet syn_set
        result = []
        if literal in self.__literal_list:
            for current in self.__literal_list[literal]:
                syn_set = self.getSynSetWithId(current.getSynSetId())
                if syn_set is not None:
                    result.append(syn_set)
        return result

    cpdef list getLiteralsWithPossibleModifiedLiteral(self, str literal):
        """
        Finds literals with specified literal String and adds to the newly created literal String list.
        Ex: cleanest - clean

        PARAMETERS
        ----------
        literal : Literal
            literal String to be searched in literal list

        RETURNS
        -------
        list
            Returns a list of literals with specified literal String
        """
        cdef list result
        cdef str word_without_last_one, word_without_last_two, word_without_last_three
        result = [literal]
        word_without_last_one = literal[:len(literal) - 1]
        word_without_last_two = literal[:len(literal) - 2]
        word_without_last_three = literal[:len(literal) - 3]
        if literal in self.__exception_list:
            for exceptional_word in self.__exception_list[literal]:
                result.append(exceptional_word.getRoot())
        if literal.endswith("s") and word_without_last_one in self.__literal_list:
            result.append(word_without_last_one)
        if (literal.endswith("es") or literal.endswith("ed") or literal.endswith("er")) \
                and word_without_last_two in self.__literal_list:
            result.append(word_without_last_two)
        if literal.endswith("ed") and (word_without_last_two + literal[len(literal) - 3]) in self.__literal_list:
            result.append(word_without_last_two + literal[len(literal) - 3])
        if (literal.endswith("ed") or literal.endswith("er")) and (word_without_last_two + "e") in self.__literal_list:
            result.append(word_without_last_two + "e")
        if (literal.endswith("ing") or literal.endswith("est")) and word_without_last_three in self.__literal_list:
            result.append(word_without_last_three)
        if literal.endswith("ing") and (word_without_last_three + literal[len(literal) - 4]) in self.__literal_list:
            result.append(word_without_last_three + literal[len(literal) - 4])
        if (literal.endswith("ing") or literal.endswith("est")) and (word_without_last_three + "e") in self.__literal_list:
            result.append(word_without_last_three + "e")
        if literal.endswith("ies") and (word_without_last_three + "y") in self.__literal_list:
            result.append(word_without_last_three + "y")
        return result

    cpdef list getSynSetsWithPossiblyModifiedLiteral(self,
                                                     str literal,
                                                     object pos):
        """
        Finds SynSets with specified literal String and part of speech tag, then adds to the newly created SynSet list.
        Ex: cleanest - clean

        PARAMETERS
        ----------
        literal : str
            Literal String to be searched in literal list
        pos : Pos
            part of speech tag to be searched in SynSets

        RETURNS
        -------
        list
            Returns a list of SynSets with specified literal String and part of speech tag
        """
        cdef list result
        cdef list modified_literals
        cdef str modified_literal
        result = []
        modified_literals = self.getLiteralsWithPossibleModifiedLiteral(literal)
        for modified_literal in modified_literals:
            if modified_literal in self.__literal_list:
                self.addSynSetsWithLiteralToList(result, modified_literal, pos)
        return result

    cpdef addReverseRelation(self,
                             SynSet synSet,
                             SemanticRelation semanticRelation):
        """
        Adds the reverse relations to the SynSet.

        PARAMETERS
        ----------
        synSet : SynSet
            SynSet to add the reverse relations
        semanticRelation : SemanticRelation
            relation whose reverse will be added
        """
        cdef SynSet other_syn_set
        cdef SemanticRelation other_relation
        other_syn_set = self.getSynSetWithId(semanticRelation.getName())
        if other_syn_set is not None and SemanticRelation.reverse(semanticRelation.getRelationType()) is not None:
            other_relation = SemanticRelation(synSet.getId(),
                                             SemanticRelation.reverse(semanticRelation.getRelationType()))
            if not other_syn_set.containsRelation(other_relation):
                other_syn_set.addRelation(other_relation)

    cpdef removeReverseRelation(self,
                                SynSet synSet,
                                SemanticRelation semanticRelation):
        """
        Removes the reverse relations from the SynSet.

        PARAMETERS
        ----------
        synSet : SynSet
            SynSet to remove the reverse relation
        semanticRelation : SemanticRelation
            relation whose reverse will be removed
        """
        cdef SynSet other_syn_set
        cdef SemanticRelation other_relation
        other_syn_set = self.getSynSetWithId(semanticRelation.getName())
        if other_syn_set is not None and SemanticRelation.reverse(semanticRelation.getRelationType()) is not None:
            other_relation = SemanticRelation(synSet.getId(),
                                             SemanticRelation.reverse(semanticRelation.getRelationType()))
            if other_syn_set.containsRelation(other_relation):
                other_syn_set.removeRelation(other_relation)

    cpdef equalizeSemanticRelations(self):
        """
        Loops through the SynSet list and adds the possible reverse relations.
        """
        cdef SynSet syn_set
        cdef int i
        for syn_set in self.__syn_set_list.values():
            for i in range(syn_set.relationSize()):
                if isinstance(syn_set.getRelation(i), SemanticRelation):
                    self.addReverseRelation(syn_set, syn_set.getRelation(i))

    cpdef constructLiterals(self,
                            str word,
                            MorphologicalParse parse,
                            MetamorphicParse metaParse,
                            FsmMorphologicalAnalyzer fsm):
        """
        Creates a list of literals with a specified word, or possible words corresponding to morphological parse.

        PARAMETERS
        ----------
        word : str
            literal String
        parse : MorphologicalParse
            morphological parse to get possible words
        metaParse : MetamorphicParse
            metamorphic parse to get possible words
        fsm : FsmMorphologicalAnalyzer
            finite state machine morphological analyzer to be used at getting possible words

        RETURNS
        -------
        list
            A list of literal
        """
        cdef list result
        cdef set possible_words
        cdef str possible_word
        result = []
        if parse.size() > 0:
            if not parse.isPunctuation() and not parse.isCardinal() and not parse.isReal():
                possible_words = fsm.getPossibleWords(parse, metaParse)
                for possible_word in possible_words:
                    result.extend(self.getLiteralsWithName(possible_word))
            else:
                result.extend(self.getLiteralsWithName(word))
        else:
            result.extend(self.getLiteralsWithName(word))
        return result

    cpdef list constructSynSets(self,
                                str word,
                                MorphologicalParse parse,
                                MetamorphicParse metaParse,
                                FsmMorphologicalAnalyzer fsm):
        """
        Creates a list of SynSets with a specified word, or possible words corresponding to morphological parse.

        PARAMETERS
        ----------
        word : str
            literal String  to get SynSets with
        parse : MorphologicalParse
            morphological parse to get SynSets with proper literals
        metaParse : MetamorphicParse
            metamorphic parse to get possible words
        fsm : FsmMorphologicalAnalyzer
            finite state machine morphological analyzer to be used at getting possible words

        RETURNS
        -------
        list
            A list of SynSets
        """
        cdef list result
        cdef set possible_words
        cdef str possible_word
        cdef list syn_sets
        result = []
        if parse.size() > 0:
            if parse.isProperNoun():
                result.append(self.getSynSetWithLiteral("(özel isim)", 1))
            if parse.isTime():
                result.append(self.getSynSetWithLiteral("(zaman)", 1))
            if parse.isDate():
                result.append(self.getSynSetWithLiteral("(tarih)", 1))
            if parse.isHashTag():
                result.append(self.getSynSetWithLiteral("(hashtag)", 1))
            if parse.isEmail():
                result.append(self.getSynSetWithLiteral("(email)", 1))
            if parse.isOrdinal():
                result.append(self.getSynSetWithLiteral("(sayı sıra sıfatı)", 1))
            if parse.isPercent():
                result.append(self.getSynSetWithLiteral("(yüzde)", 1))
            if parse.isFraction():
                result.append(self.getSynSetWithLiteral("(kesir sayı)", 1))
            if parse.isRange():
                result.append(self.getSynSetWithLiteral("(sayı aralığı)", 1))
            if parse.isReal():
                result.append(self.getSynSetWithLiteral("(reel sayı)", 1))
            if not parse.isPunctuation() and not parse.isCardinal() and not parse.isReal():
                possible_words = fsm.getPossibleWords(parse, metaParse)
                for possible_word in possible_words:
                    syn_sets = self.getSynSetsWithLiteral(possible_word)
                    if len(syn_sets) > 0:
                        for syn_set in syn_sets:
                            if syn_set.getPos() is not None and (parse.getPos() == "NOUN" or parse.getPos() == "ADVERB"
                                                                or parse.getPos() == "VERB" or parse.getPos() == "ADJ"
                                                                or parse.getPos() == "CONJ"):
                                if syn_set.getPos() == Pos.NOUN:
                                    if parse.getPos() == "NOUN" or parse.getRootPos() == "NOUN":
                                        result.append(syn_set)
                                elif syn_set.getPos() == Pos.ADVERB:
                                    if parse.getPos() == "ADVERB" or parse.getRootPos() == "ADVERB":
                                        result.append(syn_set)
                                elif syn_set.getPos() == Pos.VERB:
                                    if parse.getPos() == "VERB" or parse.getRootPos() == "VERB":
                                        result.append(syn_set)
                                elif syn_set.getPos() == Pos.ADJECTIVE:
                                    if parse.getPos() == "ADJ" or parse.getRootPos() == "ADJ":
                                        result.append(syn_set)
                                elif syn_set.getPos() == Pos.CONJUNCTION:
                                    if parse.getPos() == "CONJ" or parse.getRootPos() == "CONJ":
                                        result.append(syn_set)
                                else:
                                    result.append(syn_set)
                            else:
                                result.append(syn_set)
                if len(result) == 0:
                    for possible_word in possible_words:
                        syn_sets = self.getSynSetsWithLiteral(possible_word)
                        result.extend(syn_sets)
            else:
                result.extend(self.getSynSetsWithLiteral(word))
            if parse.isCardinal() and len(result) == 0:
                result.append(self.getSynSetWithLiteral("(tam sayı)", 1))
        else:
            result.extend(self.getSynSetsWithLiteral(word))
        return result

    cpdef list constructIdiomLiterals(self,
                                      FsmMorphologicalAnalyzer fsm,
                                      MorphologicalParse morphologicalParse1,
                                      MetamorphicParse metaParse1,
                                      MorphologicalParse morphologicalParse2,
                                      MetamorphicParse metaParse2,
                                      MorphologicalParse morphologicalParse3 = None,
                                      MetamorphicParse metaParse3 = None):
        """
        Returns a list of literals using 3 possible words gathered with the specified morphological parses and
        metamorphic parses.

        PARAMETERS
        ----------
        morphologicalParse1 : MorphologicalParse
            morphological parse to get possible words
        morphologicalParse2 : MorphologicalParse
            morphological parse to get possible words
        morphologicalParse3 : MorphologicalParse
            morphological parse to get possible words
        metaParse1 : MetamorphicParse
            metamorphic parse to get possible words
        metaParse2 : MetamorphicParse
            metamorphic parse to get possible words
        metaParse3 : MetamorphicParse
            metamorphic parse to get possible words
        fsm : FsmMorphologicalAnalyzer
            finite state machine morphological analyzer to be used at getting possible words

        RETURNS
        -------
        list
            A list of literals
        """
        cdef list result
        cdef set possible_words1
        cdef set possible_words2
        cdef set possible_words3
        cdef str possible_word1, possible_word2, possible_word3
        result = []
        possible_words1 = fsm.getPossibleWords(morphologicalParse1, metaParse1)
        possible_words2 = fsm.getPossibleWords(morphologicalParse2, metaParse2)
        if morphologicalParse3 is not None and metaParse3 is not None:
            possible_words3 = fsm.getPossibleWords(morphologicalParse3, metaParse3)
            for possible_word1 in possible_words1:
                for possible_word2 in possible_words2:
                    for possible_word3 in possible_words3:
                        result.extend(self.getLiteralsWithName(possible_word1 + " " + possible_word2 +
                                                               " " + possible_word3))
        else:
            for possible_word1 in possible_words1:
                for possible_word2 in possible_words2:
                    result.extend(self.getLiteralsWithName(possible_word1 + " " + possible_word2))
        return result

    cpdef list constructIdiomSynSets(self,
                                     FsmMorphologicalAnalyzer fsm,
                                     MorphologicalParse morphologicalParse1,
                                     MetamorphicParse metaParse1,
                                     MorphologicalParse morphologicalParse2,
                                     MetamorphicParse metaParse2,
                                     MorphologicalParse morphologicalParse3 = None,
                                     MetamorphicParse metaParse3 = None):
        """
        Returns a list of SynSets using 3 possible words gathered with the specified morphological parses and
        metamorphic parses.

        PARAMETERS
        ----------
        morphologicalParse1 : MorphologicalParse
            morphological parse to get possible words
        morphologicalParse2 : MorphologicalParse
            morphological parse to get possible words
        morphologicalParse3 : MorphologicalParse
            morphological parse to get possible words
        metaParse1 : MetamorphicParse
            metamorphic parse to get possible words
        metaParse2 : MetamorphicParse
            metamorphic parse to get possible words
        metaParse3 : MetamorphicParse
            metamorphic parse to get possible words
        fsm : FsmMorphologicalAnalyzer
            finite state machine morphological analyzer to be used at getting possible words

        RETURNS
        -------
        list
            A list of SynSets
        """
        cdef list result
        cdef set possible_words1
        cdef set possible_words2
        cdef set possible_words3
        cdef str possible_word1, possible_word2, possible_word3
        result = []
        possible_words1 = fsm.getPossibleWords(morphologicalParse1, metaParse1)
        possible_words2 = fsm.getPossibleWords(morphologicalParse2, metaParse2)
        if morphologicalParse3 is not None and metaParse3 is not None:
            possible_words3 = fsm.getPossibleWords(morphologicalParse3, metaParse3)
            for possible_word1 in possible_words1:
                for possible_word2 in possible_words2:
                    for possible_word3 in possible_words3:
                        if self.numberOfSynSetsWithLiteral(possible_word1 + " " + possible_word2 + " "
                                                           + possible_word3) > 0:
                            result.extend(self.getSynSetsWithLiteral(possible_word1 + " " + possible_word2 +
                                                                     " " + possible_word3))
        else:
            for possible_word1 in possible_words1:
                for possible_word2 in possible_words2:
                    if self.numberOfSynSetsWithLiteral(possible_word1 + " " + possible_word2) > 0:
                        result.extend(self.getSynSetsWithLiteral(possible_word1 + " " + possible_word2))
        return result

    cpdef sortDefinitions(self):
        """
        Sorts definitions of SynSets in SynSet list according to their lengths.
        """
        cdef SynSet synSet
        for synSet in self.__syn_set_list:
            synSet.sortDefinitions()

    cpdef list getInterlingual(self, str synSetId):
        """
        Returns a list of SynSets with the interlingual relations of a specified SynSet ID.

        PARAMETERS
        ----------
        synSetId : str
            SynSet ID to be searched

        RETURNS
        -------
        list
            A list of SynSets with the interlingual relations of a specified SynSet ID
        """
        if synSetId in self.__interlingual_list:
            return self.__interlingual_list[synSetId]
        else:
            return []

    cpdef bint __containsSameLiteral(self,
                                     SynSet synSet1,
                                     SynSet synSet2):
        cdef int i, j
        cdef Literal literal1, literal2
        for i in range(synSet1.getSynonym().literalSize()):
            literal1 = synSet1.getSynonym().getLiteral(i)
            for j in range(i + 1, synSet2.getSynonym().literalSize()):
                literal2 = synSet2.getSynonym().getLiteral(j)
                if literal1.getName() == literal2.getName() and synSet1.getPos() is not None:
                    return True
        return False

    cpdef saveAsXml(self, str fileName):
        """
        Method to write SynSets to the specified file in the XML format.

        PARAMETERS
        ----------
        fileName : str
            file name to write XML files
        """
        cdef SynSet syn_set
        out_file = open(fileName, "w", encoding="utf8")
        out_file.write("<SYNSETS>\n")
        for syn_set in self.__syn_set_list.values():
            syn_set.saveAsXml(out_file)
        out_file.write("</SYNSETS>\n")
        out_file.close()

    cpdef int size(self):
        """
        Returns the size of the SynSet list.

        RETURNS
        -------
        int
            The size of the SynSet list
        """
        return len(self.__syn_set_list)

    cpdef int findPathLength(self,
                             list pathToRootOfSynSet1,
                             list pathToRootOfSynSet2):
        """
        Conduct common operations between similarity metrics.

        PARAMETERS
        ----------
        pathToRootOfSynSet1 : list
            First list of Strings
        pathToRootOfSynSet2 : list
            Second list of Strings

        RETURNS
        -------
        int
            Path length
        """
        cdef int i, found_index
        for i in range(len(pathToRootOfSynSet1)):
            if pathToRootOfSynSet1[i] in pathToRootOfSynSet2:
                found_index = pathToRootOfSynSet2.index(pathToRootOfSynSet1[i])
                return i + found_index - 1
        return -1

    cpdef tuple __findLCS(self,
                          list pathToRootOfSynSet1,
                          list pathToRootOfSynSet2):
        """
        Returns depth and ID of the LCS.

        PARAMETERS
        ----------
        pathToRootOfSynSet1 : list
            First list of Strings
        pathToRootOfSynSet2 : list
            Second list of Strings

        RETURNS
        -------
        tuple
            Depth and ID of the LCS
        """
        cdef int i
        cdef str lcs_id
        for i in range(len(pathToRootOfSynSet1)):
            lcs_id = pathToRootOfSynSet1[i]
            if lcs_id in pathToRootOfSynSet2:
                return lcs_id, len(pathToRootOfSynSet1) - i + 1
        return None

    cpdef int findLCSDepth(self,
                           list pathToRootOfSynSet1,
                           list pathToRootOfSynSet2):
        """
        Returns the depth of path.

        PARAMETERS
        ----------
        pathToRootOfSynSet1 : list
            First list of Strings
        pathToRootOfSynSet2 : list
            Second list of Strings

        RETURNS
        -------
        int
            LCS depth
        """
        cdef tuple temp
        temp = self.__findLCS(pathToRootOfSynSet1, pathToRootOfSynSet2)
        if temp is not None:
            return temp[1]
        else:
            return -1

    cpdef str findLCSid(self,
                        list pathToRootOfSynSet1,
                        list pathToRootOfSynSet2):
        """
        Returns the ID of LCS of path.

        PARAMETERS
        ----------
        pathToRootOfSynSet1 : list
            First list of Strings
        pathToRootOfSynSet2 : list
            Second list of Strings

        RETURNS
        -------
        str
            LCS ID
        """
        cdef tuple temp
        temp = self.__findLCS(pathToRootOfSynSet1, pathToRootOfSynSet2)
        if temp is not None:
            return temp[0]
        else:
            return None

    cpdef SynSet percolateUp(self, SynSet root):
        """
        Finds the parent of a node. It does not move until the root, instead it goes one level up.

        PARAMETERS
        ----------
        root : SynSet
            SynSet whose parent will be find

        RETURNS
        -------
        SynSet
            Parent SynSet
        """
        cdef int i
        cdef Relation r
        for i in range(root.relationSize()):
            r = root.getRelation(i)
            if isinstance(r, SemanticRelation):
                if r.getRelationType() == SemanticRelationType.HYPERNYM \
                        or r.getRelationType() == SemanticRelationType.INSTANCE_HYPERNYM:
                    root = self.getSynSetWithId(r.getName())
                    return root
        return None

    cpdef list findPathToRoot(self, SynSet synSet):
        """
        Finds the path to the root node of a SynSets.

        PARAMETERS
        ----------
        synSet : SynSet
            SynSet whose root path will be found

        RETURNS
        -------
        list
            List of String corresponding to nodes in the path
        """
        cdef list path_to_root
        path_to_root = []
        while synSet is not None:
            if synSet.getId() in path_to_root:
                break
            path_to_root.append(synSet.getId())
            synSet = self.percolateUp(synSet)
        return path_to_root
