import spacy
import json

def extract_keywords(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    keywords = []
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN", "VERB"]:  # Filter for nouns, proper nouns, and verbs
            keywords.append(token.text)
    
    return keywords

def main():
    user_input = input("Enter your text: ")
    keywords = extract_keywords(user_input)
    
    output = {
        "keywords": keywords
    }
    
    json_output = json.dumps(output)
    print(json_output)

if __name__ == "__main__":
    main()
