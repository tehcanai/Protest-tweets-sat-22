## An Analysis of Tweets Surrounding The 22 January 2022 Protests on MACC 

## Introduction

On 22 January 2022, hundreds of protesters made up of political parties and civil societies took to streets of Kuala Lumpur, Malaysia to demand for the resignation of MACC Chief, Tan Sri Dato’ Sri Haji Azam bin Baki amidst the corruption scandals plaguing his tenure. As the action happened on the streets, in this resarch project, we will look for the conversations happening surrounding the events of the protest on the twitter digital space with the outcome of gaining insights on political conversations in Malaysia.

## Data Collection

About 90k tweets were pulled with twitter API's stream tweets feature with about 5% sampled for the dataset. The code for streaming the tweets can be found in the project repo: <href  src ="https://github.com/tehcanai/Protest-tweets-sat-22/blob/47d66a944adfd52cb8655386c39ffeba02cf468c/stream_tweets.py">here</href>

Dataset: <href src="https://github.com/tehcanai/Protest-tweets-sat-22/blob/5b0905c8f76061b6abe6a06be5f632eee0317e8a/resources/sat22-1-22">here</href>

### Stream Tweet Ruleset

The ruleset for the tweets to be pulled consists of words that can be found such usually in tweets concerning politics. Thus, we filtered the stream based on five tags we created based on issues which are Malay, Royals, Political Parties, Governement, and People in an attempt to pull the tweets that are actually concerning politics. There are no tags related to protests, corruption, or the MACC as we intend to check if these issues will be placed in similar contexts with the created tags by twitter accounts.

Ruleset:
```markdown
"value": "melayu OR melayu islam OR ketuanan melayu OR bangsa melayu",
"tag": "melayu"

"value": "sultan melayu OR agong OR raja melayu",
"tag": "sultan"
 
"value": "umno OR pakatan harapan OR DAP malaysia OR Barisan Nasional",
"tag": "parti politik"

"value": "Kerajaan OR gov malaysia OR malaysian government OR gomen OR kjaan",
"tag": "Kjaan"
 
"value": "rakyat OR marhaen OR negara",
"tag": "negara"
 ```
## Analysis and Results

### Popularity vs Tweet Length

We attempted to look on who the influential accounts were on the day. This is measured by the frequencies of retweets and mentions of accounts as a proxy for the popularity of the accounts. Thus, we parsed the dataset for accounts and averaged the tweet lengths the accounts are mentioned on. The plot is as below:

<img url="https://github.com/tehcanai/Protest-tweets-sat-22/blob/b0ee7ba72c78e652f87731ed78c8e59f51f11d10/resources/img/overview.png">

From the graph, the top influential accounts are identified as abolqazCTG, aminlandak, syedAkramin, jedildzuhrie, and H_Bakkaniy. From a quick search accounts, we can check for the tweets that were influential during the protests

abolqazCTG
<blockquote class="twitter-tweet"><p lang="in" dir="ltr">Azam Baki ni mesti boss level lain ni. Tutup KL sampai macam ni.<br><br>Efficient juga PDRM ni. Boleh divert dan kerah 1,000 orang. Time banjir dekat mana?<br><br>Untuk rakyat punya lembab, lawan rakyat laju je. Faceless tools of cowardice oppressors.<a href="https://twitter.com/hashtag/TangkapAzamBaki?src=hash&amp;ref_src=twsrc%5Etfw">#TangkapAzamBaki</a></p>&mdash; Abol The CrashTestGuy Qaz (@AbolqazCTG) <a href="https://twitter.com/AbolqazCTG/status/1484695230591152128?ref_src=twsrc%5Etfw">January 22, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

<img url="https://github.com/tehcanai/Protest-tweets-sat-22/blob/b0ee7ba72c78e652f87731ed78c8e59f51f11d10/resources/img/med_accs.png"></img>

