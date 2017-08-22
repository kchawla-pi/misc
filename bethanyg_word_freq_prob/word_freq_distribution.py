import string
import operator

# A note, I used ordered dict as it made it easier for me to visualize the data and solve
# it when it is in order. using a dict does not change the answer.
def make_word_freq(text:str) -> dict:
    # Create word frequency dict.
    text = text.lower()
    only_letters = [char_ for char_ in text if char_ in string.ascii_letters or char_ == ' ']
    words_list = ''.join(only_letters).split()
    word_freq = {word: words_list.count(word) for word in words_list}
    return word_freq


def make_freq_distrib(word_freq: dict) -> dict:
    # create dict of frequecy of word frequencies
    freq_distrib = {v: list(word_freq.values()).count(v) for k, v in word_freq.items()}
    freq_distrib = dict(sorted(freq_distrib.items(), key=operator.itemgetter(1)))
    return freq_distrib


def make_word_freq_distrib(freq_distrib: dict) -> dict:
    # Create dict where values are list of frequencies greater than frequency of current key
    freq_greater = {k: [in_v for in_v in freq_distrib.values() if in_v > v] for k, v in
                    freq_distrib.items()}
    # sum the list of greater frequency(cumsum final value) and divide by total frequency.
    freq_total = sum(freq_distrib.values())
    word_freq_distrib = {k: sum(v) / freq_total for k, v in freq_greater.items()}
    return word_freq_distrib

text = '''This is my test text.  We're keeping this text short to keep things manageable.
    The quick brown fox jumps over the lazy lazy lazy dog. Yes, the dog was very lazy.'''
''' {3: 0.9130434782608695, 4: 0.9130434782608695, 2: 0.782608695652174, 1: 0.0} '''
word_freq = make_word_freq(text)
freq_distrib = make_freq_distrib(word_freq)
word_freq_distrib = make_word_freq_distrib(freq_distrib)
print(word_freq_distrib)
