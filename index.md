## Introduction

On 22 January 2022, hundreds of protesters made up of political parties and civil societies took to streets of Kuala Lumpur, Malaysia to demand for the resignation of MACC Chief, Tan Sri Dato’ Sri Haji Azam bin Baki amidst the corruption scandals plaguing his tenure. As the action happened on the streets, in this resarch project, we will look for the conversations happening surrounding the events of the protest on the twitter digital space with the outcome of gaining insights on political conversations in Malaysia.

## Data Collection

About 90k tweets were pulled with twitter API's stream tweets feature with about 5% sampled for the dataset. The code for streaming the tweets can be found in the project repo: https://github.com/tehcanai/Protest-tweets-sat-22/blob/47d66a944adfd52cb8655386c39ffeba02cf468c/stream_tweets.py

Dataset: https://github.com/tehcanai/Protest-tweets-sat-22/blob/5b0905c8f76061b6abe6a06be5f632eee0317e8a/resources/sat22-1-22

### Stream Tweet Ruleset

The ruleset for the tweets to be pulled consists of words that can be found such usually in tweets concerning politics. Thus, we filtered the stream based on five tags we created based on issues which are Malay, Royals, Political Parties, Governement, and People in an attempt to pull the tweets that are actually concerning politics.

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

We attempted to look on who the influential accounts were on the day. This is measured by the frequencies of retweets and mentions of accounts as a proxy for the popularity of the accounts. 

<img src="https://github.com/tehcanai/Protest-tweets-sat-22/blob/b0ee7ba72c78e652f87731ed78c8e59f51f11d10/resources/img/overview.png" class="img-responsive" alt=""> </div>




