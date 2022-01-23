f = open("dataset", "r", encoding="utf-8")

spec_characters = ['\n', ',', '.', ':', '(', ')', '"', '!', '@', '#']
rmvd_words = ['@', "RT", "https", '#', '\n']

target_words = ["banjir", "kerajaan", "protes", "Azam Baki", "melayu"
                "pembangkang", "korup", "corrupt", "raja", "rakyat"]

filtered_tokens = []
pairing_words = []

for tweet in f.readlines() :
    target_words_tweet = []
    for word in target_words :
        if word in tweet :
            target_words_tweet.append(word)
    if len(target_words_tweet) >= 2 : pairing_words.append(target_words_tweet)

pow_pairs = {}
for pair in pairing_words :
    if str(pair) not in pow_pairs :
        pow_pairs[str(pair)] = 1
    if str(pair) in pow_pairs :
        pow_pairs[str(pair)] += 1

for p in pow_pairs : print(p + " : " + str(pow_pairs[p]))
        
f.close()
