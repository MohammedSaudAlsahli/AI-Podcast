from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    NEWS_API_KEY: str
    OPENROUTER_API_KEY: str
    GOOGLE_CLIENT_ID: str
    GOOGLE_PROJECT_ID: str
    GOOGLE_CLIENT_SECRET: str
    TOKEN_URI: str
    REFRESH_TOKEN: str
    ACCESS_TOKEN: str
    GOOGLE_API_KEY: str
    debug: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


BG_VIDEO = Path(__file__).parent / "bg_video.mp4"
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
  The output must be a in JSON object with the following structure:


  {
    "podcastTitle": "The Weekly Roundup",
    "episodeTitle": "Your clever AI-generated episode title here",
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
}"""

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

TEST_AUDIO = [
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/c88e3f45084f76f67b2692257d05ac40feff9eb1380503e9efda0818636db082/tmpmbvgwbmb.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/7d43a8718de9a1ace173dc2d2aa839a7639c550a25ff5fa77b1faf41201b26e7/tmpk5aerjt8.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/d0aff4360574af938ddcb7781e9f7f277d005503759759aba98c1d7b9f11b885/tmpsigi_9u6.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/efaf48bb9e22fd227cf9391d2a39a3b466030b450db50ac8597020a87222443f/tmp_0n591u6.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/a6988f803a85d4b3431318b3c240b641e6aca6ebe1dfef58dd4a62f99f18387f/tmpapu03yjy.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/bc362e88eda0505842d94a0a4e938478788ff87a34d55b0346e4120f111d5368/tmpsqeosf9p.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/c3f947f10c170c8a6b95434c403aa49e4cf1475797231ecd41a693b305d9b871/tmpgjfyn_a0.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/593d9fcb8c32135c0a677ec66959cb496baab7a1da9a3a84f61def7640ed02eb/tmpl04ikukv.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/388d443fc3feb96028cf4fd28188b6452908988f61af881c08cef7a21cce5b4d/tmpgnyki66z.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/3cf5263b093f17b11e22c79ffb2ac63710d93860bdd39e053b2a53ae9a2c5872/tmpq60wnlpk.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/ed4223d107b64004965a1acefa3c1a4a7d9719a9bcd5193964a8c3d4fa4c571f/tmpsfae3dwp.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/049e7a55cd1e6f64e16b29cbdc1430842f3ccc2b7ca07c25f77562e0cbeec933/tmp_85fz4ym.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/d292eccf711cd7ea798183ff5631e2c239cbe55a7eafd6bb414e872eb77c9f2b/tmpz3lgdc6k.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/e4932ec83af1404128fa2ccac58d72b3bead9fd6afd8a80cbe9adf6443d86554/tmppo1s6h2b.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/556886cbcf2c30757fd467a1465932b6c3d86d6b043b6b7e9727966f137cf2c3/tmp9giwiaw9.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/d006c92f235bfcd762bd46bffe094a720f926b24fe5b05b12cf3c55fcab4a15a/tmplt0v3gxj.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/6e05a240b8e1062334d51f7652306d8cb8eb38d80b59016eed4b6ef19fe5dd07/tmpvfii_vfn.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/693946ac9de57706210f007bc0e2ac2076baea6e305a288725edf38f7f848b21/tmpkcxyobgy.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/45a6cd9c75f004ce27b7215f949967d47ad75a3fcea55e7a15cbbefd4d3dd9f0/tmp_suhcvr3.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/f17bb34ae19b042f2ab078791316beb616498797fbfc3ab24938e78677f0b486/tmpyzzrclgj.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/4335f6c102a5195fe1a7ab977e29904bc32ef8ce7b24a21d2305b2de7b8a9958/tmpx3stbavo.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/4485924a0a03eb085906e5106613d3b177734e1db59fdc1a0833539ff4b90a2c/tmp0_lr40hj.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/233bb66da88c2e235a5bcd5a16dab987a4d0838a958d727377873fde215f7f4b/tmpd88ibr_p.mp3",
    "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/b71edbe2314b48590fa7ead674b122f9e0c3e02013e642f3fb746884f62ec51d/tmp4af7gxcq.mp3",
]
