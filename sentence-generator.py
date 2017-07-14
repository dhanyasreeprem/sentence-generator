import random
num_list = ["dog" , "donut","fortune cookies", "donkey", "Melissa"]
prepositions = "under", "over", "behind", "beneath","inside", "into","near", "atop","on";
article_list = ["a", "the"];
verb_list = ["sings", "eats", "codes", "studies", "cries","laughes", "hops", "mops","sleeps","runs"];
adjective_list = ["ugly", "happy","tired","creepy","gloomy","brave","fierce","calm","studious","intelligent"];
adverb_list = ["lazily","sadly","productively","happily","gleafully,"];

def noun_phrase():
    return random.choice(article_list) + " " + random.choice(adjective_list) + " " + random.choice(num_list);

def prepositional_phrase():
    return random.choice(prepositions) +" " +  noun_phrase();

def verb_phrase():
    return random.choice(adverb_list) + " " + random.choice(verb_list);

def sentence():
    return noun_phrase() + " " + verb_phrase() + " " + prepositional_phrase()


print(sentence());
