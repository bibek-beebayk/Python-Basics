from random import randint
import copy

# template for the mad libs
story = (
    "It's {}! " +
    "{} is coming over to get ready to {} with me! " +
    "{} helped us {} pumpkins, and now {} and I are going to put them in the {}. " +
    "We are full after eating {}, and are ready to go now! " +
    "{} told us to watch out for the {} down the street because it is scary with {} webs and broken {}. " +
    "It's the house where {} and {} live! " +
    "But I'm not {}! " +
    "Happy {} to everyone from {}!"
)

# print(type(story))

word_dict = {
    'holiday': ['Halloween', 'Christmas', 'Thanksgiving', 'Hannukah', 'Dashain', 'Tihar', 'Holi', 'La Tomatina', 'Mardi Gras'],

    'person': ['Jack', 'Amy', 'Priest', 'Lawyer', 'Doctor', 'John', 'Henry', 'Emily', 'Bibek', 'Ali', 'Buddha', 'Christ', 'Hitler', 'Obama', 'Biden', 'Bin Laden', 'Modi', 'Churchill', 'Ed Sheran', 'Eminem', 'Kallu Kaliya', 'Gabbar Singh', 'Mogambo', 'Picasso', 'Tenali Rama', 'Birbal', 'Betal', 'Madam Curie', 'Einstein', 'Bob Marley', 'Michael Jackson', 'The Rock', 'Da Vinci', 'Charlie Chaplin', 'Shaakal', 'Hanuman', 'Spiderman', 'Iron Man', 'Batman', 'The Hulk', 'Loki', 'Vasco De Gama', 'Socrates'],

    'action': ['play', 'fight', 'read', 'study', 'hang out', 'jump', 'eat', 'work', 'drink', 'drive', 'walk', 'talk', 'catch', 'listen', 'cook', 'run', 'hump', 'give', 'climb', 'wait', 'wash', 'knit', 'masturbate', 'crawl', 'smell', 'sew', 'dream'],

    'place': ['church', 'backyard', 'kitchen', 'roof', 'bathroom', 'living room', 'woods', 'balcony', 'passage', 'hallway', 'garage', 'warehouse', 'basement', 'bedroom'],

    'food': ['chips', 'fries', 'coke', 'cake', 'tacos', 'momos', 'chowmein', 'burger', 'sandwich', 'dhido', 'curry', 'chicken fry', 'chicken chilly', 'veg rolls', 'cereals', 'dal bhat', 'chapati', 'samosa', 'sizzler'],

    'bug': ['spider', 'lice', 'bedbug', 'ant', 'cockroach', 'flies', 'fleas', 'mite', 'mosquito', 'termite', 'tick'],

    'thing': ['table', 'chair', 'bed', 'hanger', 'bones', 'sofa', 'rack', 'cupboard', 'log', 'tv', 'fridge', 'cooler'],

    'feeling': ['happy', 'sad', 'scared', 'calm', 'bored', 'awkward', 'anxious', 'disgusted', 'excited', 'interested', 'nostalgic', 'sympathetic'],

}


def get_word(type, local_dict):
    words = local_dict[type]
    # print(words)
    count = len(words)-1
    # print(count)
    index = randint(0, count)
    # print(index)
    word = words[index]
    # print(word)
    local_dict[type].pop(index)
    # print(local_dict[type])
    return word

# print(get_word('bug', word_dict))


def create_story():
    print(story.format(
        get_word('holiday', word_dict),
        get_word('person', word_dict),
        get_word('action', word_dict),
        get_word('person', word_dict),
        get_word('action', word_dict),
        get_word('person', word_dict),
        get_word('place', word_dict),
        get_word('food', word_dict),
        get_word('person', word_dict),
        get_word('place', word_dict),
        get_word('bug', word_dict),
        get_word('thing', word_dict),
        get_word('person', word_dict),
        get_word('person', word_dict),
        get_word('feeling', word_dict),
        get_word('holiday', word_dict),
        get_word('person', word_dict),
    )
)

create_story()
