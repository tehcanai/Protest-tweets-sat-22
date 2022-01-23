import matplotlib.pyplot as plt

lines_f = open("sat22-1-22", "r", encoding="utf-8")

lines = lines_f.readlines()

buffer, accounts, freq, twt_len = [], [], [], []

for l in lines :
    read_to_buffer = False
    line_chars = list(l) 
    for c in line_chars :
        if ((c == ' ') or (c == ':')) and (read_to_buffer == True): 
            read_to_buffer = False
            if (len(buffer) <= 15) and ("".join(buffer) not in accounts) and (len(line_chars) <= 280) :
                accounts.append("".join(buffer))
                freq.append(1)
                twt_len.append(len(line_chars))
            elif (len(buffer) <= 15) and ("".join(buffer) in accounts) and (len(line_chars) <= 280) :
                freq[accounts.index("".join(buffer))] += 1
                twt_len[accounts.index("".join(buffer))] += len(line_chars)
            buffer = []
        elif (read_to_buffer == True) : buffer.append(c)
        elif (c == '@') : read_to_buffer = True

avg_twt_len = []

for i in range(len(freq)) :
    avg_twt_len.append(twt_len[i]/freq[i])

plt.scatter(avg_twt_len, freq, c="black", s=5)
plt.rcParams.update({'font.size': 2})
plt.xlabel("Average tweet length ")
plt.ylabel("Quotes/retweets (sampled)")
plt.show()
