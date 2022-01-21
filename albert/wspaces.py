def wspaces(sentence):
    # words with no content
    rwords = ["el", "la","a","en","de","y","una","uno","las","los","ellos","ellas","eso","esto","es","un","sus","the","se", "para","del","e","que", "no"] 

    for letter in sentence:
        if(letter == ' '):
            # index of the whitespace
            wspace = sentence.index(letter)

            # remove all words with no content (ej: 'del')
            if(sentence[0:wspace].lower() not in rwords):
                #print(sentence[0:wspace].lower())
                yield sentence[0:wspace].lower()
                
                # title is now a new list without the last letter
                sentence = sentence[wspace+1:]
            else:
                # title is now a new list without the last letter
                sentence = sentence[wspace+1:]
        
    #print(sentence.lower())
    yield sentence.lower()

    pass