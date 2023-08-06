from io import TextIOWrapper

from AnnotatedSentence.AnnotatedPhrase cimport AnnotatedPhrase
from AnnotatedSentence.AnnotatedWord cimport AnnotatedWord
from DependencyParser.ParserEvaluationScore cimport ParserEvaluationScore
from DependencyParser.Universal.UniversalDependencyRelation cimport UniversalDependencyRelation
from MorphologicalAnalysis.MorphologicalParse cimport MorphologicalParse
from MorphologicalAnalysis.MetamorphicParse cimport MetamorphicParse


cdef class AnnotatedSentence(Sentence):

    def __init__(self,
                 fileOrStr=None,
                 fileName=None):
        """
        Converts a simple sentence to an annotated sentence

        PARAMETERS
        ----------
        fileOrStr
            Simple sentence
        """
        cdef list word_array
        cdef str line, word
        self.words = []
        word_array = []
        if fileOrStr is not None:
            if fileName is not None:
                self.__file_name = fileName
            if isinstance(fileOrStr, TextIOWrapper):
                line = fileOrStr.readline()
                fileOrStr.close()
                word_array = line.rstrip().split(" ")
            elif isinstance(self, str):
                word_array = fileOrStr.split(" ")
            for word in word_array:
                if len(word) > 0:
                    self.words.append(AnnotatedWord(word))

    cpdef list getShallowParseGroups(self):
        """
        The method constructs all possible shallow parse groups of a sentence.

        RETURNS
        -------
        list
            Shallow parse groups of a sentence.
        """
        cdef list shallow_parse_groups
        cdef AnnotatedWord word, previous_word
        cdef AnnotatedPhrase current
        cdef int i
        shallow_parse_groups = []
        previous_word = None
        current = None
        for i in range(self.wordCount()):
            word = self.getWord(i)
            if isinstance(word, AnnotatedWord):
                if previous_word is None:
                    current = AnnotatedPhrase(i, word.getShallowParse())
                else:
                    if isinstance(previous_word, AnnotatedWord) and previous_word.getShallowParse() is not None \
                            and previous_word.getShallowParse() != word.getShallowParse():
                        shallow_parse_groups.append(current)
                        current = AnnotatedPhrase(i, word.getShallowParse())
                current.addWord(word)
                previous_word = word
        shallow_parse_groups.append(current)
        return shallow_parse_groups

    cpdef bint containsPredicate(self):
        """
        The method checks all words in the sentence and returns true if at least one of the words is annotated with
        PREDICATE tag.

        RETURNS
        -------
        bool
            True if at least one of the words is annotated with PREDICATE tag; False otherwise.
        """
        cdef AnnotatedWord word
        for word in self.words:
            if isinstance(word, AnnotatedWord):
                if word.getArgument() is not None and word.getArgument().getArgumentType() == "PREDICATE":
                    return True
        return False

    cpdef bint updateConnectedPredicate(self,
                                        str previousId,
                                        str currentId):
        cdef bint modified
        cdef AnnotatedWord word
        modified = False
        for word in self.words:
            if isinstance(word, AnnotatedWord):
                if word.getArgument() is not None and word.getArgument().getId() is not None and \
                        word.getArgument().getId() == previousId:
                    word.setArgument(word.getArgument().getArgumentType() + "$" + currentId)
                    modified = True
                if word.getFrameElement() is not None and word.getFrameElement().getId() is not None and \
                    word.getFrameElement().getId() == previousId:
                    word.setFrameElement(word.getFrameElement().getFrameElementType() + "$" + \
                                         word.getFrameElement().getFrame() + "$" + currentId)
                    modified = True
        return modified

    cpdef list predicateCandidates(self, FramesetList framesetList):
        """
        The method returns all possible words, which is
        1. Verb
        2. Its semantic tag is assigned
        3. A frameset exists for that semantic tag

        PARAMETERS
        ----------
        framesetList : FramesetList
            Frameset list that contains all frames for Turkish

        RETURNS
        -------
        A list of words, which are verbs, semantic tags assigned, and framesetlist assigned for that tag.
        """
        cdef list candidate_list
        cdef AnnotatedWord word, annotated_word, next_annotated_word
        cdef int i, j
        candidate_list = []
        for word in self.words:
            if isinstance(word, AnnotatedWord):
                if word.getParse() is not None and word.getParse().isVerb() and word.getSemantic() is not None \
                        and framesetList.frameExists(word.getSemantic()):
                    candidate_list.append(word)
        for i in range(2):
            for j in range(len(self.words) - i - 1):
                annotated_word = self.words[j]
                next_annotated_word = self.words[j + 1]
                if isinstance(annotated_word, AnnotatedWord) and isinstance(next_annotated_word, AnnotatedWord):
                    if annotated_word not in candidate_list and next_annotated_word in candidate_list \
                            and annotated_word.getSemantic() is not None \
                            and annotated_word.getSemantic() == next_annotated_word.getSemantic():
                        candidate_list.append(annotated_word)
        return candidate_list

    cpdef list predicateFrameCandidates(self, FrameNet frameNet):
        """
        The method returns all possible words, which is
        1. Verb
        2. Its semantic tag is assigned
        3. A lexicalUnit exists for that semantic tag

        PARAMETERS
        ----------
        frameNet : FrameNet
            FrameNet that contains all frames for Turkish

        RETURNS
        -------
        A list of words, which are verbs, semantic tags assigned, and frame assigned for that tag.
        """
        cdef list candidate_list
        cdef AnnotatedWord word, annotated_word, next_annotated_word
        cdef int i, j
        candidate_list = []
        for word in self.words:
            if isinstance(word, AnnotatedWord):
                if word.getParse() is not None and word.getParse().isVerb() and word.getSemantic() is not None \
                        and frameNet.lexicalUnitExists(word.getSemantic()):
                    candidate_list.append(word)
        for i in range(2):
            for j in range(len(self.words) - i - 1):
                annotated_word = self.words[j]
                next_annotated_word = self.words[j + 1]
                if isinstance(annotated_word, AnnotatedWord) and isinstance(next_annotated_word, AnnotatedWord):
                    if annotated_word not in candidate_list and next_annotated_word in candidate_list \
                            and annotated_word.getSemantic() is not None \
                            and annotated_word.getSemantic() == next_annotated_word.getSemantic():
                        candidate_list.append(annotated_word)
        return candidate_list

    cpdef str getPredicate(self, int index):
        """
        Returns the nearest predicate to the index'th word in the sentence.

        PARAMETERS
        ----------
        index : int
            Word index

        RETURNS
        -------
        str
            The nearest predicate to the index'th word in the sentence.
        """
        cdef int count1, count2, i
        cdef str data
        cdef list word, parse
        count1 = 0
        count2 = 0
        data = ""
        word = []
        parse = []
        if index < self.wordCount():
            for i in range(self.wordCount()):
                word.append(self.getWord(i))
                parse.append(self.getWord(i).getParse())
            for i in range(index, -1, -1):
                if parse[i] is not None and parse[i].getRootPos() is not None and parse[i].getPos() is not None \
                        and parse[i].getRootPos() == "VERB" and parse[i].getPos() == "VERB":
                    count1 = index - i
                    break
            for i in range(index, self.wordCount() - index):
                if parse[i] is not None and parse[i].getRootPos() is not None and parse[i].getPos() is not None \
                        and parse[i].getRootPos() == "VERB" and parse[i].getPos() == "VERB":
                    count2 = i - index
                    break
            if count1 > count2:
                data = word[count1].getName()
            else:
                data = word[count2].getName()
        return data

    cpdef str getFileName(self):
        """
        Returns file name of the sentence

        RETURNS
        -------
        str
            File name of the sentence
        """
        return self.__file_name

    cpdef removeWord(self, int index):
        """
        Removes the i'th word from the sentence

        PARAMETERS
        ----------
        index : int
            Word index
        """
        self.words.pop(index)

    cpdef str toStems(self):
        """
        The toStems method returns an accumulated string of each word's stems in words {@link ArrayList}.
        If the parse of the word does not exist, the method adds the surfaceform to the resulting string.

        RETURNS
        -------
        str
             String result which has all the stems of each item in words {@link ArrayList}.
        """
        cdef AnnotatedWord annotated_word
        cdef str result
        cdef int i
        if len(self.words) > 0:
            annotated_word = self.words[0]
            if annotated_word.getParse() is not None:
                result = annotated_word.getParse().getWord().getName()
            else:
                result = annotated_word.getName()
            for i in range(1, len(self.words)):
                annotated_word = self.words[i]
                if annotated_word.getParse() is not None:
                    result = result + " " + annotated_word.getParse().getWord().getName()
                else:
                    result = result + " " + annotated_word.getName()
            return result
        else:
            return ""

    cpdef ParserEvaluationScore compareParses(self, AnnotatedSentence sentence):
        cdef ParserEvaluationScore score
        cdef UniversalDependencyRelation relation1, relation2
        score = ParserEvaluationScore()
        for i in range(self.wordCount()):
            relation1 = self.words[i].getUniversalDependency()
            relation2 = sentence.getWord(i).getUniversalDependency()
            if relation1 is not None and relation2 is not None:
                score.add(relation1.compareRelations(relation2))
        return score

    cpdef save(self):
        """
        Saves the current sentence.
        """
        self.writeToFile(self.__file_name)

    cpdef str getUniversalDependencyFormat(self, str path=None):
        cdef str result
        cdef int i
        cdef AnnotatedWord word
        if path is None:
            result = "# sent_id = " + self.getFileName() + "\n" + "# text = " + self.toString() + "\n"
        else:
            result = "# sent_id = " + path + self.getFileName() + "\n" + "# text = " + self.toString() + "\n"
        for i in range(self.wordCount()):
            word = self.getWord(i)
            result += str(i + 1) + "\t" + word.getUniversalDependencyFormat(self.wordCount()) + "\n"
        result += "\n"
        return result

    cpdef list constructLiterals(self, WordNet wordNet, FsmMorphologicalAnalyzer fsm, int wordIndex):
        """
        Creates a list of literal candidates for the i'th word in the sentence. It combines the results of
        1. All possible root forms of the i'th word in the sentence
        2. All possible 2-word expressions containing the i'th word in the sentence
        3. All possible 3-word expressions containing the i'th word in the sentence

        PARAMETERS
        ----------
        wordNet : WordNet
            Turkish wordnet
        fsm : FsmMorphologicalAnalyzer
            Turkish morphological analyzer
        wordIndex : int
            Word index

        RETURNS
        -------
        list
            List of literal candidates containing all possible root forms and multiword expressions.
        """
        cdef AnnotatedWord word, first_succeeding_word, second_succeeding_word
        cdef list possible_literals
        cdef MorphologicalParse morphologicalpParse
        cdef MetamorphicParse metamorphic_parse
        word = self.getWord(wordIndex)
        possible_literals = []
        if isinstance(word, AnnotatedWord):
            morphological_parse = word.getParse()
            metamorphic_parse = word.getMetamorphicParse()
            possible_literals.extend(wordNet.constructLiterals(morphological_parse.getWord().getName(),
                                                               morphological_parse,
                                                               metamorphic_parse,
                                                               fsm))
            first_succeeding_word = None
            second_succeeding_word = None
            if self.wordCount() > wordIndex + 1:
                first_succeeding_word = self.getWord(wordIndex + 1)
                if self.wordCount() > wordIndex + 2:
                    second_succeeding_word = self.getWord(wordIndex + 2)
            if first_succeeding_word is not None and isinstance(first_succeeding_word, AnnotatedWord):
                if second_succeeding_word is not None and isinstance(second_succeeding_word, AnnotatedWord):
                    possible_literals.extend(wordNet.constructIdiomLiterals(fsm,
                                                                            word.getParse(),
                                                                            word.getMetamorphicParse(),
                                                                            first_succeeding_word.getParse(),
                                                                            first_succeeding_word.getMetamorphicParse(),
                                                                            second_succeeding_word.getParse(),
                                                                            second_succeeding_word.getMetamorphicParse()))
                possible_literals.extend(wordNet.constructIdiomLiterals(fsm,
                                                                        word.getParse(),
                                                                        word.getMetamorphicParse(),
                                                                        first_succeeding_word.getParse(),
                                                                        first_succeeding_word.getMetamorphicParse()))
        return possible_literals

    cpdef list constructSynSets(self,
                                WordNet wordNet,
                                FsmMorphologicalAnalyzer fsm,
                                int wordIndex):
        """
        Creates a list of synset candidates for the i'th word in the sentence. It combines the results of
        1. All possible synsets containing the i'th word in the sentence
        2. All possible synsets containing 2-word expressions, which contains the i'th word in the sentence
        3. All possible synsets containing 3-word expressions, which contains the i'th word in the sentence

        PARAMETERS
        ----------
        wordNet : WordNet
            Turkish wordnet
        fsm : FsmMorphologicalAnalyzer
            Turkish morphological analyzer
        wordIndex : int
            Word index

        RETURNS
        -------
        list
            List of synset candidates containing all possible root forms and multiword expressions.
        """
        cdef AnnotatedWord word, first_preceding_word, second_preceding_word
        cdef AnnotatedWord first_succeeding_word, second_succeeding_word
        cdef list possible_syn_sets
        cdef MorphologicalParse morphological_parse
        cdef MetamorphicParse metamorphic_parse
        word = self.getWord(wordIndex)
        possible_syn_sets = []
        if isinstance(word, AnnotatedWord):
            morphological_parse = word.getParse()
            metamorphic_parse = word.getMetamorphicParse()
            possible_syn_sets.extend(wordNet.constructSynSets(morphological_parse.getWord().getName(),
                                                              morphological_parse,
                                                              metamorphic_parse,
                                                              fsm))
            first_preceding_word = None
            second_preceding_word = None
            first_succeeding_word = None
            second_succeeding_word = None
            if wordIndex > 0:
                first_preceding_word = self.getWord(wordIndex - 1)
                if wordIndex > 1:
                    second_preceding_word = self.getWord(wordIndex - 2)
            if self.wordCount() > wordIndex + 1:
                first_succeeding_word = self.getWord(wordIndex + 1)
                if self.wordCount() > wordIndex + 2:
                    second_succeeding_word = self.getWord(wordIndex + 2)
            if first_preceding_word is not None and isinstance(first_preceding_word, AnnotatedWord):
                if second_preceding_word is not None and isinstance(second_preceding_word, AnnotatedWord):
                    possible_syn_sets.extend(wordNet.constructIdiomSynSets(fsm, second_preceding_word.getParse(),
                                                                         second_preceding_word.getMetamorphicParse(),
                                                                         first_preceding_word.getParse(),
                                                                         first_preceding_word.getMetamorphicParse(),
                                                                         word.getParse(), word.getMetamorphicParse()))
                possible_syn_sets.extend(wordNet.constructIdiomSynSets(fsm, first_preceding_word.getParse(),
                                                                     first_preceding_word.getMetamorphicParse(),
                                                                     word.getParse(), word.getMetamorphicParse()))
            if first_succeeding_word is not None and isinstance(first_succeeding_word, AnnotatedWord):
                if second_succeeding_word is not None and isinstance(second_succeeding_word, AnnotatedWord):
                    possible_syn_sets.extend(wordNet.constructIdiomSynSets(fsm, word.getParse(),
                                                                         word.getMetamorphicParse(),
                                                                         first_succeeding_word.getParse(),
                                                                         first_succeeding_word.getMetamorphicParse(),
                                                                         second_succeeding_word.getParse(),
                                                                         second_succeeding_word.getMetamorphicParse()))
                possible_syn_sets.extend(wordNet.constructIdiomSynSets(fsm, word.getParse(), word.getMetamorphicParse(),
                                                                     first_succeeding_word.getParse(),
                                                                     first_succeeding_word.getMetamorphicParse()))
        return possible_syn_sets
