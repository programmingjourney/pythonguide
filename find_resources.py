# Inputs:
# resources
# recipe
# Output
# produce - how much

import spacy
spacy.load('en_core_web_sm')
from spacy.lang.en import English

parser = English()
example = '''
2 tablespoons olive oil
8 bone-in, skin-on chicken thighs
450 grams (1 lb) baby potatoes cleaned, cut in half or quarters
1 red onion peeled and roughly chopped
2 cloves garlic minced
2 teaspoons dried oregano
2 teaspoon fresh thyme finely chopped
1/2 teaspoon paprika
salt and freshly ground black pepper to taste
'''

# Code "borrowed" from somewhere?!
def entities(example, show=False):
    if show: print(example)
    parsedEx = parser(example)

    print("-------------- entities only ---------------")
    # if you just want the entities and nothing else, you can do access the parsed examples "ents" property like this:
    ents = list(parsedEx.ents)
    tags = {}
    for entity in ents:
        # print(entity.label, entity.label_, ' '.join(t.orth_ for t in entity))
        term = ' '.join(t.orth_ for t in entity)
        if ' '.join(term) not in tags:
            tags[term] = [(entity.label, entity.label_)]
        else:
            tags[term].append((entity.label, entity.label_))
    print(tags)

entities(example)