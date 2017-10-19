from os import listdir
class Reviewer():
    def __init__(self):
        pass

sub_neg_train_r = "data/subset/train/neg/"
sub_pos_train_r = "data/subset/train/pos/"

# generates the list of stop words, and sorts the list
stop_words_file = open("data/stop_words.txt")
stop_words = []
for l in stop_words_file:
    stop_words.append(l.strip())
stop_words.sort()
print(stop_words)


def make_legal_format(text):
    # makes the text lower case and alpha numerical.
    # NB! Currently joins words when a character is removed, if this is not desirable, the second commented if clause
    # should be used instead of the current one.
    t = text.lower()
    t_length = len(t)
    i = 0
    while i < (t_length):
        if not t[i].isalnum() and t[i] != ' ':
            t = t[:i] + t[i+1:]
            # both indexes needs to be subtracted from since the remaining indexes has changed.
            t_length -= 1
            i -= 1

        # if clause for use if replacing chars with spaces is preferred
        # if not t[i].isalnum() and t[i] != ' ':
        #     t = t[:i] +' '+ t[i + 1:]
        i += 1
    return t

def remove_stop_words(text):
    # make the string into a list, remove duplicates, and remove stop words.
    t = text.split()
    t = list(set(t))
    for w in t:
        if w in stop_words:
            t.remove(w)
    return t

def train(directory, flavour):
    reviews = listdir(directory)
    for i in reviews:
        current_review = open(directory + i)
        review_string = ''
        for l in current_review:
            review_string += make_legal_format(l)
            print(l)

        current_review.close()



class Review():
    def __init__(self, common_words):
        self.common_words = common_words