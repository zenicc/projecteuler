''' code for Bigrams from https://www.youtube.com/watch?v=PaCmpygFfXo '''

# create dictionary of consecutive pairs of letters with a count of their frequency
b = {}

w = "marionmma"

# this separates the word into consecutive pairs with a control character at the start and end
chs = ["<S>"] + list(w) + ["<E>"]
for ch1, ch2 in zip(chs, chs[1:]):
    bigram = (ch1, ch2)
    b[bigram] = b.get(bigram, 0) + 1
print(b)
