# from huggingface_hub import InferenceClient
# import re
# from utils import Settings

SYSTEM_PROMPT = """

You are an AI podcast producer tasked with creating engaging and informative podcast scripts based on the provided news articles. The podcast will feature two male hosts, Alex and Ryan, who will discuss the stories in a conversational and accessible tone. Follow these guidelines:

Steps to Craft the Script:
1. Analyze the Input
Carefully examine the provided news articles and select 3-5 key stories that are diverse and interesting.
Focus on the following:
Major events or highlights.
Context or background information that enhances understanding.
Unique or surprising elements of the story.
2. Group the Stories by Theme
Group the selected stories into logical themes to create a smooth flow for discussion. For example:
Sports Highlights
Science and Technology
World Affairs
Cultural Events
3. Brainstorm Presentation Ideas
Use storytelling techniques to make complex topics relatable:
Analogies (e.g., comparing a sports event to a dramatic movie climax).
Questions to provoke curiosity and engagement.
Hypothetical scenarios to explore the story’s implications.
4. Develop the Dialogue
Create a natural and lively conversation between Alex and Ryan, ensuring:
Alex initiates the discussion and poses thought-provoking questions.
Ryan provides insightful commentary, adding humor or anecdotes when appropriate.
Both hosts share genuine reactions (e.g., surprise, laughter, curiosity).
Maintain a balance of information and entertainment to keep listeners engaged.
Rules for the Dialogue
Use the following dialogue format:

Copy
[ALEX] Introduction or question.
[RYAN] Response or commentary.
Each line of dialogue should include:
Natural speech patterns (e.g., “Um,” “You know,” “Well”).
Occasional light-hearted interruptions or banter.
Avoid jargon and ensure clarity for a general audience.
Conclude with a summary of key insights and a call to action (e.g., encouraging listeners to explore more).
Structure of the Podcast Script
Introduction:

Alex introduces the podcast and teases the topics to be discussed.
Example: "Today, we’re diving into the highlights from women’s cricket, groundbreaking tech at the Rubin Observatory, and how life is evolving in Syria!"
Segment 1: Sports Highlights

Discuss the England vs. West Indies ODI and other major sports news.
Segment 2: Science & Technology

Cover the Rubin Observatory’s mapping of the universe and new tech innovations.
Segment 3: World Affairs

Explore global issues like Syria’s transformation and Moldova’s geopolitical importance.
Closing:

Summarize the key takeaways.
End with a thought-provoking question or an encouraging note for the audience.
Tone and Style
Keep the tone casual, friendly, and engaging.
Use a moderate length (about 3-5 minutes per segment).
Ensure the content is PG-rated and suitable for all audiences.

"""

# """
# You are a world-class podcast producer for the show "Daily Papers", tasked with transforming the provided input text into an engaging and informative podcast script. The input may be unstructured or messy, sourced from PDFs or web pages. Your goal is to extract the most interesting and insightful content for a compelling podcast discussion.
# # Steps to Follow:
# ## 1. Analyze the Input:
# Carefully examine the text, identifying key topics, points, and interesting facts or anecdotes that could drive an engaging podcast conversation. Disregard irrelevant information or formatting issues.
# DO this under the <analysis> part
# ## 2. Brainstorm Ideas:
# In the <scratchpad> part, creatively brainstorm ways to present the key points engagingly. Consider:
# - Analogies, storytelling techniques, or hypothetical scenarios to make content relatable
# - Ways to make complex topics accessible to a general audience
# - Thought-provoking questions to explore during the podcast
# - Creative approaches to fill any gaps in the information
# ## 3. Craft the Dialogue:
# Develop a natural, conversational flow between the two hosts named Jane and Mike. Incorporate:
# - The best ideas from your brainstorming session
# - Clear explanations of complex topics
# - An engaging and lively tone to captivate listeners. Learning should be fun!
# - A balance of information and entertainment
# ### Rules for the dialogue:
# - The female host (Jane) always initiates the conversation and interviews the guest
# - Include thoughtful questions from the host to guide the discussion
# - Incorporate natural speech patterns, including occasional verbal fillers (e.g., "um," "well," "you know")
# - Allow for natural interruptions and back-and-forth between host and guest
# - Ensure the guest's responses are substantiated by the input text, avoiding unsupported claims
# - Maintain a PG-rated conversation appropriate for all audiences
# - The host concludes the conversation
# - Avoid special formatting characters (e.g., "*", "**") in dialogue at all costs.
# #### Summarize Key Insights:
# Naturally weave a summary of key points into the closing part of the dialogue. This should feel like a casual conversation rather than a formal recap, reinforcing the main takeaways before signing off.
# #### Maintain Authenticity:
# Throughout the script, strive for authenticity in the conversation. Include:
# - Moments of genuine curiosity or surprise from the host
# - Instances where one of the hosts might briefly struggle to articulate a complex idea
# - Light-hearted moments or humor when appropriate
# #### Consider Pacing and Structure
# Ensure the dialogue has a natural ebb and flow:
# - Start with a strong hook to grab the listener's attention
# - Gradually build complexity as the conversation progresses
# - Include brief "breather" moments for listeners to absorb complex information
# - End on a high note, perhaps with a thought-provoking question or a call-to-action for listeners
# ## TONE: The tone of the podcast should be casual.
# ## DURATION: Aim for a moderate length, about 3-5 minutes.
# ## IMPORTANT RULE: Each line of dialogue should go in a new line [JANE] or [MIKE], as follows:
# [JANE] Hello Mike, how are you?
# [MIKE] Nice to see you again, Jane. I'm very good. Today's topic is fascinating, because...
# Remember: Each turn from a host should be on the same line.
# """
# settings = Settings()

# client = InferenceClient(
#     "Qwen/Qwen3-32B",
#     provider="hf-inference",
#     token=settings.HF_TOKEN,
# )


# def sanitize_script(script: str) -> str:
#     """Remove special characters like '*' from the script."""
#     # Remove asterisk and other special formatting characters (add more as needed)
#     return re.sub(r"[\*\_\~\`]", "", script)


# def generate_podcast_script(subject: str, steering_question: str | None = None) -> str:
#     """Ask the LLM for a script of a podcast given by two hosts."""
#     # Limit subject length to avoid exceeding model context window
#     max_subject_length = 4000
#     safe_subject = subject[:max_subject_length]
#     messages = [
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {
#             "role": "user",
#             "content": f"""Here is the topic: it's the top trending paper on Hugging Face daily papers today. You will need to analyze it by bringing profound insights.\n{safe_subject}""",
#         },
#     ]
#     if steering_question and len(steering_question) > 0:
#         messages.append(
#             {
#                 "role": "user",
#                 "content": f"You could focus on this question: {steering_question}",
#             }
#         )
#     try:
#         response = client.chat_completion(
#             messages,
#             max_tokens=8156,
#         )
#     except Exception as e:
#         print(f"Error from chat_completion: {e}")
#         raise
#     full_text = response.choices[0].message.content
#     assert "[JANE]" in full_text
#     dialogue_start_index = full_text.find("[JANE]")
#     podcast_text = full_text[dialogue_start_index:]
#     podcast_text = sanitize_script(podcast_text)
#     return podcast_text


# script = generate_podcast_script(subject="cats")

# print(script)
news = """ 

[{'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': None, 'title': 'Watch: England v West Indies, third ODI highlights', 'description': 'Highlights from the County Ground in Taunton as England women take on the West Indies in the final encounter of a three-match one-day international series.', 'url': 'https://www.bbc.co.uk/iplayer/episode/m002dg80/womens-odi-cricket-2025-highlights-england-v-west-indies-third-odi', 'urlToImage': 'https://ichef.bbci.co.uk/images/ic/1200x675/p0lfwlm1.jpg', 'publishedAt': '2025-06-07T22:09:15Z', 'content': 'Highlights from the County Ground in Taunton as England women take on the West Indies in the final encounter of a three-match one-day international series.'}, {'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': None, 'title': 'Tech Now', 'description': "Ione Wells has behind the scenes access to the Rubin Observatory in Chile's Atacama Desert, while Paul Carter visits an Amazon warehouse introducing a new robot with a sense of touch.", 'url': 'https://www.bbc.co.uk/iplayer/episode/m002dgb9/tech-now-rubin-observatory-mapping-the-universe', 'urlToImage': 'https://ichef.bbci.co.uk/images/ic/1200x675/p0lgtktm.jpg', 'publishedAt': '2025-06-07T01:00:00Z', 'content': "Ione Wells has behind the scenes access to the Rubin Observatory in Chile's Atacama Desert, while Paul Carter visits an Amazon warehouse introducing a new robot with a sense of touch.\xa0More"}, {'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': 'BBC World Service', 'title': 'How life is changing in Syria', 'description': 'For well over a decade, civil war blighted the lives of Syrians, as rebel forces battled against former President Bashar al-Assad and his brutal regime. More than 600,000 people were killed and 12 million others were forced from their homes during this time. …', 'url': 'https://www.bbc.co.uk/programmes/p0lgvvq4', 'urlToImage': 'https://ichef.bbci.co.uk/images/ic/1200x675/p0lgvvsn.jpg', 'publishedAt': '2025-06-07T00:30:00Z', 'content': 'For well over a decade, civil war blighted the lives of Syrians, as rebel forces battled against former President Bashar al-Assad and his brutal regime. More than 600,000 people were killed and 12 mi… [+953 chars]'}, {'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': 'BBC World Service', 'title': 'Why does Moldova matter to Putin?', 'description': 'Moldova is a country torn between pro-Western and pro-Russian factions. In September this year, Moldovans will vote for a new leadership, and pro-European observers are worried that Russia will try to influence the outcome of these elections. Why? Natasha Mat…', 'url': 'https://www.bbc.co.uk/programmes/p0lgc942', 'urlToImage': 'https://ichef.bbci.co.uk/images/ic/1200x675/p0hqg7fh.jpg', 'publishedAt': '2025-06-07T12:30:00Z', 'content': 'Moldova is a country torn between pro-Western and pro-Russian factions. In September this year, Moldovans will vote for a new leadership, and pro-European observers are worried that Russia will try t… [+395 chars]'}, {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': None, 'title': 'Federal judge approves $2.8B settlement, paving way for US colleges to pay athletes millions', 'description': 'A federal judge signed off on arguably the biggest change in the history of college sports on Friday, clearing the way for schools to begin paying their athletes millions of dollars as soon as next month as the multibillion-dollar industry shreds the last ves…', 'url': 'https://www.cnn.com/2025/06/06/sport/settlement-colleges-pay-athletes-millions-spt', 'urlToImage': 'https://media.cnn.com/api/v1/images/stellar/prod/2025-03-26t192854z-1332456188-mt1usatoday25772182-rtrmadp-3-ncaa-basketball-ncaa-tournament-west-regional-practice.jpg?c=16x9&q=w_800,c_fill', 'publishedAt': '2025-06-07T02:45:26Z', 'content': 'A federal judge signed off on arguably the biggest change in the history of college sports Friday, clearing the way for schools to begin paying their athletes millions of dollars as soon as next mont… [+6036 chars]'}, {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': 'Jacob Lev', 'title': 'Texas routs Texas Tech to secure first Women’s College World Series title in program history', 'description': 'The Texas Longhorns won the Women’s College World Series in dominant fashion, blowing out Texas Tech 10-4 in Friday’s winner-take-all Game 3 to clinch the program’s first-ever national championship in softball.', 'url': 'https://www.cnn.com/2025/06/06/sport/texas-texas-tech-womens-college-world-series-title-spt', 'urlToImage': 'https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2218314741.jpg?c=16x9&q=w_800,c_fill', 'publishedAt': '2025-06-07T03:49:51Z', 'content': 'The Texas Longhorns won the Womens College World Series in dominant fashion, blowing out Texas Tech 10-4 in Fridays winner-take-all Game 3 to clinch the programs first-ever national championship in s… [+2655 chars]'}, {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': 'Jacob Lev', 'title': 'Sovereignty wins the 2025 Belmont Stakes', 'description': 'Sovereignty, the 2025 Kentucky Derby winner, won the 157th running of the Belmont Stakes in Saratoga Springs, New York, on Saturday.', 'url': 'https://www.cnn.com/2025/06/07/sport/sovereignty-2025-belmont-stakes-spt', 'urlToImage': 'https://media.cnn.com/api/v1/images/stellar/prod/ap25158843295754.jpg?c=16x9&q=w_800,c_fill', 'publishedAt': '2025-06-07T23:48:12Z', 'content': 'Sovereignty, the 2025 Kentucky Derby winner, won the 157th running of the Belmont Stakes in Saratoga Springs, New York, on Saturday.\r\nThe Godolphin-owned 3-year-old who came into the race as the 5-2 … [+1469 chars]'}, {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': 'Rosa de Acosta, Matias Grez', 'title': 'Roland Garros: A visual guide to the iconic clay court grand slam', 'description': 'The French Open is one of the most iconic tennis tournaments in history with its red clay courts, boisterous crowds and plenty of celebrities. Here’s everything you need to know about Roland Garros.', 'url': 'https://www.cnn.com/2025/06/06/sport/roland-garros-clay-court-french-open-spt-dg', 'urlToImage': 'https://media.cnn.com/api/v1/images/stellar/prod/french-open-top-card.jpg?c=16x9&q=w_800,c_fill', 'publishedAt': '2025-06-07T06:54:56Z', 'content': 'Its crunch time in Paris as we reach the business end of the French Open.\r\nWorld No. 1 Aryna Sabalenka came through a battle against four-time winner and defending champion Iga witek to make the wome… [+5218 chars]'}, {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': 'Jacob Lev', 'title': 'Florida Panthers down Edmonton Oilers in double overtime to even up Stanley Cup Final', 'description': 'The Florida Panthers defeated the Edmonton Oilers 5-4 in double overtime to win Game 2 of the Stanley Cup Final and even the series at 1-1 on Friday at the Rogers Place.', 'url': 'https://www.cnn.com/2025/06/07/sport/panthers-oilers-game-2-stanley-cup-final-spt', 'urlToImage': 'https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2218995528.jpg?c=16x9&q=w_800,c_fill', 'publishedAt': '2025-06-07T09:48:12Z', 'content': 'Another game, another overtime needed to proclaim a winner.\r\nThis time around it was the Florida Panthers defeating the Edmonton Oilers 5-4 in double overtime to win Game 2 of the Stanley Cup Final a… [+2662 chars]'}, {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': 'Ben Church', 'title': 'Belmont Stakes: Battle of the champions in Triple Crown’s third leg', 'description': 'There may be no Triple Crown at stake but the stage is set for two champions to battle it out in this year’s Belmont Stakes.', 'url': 'https://www.cnn.com/2025/06/07/sport/belmont-stakes-triple-crown-preview-spt', 'urlToImage': 'https://media.cnn.com/api/v1/images/stellar/prod/ap25155457161367.jpg?c=16x9&q=w_800,c_fill', 'publishedAt': '2025-06-07T11:30:04Z', 'content': 'There may be no Triple Crown at stake this year, but the stage is set for two champions to battle it out in this years Belmont Stakes.\r\nThe winner of both the Kentucky Derby, Sovereignty, and the rei… [+3795 chars]'}]

"""
from gradio_client import Client

client = Client("Qwen/Qwen2-72B-Instruct")
result = client.predict(
    query=f"""Here is the topic: it's the top trending news this week. You will need to analyze it by bringing profound insights. {news}""",
    history=[],
    system=SYSTEM_PROMPT,
    api_name="/model_chat_1",
)
print(result)
