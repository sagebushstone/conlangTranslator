import spacy

nlp = spacy.load("en_core_web_sm")
lemmatizer = nlp.get_pipe("lemmatizer")

doc = nlp("the woods are pretty")
for token in doc:
   print(token.text, token.pos_, token.dep_, token.tag_)

# VARIABLES TO BE CHANGED IN FUNCTIONS
verbTense = ""
verbLemma = ""

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

print([token.lemma_ for token in doc])

for token in doc:
    if(token.pos_ == "VERB" or token.pos_ == "AUX"): # accounts for verbs and "be" ... not "should" or others
        verb()
        print(verbTense + "'" + token.text + " or " + verbTense + "'" + verbLemma)

