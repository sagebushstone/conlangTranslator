import spacy

nlp = spacy.load("en_core_web_sm")
lemmatizer = nlp.get_pipe("lemmatizer")

doc = nlp("i want to eat")
for token in doc:
   print(token.text, token.pos_, token.dep_, token.tag_)

# VARIABLES TO BE CHANGED IN FUNCTIONS
verbTense = ""
verbLemma = ""

performer = ""


# VERB FUNCTION
def verb():
    global verbTense
    global verbLemma

    if(token.tag_ == "VBD" or token.tag_ == "VBN"):
        verbTense = "mu"
    elif(token.tag_ == "VBP" or token.tag_ == "VBZ" or token.tag_ == "VBG"):
        verbTense = "na"
    elif(token.tag_ == "VB"):
        verbTense = "we"

    verbLemma = token.lemma_
    return

# PRONOUN/SUBJECT FUNCTION
def subject():
    global performer

    if(token.text == "I" or token.text == "me"):
        performer = "eo"
    elif(token.text == "you"):
        performer = "a"
    elif(token.text == "we"):
        performer = "as"
    elif(token.text == "he"):
        performer = "e"
    elif(token.text == "she"):
        performer = "u"
    elif(token.text == "they" or token.tag_ == "NNP" or token.tag_ == "NNS"): # how to accomodate for sing. they? and mult he/she for that matter?
        performer = "os"
    else:
        otherSub() # NEED TO MAKE EXTRA FUNCTION FOR OTHER POSSIBILITIES... IT, THAT, WHO, WHICH... including plurals
    return

# OTHER SUBJECT FUNCTION
def otherSub():
    global performer
    if(token.text == "that"):
        performer = "kata"
    elif(token.text == "this"):
        performer = "kat"
    else: # need to add in "those"
        performer = "dat"

    return

print([token.lemma_ for token in doc])

for token in doc:
    if(token.pos_ == "VERB" or token.pos_ == "AUX"): # accounts for verbs and "be" ... not "should" or others
        verb()
        #print(verbTense + "'" + token.text + " or " + verbTense + "'" + verbLemma)
    if(token.dep_ == "nsubj"):
        subject()

print(verbTense + "'" + performer + "'" + verbLemma)

