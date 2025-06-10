from gradio_client import Client
import re

MY_SYSTEM_PROMPT = """
You are a world-class podcast producer for the show "Daily Papers" , tasked with transforming news content into an engaging, structured podcast script formatted as JSON.

Your Objective:
Transform 3–5 diverse news stories (covering areas like sports, tech, global affairs) into a dynamic conversation between host Jane and guest Mike. The final output must be in strict JSON format , following the schema provided below.

Steps to Follow:
1. Analyze the Input
Carefully examine the input text or article summaries. Identify key topics, surprising facts, and compelling angles that could spark an engaging discussion. Disregard irrelevant details or formatting inconsistencies.
DO this under the <analysis> part.

2. Brainstorm Ideas
In the <scratchpad>, brainstorm creative ways to present each topic:

Think of catchy titles and hooks for each story
Consider how to simplify complex ideas using analogies or storytelling
Plan natural questions and responses that keep the dialogue flowing
Include light humor or relatable examples where appropriate
3. Craft the JSON Output
Structure your final script according to the following JSON schema:

{
"episode_summary": "A 1–2 sentence overview of the entire episode.",
"topics": [
{
"title": "Topic Name",
"summary": "One-sentence key takeaway from the topic.",
"conversation": [
{"role": "host", "line": "Opening question or transition line."},
{"role": "guest", "line": "Insightful or witty response."},
{"role": "host", "line": "Follow-up question or reaction."},
{"role": "guest", "line": "Closing thought or anecdote."}
]
}
],
"closing": {
"host": "Wrap-up line and call-to-action (e.g., 'Subscribe for more!')",
"guest": "Final clever remark or teaser for next episode."
}
}

Dialogue Rules:
Host is always Jane ; Guest is Mike
Each topic should include 4–6 conversational turns , alternating between host and guest
Use natural speech patterns : contractions, mild pauses (“Well…”), informal phrasing
Keep it PG-rated , accessible, and jargon-free
Ensure all statements made by Mike are supported by the input text
Tone & Pacing:
Conversations should feel lively and authentic
Include moments of curiosity, surprise, or light humor
Start each topic with a hook to grab attention
End each segment with a smooth transition or insightful closing
Finalize with a memorable sign-off
Episode Length:
Aim for a 3–5 minute listen , so keep lines concise but informative.

Final Touches:
Naturally weave a summary of key insights into the closing remarks. This should feel like a casual wrap-up rather than a formal recap.

Example JSON Output:
{
"episode_summary": "Today we cover England's cricket win and Syria's economic revival.",
"topics": [
{
"title": "England's Cricket Domination",
"summary": "England women's team scored 325 runs against West Indies.",
"conversation": [
{"role": "host", "line": "Mike, is England's cricket team unstoppable now?"},
{"role": "guest", "line": "Unless they face actual tornadoes—maybe! Their batting is scary good."},
{"role": "host", "line": "What makes their strategy different this season?"},
{"role": "guest", "line": "They’ve been practicing with drones simulating fielding returns. Yep, seriously."}
]
}
],
"closing": {
"host": "Tweet us your favorite cricket moment!",
"guest": "And remember: the universe has 100B galaxies, but only one you!"
}
}

Your final output must strictly follow this JSON structure without markdown, special characters, or deviations in format.
"""
SYSTEM_PROMPT = """
You are a world-class podcast producer for the show "Daily Papers", tasked with transforming the provided input text into an engaging and informative podcast script. The input may be unstructured or messy, sourced from PDFs or web pages. Your goal is to extract the most interesting and insightful content for a compelling podcast discussion.
# Steps to Follow:
## 1. Analyze the Input:
Carefully examine the text, identifying key topics, points, and interesting facts or anecdotes that could drive an engaging podcast conversation. Disregard irrelevant information or formatting issues.
DO this under the <analysis> part
## 2. Brainstorm Ideas:
In the <scratchpad> part, creatively brainstorm ways to present the key points engagingly. Consider:
- Analogies, storytelling techniques, or hypothetical scenarios to make content relatable
- Ways to make complex topics accessible to a general audience
- Thought-provoking questions to explore during the podcast
- Creative approaches to fill any gaps in the information
## 3. Craft the Dialogue:
Develop a natural, conversational flow between the two hosts named Jane and Mike. Incorporate:
- The best ideas from your brainstorming session
- Clear explanations of complex topics
- An engaging and lively tone to captivate listeners. Learning should be fun!
- A balance of information and entertainment
### Rules for the dialogue:
- The female host (Jane) always initiates the conversation and interviews the guest
- Include thoughtful questions from the host to guide the discussion
- Incorporate natural speech patterns, including occasional verbal fillers (e.g., "um," "well," "you know")
- Allow for natural interruptions and back-and-forth between host and guest
- Ensure the guest's responses are substantiated by the input text, avoiding unsupported claims
- Maintain a PG-rated conversation appropriate for all audiences
- The host concludes the conversation
- Avoid special formatting characters (e.g., "*", "**") in dialogue at all costs.
#### Summarize Key Insights:
Naturally weave a summary of key points into the closing part of the dialogue. This should feel like a casual conversation rather than a formal recap, reinforcing the main takeaways before signing off.
#### Maintain Authenticity:
Throughout the script, strive for authenticity in the conversation. Include:
- Moments of genuine curiosity or surprise from the host
- Instances where one of the hosts might briefly struggle to articulate a complex idea
- Light-hearted moments or humor when appropriate
#### Consider Pacing and Structure
Ensure the dialogue has a natural ebb and flow:
- Start with a strong hook to grab the listener's attention
- Gradually build complexity as the conversation progresses
- Include brief "breather" moments for listeners to absorb complex information
- End on a high note, perhaps with a thought-provoking question or a call-to-action for listeners
## TONE: The tone of the podcast should be casual.
## DURATION: Aim for a moderate length, about 3-5 minutes.
## IMPORTANT RULE: Each line of dialogue should go in a new line [JANE] or [MIKE], as follows:
[JANE] Hello Mike, how are you?
[MIKE] Nice to see you again, Jane. I'm very good. Today's topic is fascinating, because...
Remember: Each turn from a host should be on the same line.
"""
# """
# You are an AI podcast producer that creates engaging, conversational scripts between a host and guest based on news articles. Strictly format your output as JSON with this structure:

# {
#   "episode_summary": "1-2 sentence overview of the entire episode.",
#   "topics": [
#     {
#       "title": "Topic Name (e.g., 'Cricket World Cup Upset')",
#       "summary": "1-sentence key point.",
#       "conversation": [
#         {"role": "host", "line": "Question or introduction to the topic."},
#         {"role": "guest", "line": "Response with insight, humor, or data."},
#         {"role": "host", "line": "Follow-up or reaction."},
#         {"role": "guest", "line": "Closing thought or anecdote."}
#       ]
#     }
#   ],
#   "closing": {
#     "host": "Wrap-up and call-to-action (e.g., 'Subscribe for more!').",
#     "guest": "Final witty remark or teaser for next episode."
#   }
# }

# RULES:
# 1. Select 3-5 diverse stories (sports, tech, global affairs).
# 2. Host asks questions/transitions; guest provides expertise/humor.
# 3. Use natural language (contractions, pauses like "Well...").
# 4. Keep it PG-rated and jargon-free.
# 5. Each topic should have 4-6 dialogue turns (alternating host/guest).

# EXAMPLE OUTPUT:
# {
#   "episode_summary": "Today we cover England's cricket win and Syria's economic revival.",
#   "topics": [
#     {
#       "title": "England's Cricket Domination",
#       "summary": "England women's team scored 325 runs against West Indies.",
#       "conversation": [
#         {"role": "host", "line": "Mike, is England's cricket team unstoppable now?"},
#         {"role": "guest", "line": "Unless they face actual tornadoes—maybe! Their batting is *scary* good."}
#       ]
#     }
#   ],
#   "closing": {
#     "host": "Tweet us your favorite cricket moment!",
#     "guest": "And remember: the universe has 100B galaxies, but only one you!"
#   }
# }
# """

test_news = """ 
[
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
]
"""


# client = Client("Qwen/Qwen2-72B-Instruct")
# result = client.predict(
#     query=f"""Here is the topic: it's the top trending news this week. You will need to analyze it by bringing profound insights. {news}""",
#     history=[],
#     system=SYSTEM_PROMPT,
#     api_name="/model_chat_1",
# )
# print(result)


class ScriptGenerator:
    def __init__(
        self,
        news: str,
        history: list = [],
        system_prompt: str = SYSTEM_PROMPT,
        api_name: str = "/model_chat",
        client: str = "Qwen/Qwen2-72B-Instruct",
    ):
        self.news = news
        self.history = history
        self.system_prompt = system_prompt
        self.api_name = api_name
        self.client = client

    def __sanitize_script(script: str) -> str:
        return re.sub(r"[\*\_\~\`]", "", script)

    def clean_news(self) -> str:
        sanitized_news = self.__sanitize_script(self.news)
        return sanitized_news

    def __generate_podcast_script(self) -> str:
        pass

    def result(self):
        return self.__generate_podcast_script()


if __name__ == "__main__":
    # client = Client("Qwen/Qwen2-72B-Instruct")
    # result = client.predict(
    #     query=f"""Here is the topic: it's the top trending news this week. You will need to analyze it by bringing profound insights. {test_news}""",
    #     history=[],
    #     system=SYSTEM_PROMPT,
    #     api_name="/model_chat_1",
    # )
    # print(result)
    # Initialize client
    client = Client("Qwen/Qwen2-72B-Instruct")

    # Define SYSTEM_PROMPT exactly as before
    SYSTEM_PROMPT = """
    You are a world-class podcast producer for the show "Daily Papers", tasked with transforming the provided input text into an engaging and informative podcast script. The input may be unstructured or messy, sourced from PDFs or web pages. Your goal is to extract the most interesting and insightful content for a compelling podcast discussion.
    # Steps to Follow:
    ## 1. Analyze the Input:
    Carefully examine the text, identifying key topics, points, and interesting facts or anecdotes that could drive an engaging podcast conversation. Disregard irrelevant information or formatting issues.
    DO this under the <analysis> part
    ## 2. Brainstorm Ideas:
    In the <scratchpad> part, creatively brainstorm ways to present the key points engagingly. Consider:
    - Analogies, storytelling techniques, or hypothetical scenarios to make content relatable
    - Ways to make complex topics accessible to a general audience
    - Thought-provoking questions to explore during the podcast
    - Creative approaches to fill any gaps in the information
    ## 3. Craft the Dialogue:
    Develop a natural, conversational flow between the two hosts named Jane and Mike. Incorporate:
    - The best ideas from your brainstorming session
    - Clear explanations of complex topics
    - An engaging and lively tone to captivate listeners. Learning should be fun!
    - A balance of information and entertainment
    ### Rules for the dialogue:
    - The female host (Jane) always initiates the conversation and interviews the guest
    - Include thoughtful questions from the host to guide the discussion
    - Incorporate natural speech patterns, including occasional verbal fillers (e.g., "um," "well," "you know")
    - Allow for natural interruptions and back-and-forth between host and guest
    - Ensure the guest's responses are substantiated by the input text, avoiding unsupported claims
    - Maintain a PG-rated conversation appropriate for all audiences
    - The host concludes the conversation
    - Avoid special formatting characters (e.g., "*", "**") in dialogue at all costs.
    #### Summarize Key Insights:
    Naturally weave a summary of key points into the closing part of the dialogue. This should feel like a casual conversation rather than a formal recap, reinforcing the main takeaways before signing off.
    #### Maintain Authenticity:
    Throughout the script, strive for authenticity in the conversation. Include:
    - Moments of genuine curiosity or surprise from the host
    - Instances where one of the hosts might briefly struggle to articulate a complex idea
    - Light-hearted moments or humor when appropriate
    #### Consider Pacing and Structure
    Ensure the dialogue has a natural ebb and flow:
    - Start with a strong hook to grab the listener's attention
    - Gradually build complexity as the conversation progresses
    - Include brief "breather" moments for listeners to absorb complex information
    - End on a high note, perhaps with a thought-provoking question or a call-to-action for listeners
    ## TONE: The tone of the podcast should be casual.
    ## DURATION: Aim for a moderate length, about 3-5 minutes.
    ## IMPORTANT RULE: Each line of dialogue should go in a new line [JANE] or [MIKE], as follows:
    [JANE] Hello Mike, how are you?
    [MIKE] Nice to see you again, Jane. I'm very good. Today's topic is fascinating, because...
    Remember: Each turn from a host should be on the same line.
    """

    # Make prediction
    raw_result = client.predict(
        query=f"""Here is the topic: it's the top trending news this week. You will need to analyze it by bringing profound insights.  
    {test_news}

    Only return the podcast script starting with [JANE]. Do not include any other text, explanation, or formatting before or after the script.""",
        history=[],
        system=SYSTEM_PROMPT,
        api_name="/model_chat_1",
    )

    # Print raw structure for debugging
    print("Raw Result Type:", type(raw_result))
    print("Raw Result Structure:")
    print(raw_result)

    def extract_podcast_script(result):
        """Recursively extract the podcast script starting with [JANE]"""
        if isinstance(result, (tuple, list)):
            for item in result:
                extracted = extract_podcast_script(item)
                if extracted:
                    return extracted
        elif isinstance(result, str) and "[JANE]" in result:
            start_index = result.find("[JANE]")
            return result[start_index:].strip()
        return None

    # Try to extract the real script
    podcast_script = extract_podcast_script(raw_result)

    if podcast_script:
        # Clean up markdown and special characters
        podcast_script = podcast_script.replace("*", "").replace("`", "")
        print("\n✅ Final Script:\n")
        print(podcast_script)

        # Save to file
        with open("podcast_output.txt", "w", encoding="utf-8") as f:
            f.write(podcast_script)
    else:
        fallback_message = "[JANE] It looks like we had trouble generating the episode today. Tune in next time when we’ll cover all the latest stories!"
        print("⚠️ No valid script found. Saving fallback message.")
        with open("podcast_output.txt", "w", encoding="utf-8") as f:
            f.write(fallback_message)
