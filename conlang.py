import spacy
import mysql.connector
import os

# loaded from spacy
nlp = spacy.load("en_core_web_sm")
lemmatizer = nlp.get_pipe("lemmatizer")

# grabs mysql password from environmental variable
sqlpass = os.getenv("sqlpass")

# connect to mysql database of vocabulary
vocab = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = sqlpass,
    database = "keshkavocab"
)
cursor = vocab.cursor()

doc = nlp("animals")

engDepend = []
for token in doc:
    engDepend.append(token.dep_)
    print(token.text, token.pos_, token.dep_, token.tag_)

# VARIABLES TO BE CHANGED IN FUNCTIONS
verbTense = ""
verbLemma = ""

keshkaNoun = ""
keshkaSoB = ""

performer = ""


# NOUN FUNCTION
def noun():
    global keshkaNoun
    global keshkaSoB
    cursor.execute("SELECT keshka FROM keshkavocab.vocab WHERE english='%s'" % (token.lemma_)) # gets keshka translation of noun
    keshkaNoun = cursor.fetchall()
    cursor.execute("SELECT stateofbeing FROM keshkavocab.vocab WHERE english='%s'" % (token.lemma_)) # gets state of being of noun
    stateOfBeing = cursor.fetchone()[0]
    if(stateOfBeing == "animate"):
        if(token.tag_ == "NN"):
            keshkaSoB = "e"
        else:
            keshkaSoB = "es"
    elif(stateOfBeing == "inanimate"):
        if(token.tag_ == "NN"):
            keshkaSoB = "u"
        else:
            keshkaSoB = "us"
    elif(stateOfBeing == "abstract"):
        if(token.tag_ == "NN"):
            keshkaSoB = "o"
        else:
            keshkaSoB = "os"

    print(stateOfBeing)
    print(keshkaSoB)
    return

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
    if(token.dep_ == "nsubj"):
        subject()
    if(token.pos_ == "NOUN"):
        noun()

print(verbTense + "'" + performer + "'" + verbLemma)
print(engDepend)



