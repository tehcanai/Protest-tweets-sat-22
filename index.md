## An Analysis of Tweets Surrounding The 22 January 2022 Protests on MACC 

## Introduction

On 22 January 2022, hundreds of protesters made up of political parties and civil societies took to streets of Kuala Lumpur, Malaysia to demand for the resignation of MACC Chief, Tan Sri Dato’ Sri Haji Azam bin Baki amidst the corruption scandals plaguing his tenure. As the action happened on the streets, in this resarch project, we will look for the conversations happening surrounding the events of the protest on the twitter digital space with the outcome of gaining insights on political conversations in Malaysia.

## Data Collection

About 90k tweets were pulled with twitter API's stream tweets feature with about 5% sampled for the dataset. The code for streaming the tweets can be found in the project repo: <href  src ="https://github.com/tehcanai/Protest-tweets-sat-22/blob/47d66a944adfd52cb8655386c39ffeba02cf468c/stream_tweets.py">here</href>

### Stream Tweet Ruleset

The ruleset for the tweets to be pulled consists of words that can be found such usually in tweets concerning politics. Thus, we filtered the stream based on five tags we created based on issues which are Malay, Royals, Political Parties, Governement, and People in an attempt to pull the tweets that are actually concerning politics. There are no tags related to protests, corruption, or the MACC as we intend to check if these issues will be placed in similar contexts with the created tags by twitter users.

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

We attempted to look on what type of tweets that were popular to be retweeted and shared by twitter users. The graph is as below:

![graph-popularity-length](img/Figure_1.png)

From the graph, the best performing tweets were less than 150 words and most tweets did not reach more than 20 sampled retweets/quotes. We can probably hypotesize that the most popular tweets are short in nature for political tweets. Whether this affects all tweets in general, we do not know.

### Adjacent Issues in Tweets


