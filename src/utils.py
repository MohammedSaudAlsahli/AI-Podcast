from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NEWS_API_KEY: str
    OPENROUTER_API_KEY: str
    debug: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


SYSTEM_PROMPT = """You are a world-class podcast producer for the weekly show "The Weekly Roundup", tasked with transforming the provided news articles into detailed, engaging, and interactive podcast scripts. The goal is to create natural, lively, and entertaining conversations between the host (Emma) and guest (John) that include humor, personal comments, and thoughtful insights.
  # Steps to Follow:

  ## 1. Analyze the Input:
  Carefully examine the week's news articles, identifying key topics, points, and impactful stories. Prioritize:
  - Breaking news or major stories that defined the week.
  - Topics that are surprising, thought-provoking, or highly relevant to a wide audience.
  - A mix of topics to reflect diverse interests (e.g., science, politics, sports, culture, etc.).

  List your findings under the `<analysis>` section.

  ---

  ## 2. Brainstorm Ideas:
  In the `<scratchpad>` section, brainstorm ways to present these stories in a fun and engaging way. Consider:
  - Crafting hooks or openers for each story to grab attention.
  - Adding humor, relatable anecdotes, or hypothetical scenarios to make the content lively.
  - Posing open-ended or humorous questions to encourage interaction.
  - Introducing natural interruptions or playful disagreements between the host and guest.

  ---

  ## 3. Craft the Dialogue:
  Develop a natural, lively, and interactive flow between the two hosts, Emma and John. Their dynamic should:
  - Feel like a real conversation, with natural interruptions, jokes, and banter.
  - Include thoughtful insights but also light-hearted moments.
  - Ensure both Emma and John contribute actively, reacting to each other's comments.

  ### Rules for the Dialogue:
  - **Emma** (host) initiates the conversation and guides the discussion.
  - **John** (guest) reacts, adds insights, and occasionally interrupts with jokes or comments.
  - The conversation should:
    - Include playful banter and humor.
    - Allow for spontaneous reactions (e.g., surprise, laughter, light-hearted teasing).
    - Feature interruptions or interjections that feel natural.
    - Be highly interactive, with both hosts building on each other’s ideas.
  - Ensure all facts and information are substantiated by the input news articles.
  - Maintain a PG-rated conversation suitable for all audiences.

  ---

  ## Summarize Key Insights:
  Weave a summary of the key points into the closing part of the dialogue. This should feel like a casual conversation, with both hosts reflecting on the week’s stories. End with a thought-provoking question or call-to-action for listeners.

  ---

  ## Maintain Authenticity:
  Create realistic and engaging dialogue by including:
  - Moments of genuine curiosity or surprise.
  - Playful disagreements or debates on certain points.
  - Personal anecdotes or relatable examples.
  - Light-hearted humor to keep the tone casual and entertaining.

  ---

  ## Consider Pacing and Structure:
  - Start with a strong hook or playful comment to grab attention.
  - Gradually build complexity as the discussion progresses.
  - Include "breather" moments with jokes or relatable tangents to balance heavier topics.
  - End on a high note, leaving listeners with something to think about or laugh about.

  ---

  ## TONE:
  The tone of the podcast should be casual, friendly, humorous, and engaging.

  ---

  ## DURATION:
  Aim for a length of **15-25 minutes per episode**, ensuring detailed discussions for every story.

  ---

  ## OUTPUT FORMAT:
  The output must be a valid JSON object with the following structure:

  ```json
  {
    "podcastTitle": "The Weekly Roundup",
    "hosts": ["Emma", "John"],
    "script": [
      {
        "host": "Emma",
        "line": "Hi John, how was your week?"
      },
      {
        "host": "John",
        "line": "It’s been great, Emma! But not as great as England's performance in the ODI match."
      },
      {
        "host": "Emma",
        "line": "Oh, absolutely! That final game against the West Indies—what a thriller! Did you see the crowd?"
      },
      {
        "host": "John",
        "line": "I did! And, honestly, I think the crowd was more energetic than my morning coffee. Did you see that guy in the bright red wig?"
      },
      {
        "host": "Emma",
        "line": "How could I miss him? He looked like he was auditioning for a superhero movie. But seriously, the way England's bowlers performed was just... *chef’s kiss*."
      },
      {
        "host": "John",
        "line": "Totally. But can we talk about that dropped catch by West Indies? I mean, I haven’t seen something that bad since I tried to assemble IKEA furniture."
      },
      {
        "host": "Emma",
        "line": "Ha! At least IKEA comes with instructions. What do you think this win means for England's momentum going forward?"
      },
      {
        "host": "John",
        "line": "It’s huge. They’ve got the Ashes coming up, and if they keep this form, Australia’s in trouble. By the way, did you notice how calm the captain was under pressure? I’d be panicking if I had that much responsibility."
      },
      {
        "host": "Emma",
        "line": "Exactly! I’d be like, 'Can someone else take over? I just want a cup of tea.' Anyway, moving on—let’s talk about that Rubin Observatory story from Chile."
      },
      {
        "host": "John",
        "line": "Ah, yes! Mapping the universe. You know, Emma, if I ever disappeared, I’d probably be hiding in that observatory. Just me, the stars, and no Wi-Fi."
      }
    ]
}```"""

TEST_NEWS = """ [
    {
        "source": {
            "id": "bbc-news",
            "name": "BBC News"
        },
        "author": null,
        "title": "Watch: England v West Indies, third ODI highlights",
        "description": "Highlights from the County Ground in Taunton as England women take on the West Indies in the final encounter of a three-match one-day international series.",
        "url": "https://www.bbc.co.uk/iplayer/episode/m002dg80/womens-odi-cricket-2025-highlights-england-v-west-indies-third-odi",
        "urlToImage": "https://ichef.bbci.co.uk/images/ic/1200x675/p0lfwlm1.jpg",
        "publishedAt": "2025-06-07T22:09:15Z",
        "content": "Highlights from the County Ground in Taunton as England women take on the West Indies in the final encounter of a three-match one-day international series."
    },
    {
        "source": {
            "id": "bbc-news",
            "name": "BBC News"
        },
        "author": null,
        "title": "Tech Now",
        "description": "Ione Wells has behind the scenes access to the Rubin Observatory in Chile's Atacama Desert, while Paul Carter visits an Amazon warehouse introducing a new robot with a sense of touch.",
        "url": "https://www.bbc.co.uk/iplayer/episode/m002dgb9/tech-now-rubin-observatory-mapping-the-universe",
        "urlToImage": "https://ichef.bbci.co.uk/images/ic/1200x675/p0lgtktm.jpg",
        "publishedAt": "2025-06-07T01:00:00Z",
        "content": "Ione Wells has behind the scenes access to the Rubin Observatory in Chile's Atacama Desert, while Paul Carter visits an Amazon warehouse introducing a new robot with a sense of touch.\u00a0More"
    },
    {
        "source": {
            "id": "bbc-news",
            "name": "BBC News"
        },
        "author": "BBC World Service",
        "title": "How life is changing in Syria",
        "description": "For well over a decade, civil war blighted the lives of Syrians, as rebel forces battled against former President Bashar al-Assad and his brutal regime. More than 600,000 people were killed and 12 million others were forced from their homes during this time. \u2026",
        "url": "https://www.bbc.co.uk/programmes/p0lgvvq4",
        "urlToImage": "https://ichef.bbci.co.uk/images/ic/1200x675/p0lgvvsn.jpg",
        "publishedAt": "2025-06-07T00:30:00Z",
        "content": "For well over a decade, civil war blighted the lives of Syrians, as rebel forces battled against former President Bashar al-Assad and his brutal regime. More than 600,000 people were killed and 12 mi\u2026 [+953 chars]"
    },
    {
        "source": {
            "id": "bbc-news",
            "name": "BBC News"
        },
        "author": "BBC World Service",
        "title": "Why does Moldova matter to Putin?",
        "description": "Moldova is a country torn between pro-Western and pro-Russian factions. In September this year, Moldovans will vote for a new leadership, and pro-European observers are worried that Russia will try to influence the outcome of these elections. Why? Natasha Mat\u2026",
        "url": "https://www.bbc.co.uk/programmes/p0lgc942",
        "urlToImage": "https://ichef.bbci.co.uk/images/ic/1200x675/p0hqg7fh.jpg",
        "publishedAt": "2025-06-07T12:30:00Z",
        "content": "Moldova is a country torn between pro-Western and pro-Russian factions. In September this year, Moldovans will vote for a new leadership, and pro-European observers are worried that Russia will try t\u2026 [+395 chars]"
    },
    {
        "source": {
            "id": "cnn",
            "name": "CNN"
        },
        "author": null,
        "title": "Federal judge approves $2.8B settlement, paving way for US colleges to pay athletes millions",
        "description": "A federal judge signed off on arguably the biggest change in the history of college sports on Friday, clearing the way for schools to begin paying their athletes millions of dollars as soon as next month as the multibillion-dollar industry shreds the last ves\u2026",
        "url": "https://www.cnn.com/2025/06/06/sport/settlement-colleges-pay-athletes-millions-spt",
        "urlToImage": "https://media.cnn.com/api/v1/images/stellar/prod/2025-03-26t192854z-1332456188-mt1usatoday25772182-rtrmadp-3-ncaa-basketball-ncaa-tournament-west-regional-practice.jpg?c=16x9&q=w_800,c_fill",
        "publishedAt": "2025-06-07T02:45:26Z",
        "content": "A federal judge signed off on arguably the biggest change in the history of college sports Friday, clearing the way for schools to begin paying their athletes millions of dollars as soon as next mont\u2026 [+6036 chars]"
    },
    {
        "source": {
            "id": "cnn",
            "name": "CNN"
        },
        "author": "Issy Ronald",
        "title": "Canadian teenager Summer McIntosh smashes 400m freestyle world record",
        "description": "Canadian teenager Summer McIntosh smashed the 400m freestyle world record in some style on Saturday, recording a time of 3:54.18 at the Canadian Swimming Trials.",
        "url": "https://www.cnn.com/2025/06/08/sport/summer-mcintosh-400m-freestyle-world-record-spt",
        "urlToImage": "https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2164680929.jpg?c=16x9&q=w_800,c_fill",
        "publishedAt": "2025-06-08T11:57:00Z",
        "content": "Canadian teenager Summer McIntosh smashed the 400m freestyle world record in some style on Saturday, recording a time of 3:54.18 at the Canadian Swimming Trials.\r\nThat time trimmed more than a second\u2026 [+1321 chars]"
    },
    {
        "source": {
            "id": "cnn",
            "name": "CNN"
        },
        "author": "Jacob Lev",
        "title": "Texas routs Texas Tech to secure first Women\u2019s College World Series title in program history",
        "description": "The Texas Longhorns won the Women\u2019s College World Series in dominant fashion, blowing out Texas Tech 10-4 in Friday\u2019s winner-take-all Game 3 to clinch the program\u2019s first-ever national championship in softball.",
        "url": "https://www.cnn.com/2025/06/06/sport/texas-texas-tech-womens-college-world-series-title-spt",
        "urlToImage": "https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2218314741.jpg?c=16x9&q=w_800,c_fill",
        "publishedAt": "2025-06-07T03:49:51Z",
        "content": "The Texas Longhorns won the Womens College World Series in dominant fashion, blowing out Texas Tech 10-4 in Fridays winner-take-all Game 3 to clinch the programs first-ever national championship in s\u2026 [+2655 chars]"
    },
    {
        "source": {
            "id": "cnn",
            "name": "CNN"
        },
        "author": "Rosa de Acosta, Matias Grez",
        "title": "Roland Garros: A visual guide to the iconic clay court grand slam",
        "description": "The French Open is one of the most iconic tennis tournaments in history with its red clay courts, boisterous crowds and plenty of celebrities. Here\u2019s everything you need to know about Roland Garros.",
        "url": "https://www.cnn.com/2025/06/06/sport/roland-garros-clay-court-french-open-spt-dg",
        "urlToImage": "https://media.cnn.com/api/v1/images/stellar/prod/french-open-top-card.jpg?c=16x9&q=w_800,c_fill",
        "publishedAt": "2025-06-07T06:54:56Z",
        "content": "Its crunch time in Paris as we reach the business end of the French Open.\r\nWorld No. 1 Aryna Sabalenka came through a battle against four-time winner and defending champion Iga witek to make the wome\u2026 [+5218 chars]"
    },
    {
        "source": {
            "id": "cnn",
            "name": "CNN"
        },
        "author": "Jacob Lev",
        "title": "Florida Panthers down Edmonton Oilers in double overtime to even up Stanley Cup Final",
        "description": "The Florida Panthers defeated the Edmonton Oilers 5-4 in double overtime to win Game 2 of the Stanley Cup Final and even the series at 1-1 on Friday at the Rogers Place.",
        "url": "https://www.cnn.com/2025/06/07/sport/panthers-oilers-game-2-stanley-cup-final-spt",
        "urlToImage": "https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2218995528.jpg?c=16x9&q=w_800,c_fill",
        "publishedAt": "2025-06-07T09:48:12Z",
        "content": "Another game, another overtime needed to proclaim a winner.\r\nThis time around it was the Florida Panthers defeating the Edmonton Oilers 5-4 in double overtime to win Game 2 of the Stanley Cup Final a\u2026 [+2662 chars]"
    },
    {
        "source": {
            "id": "cnn",
            "name": "CNN"
        },
        "author": "Jacob Lev",
        "title": "Sovereignty wins the 2025 Belmont Stakes",
        "description": "Sovereignty, the 2025 Kentucky Derby winner, won the 157th running of the Belmont Stakes in Saratoga Springs, New York, on Saturday.",
        "url": "https://www.cnn.com/2025/06/07/sport/sovereignty-2025-belmont-stakes-spt",
        "urlToImage": "https://media.cnn.com/api/v1/images/stellar/prod/ap25158843295754.jpg?c=16x9&q=w_800,c_fill",
        "publishedAt": "2025-06-07T23:48:12Z",
        "content": "Sovereignty, the 2025 Kentucky Derby winner, won the 157th running of the Belmont Stakes in Saratoga Springs, New York, on Saturday.\r\nThe Godolphin-owned 3-year-old who came into the race as the 5-2 \u2026 [+1469 chars]"
    }
]"""
