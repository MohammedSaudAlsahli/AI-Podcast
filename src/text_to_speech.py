from asyncio import sleep
from gradio_client import Client


class TTS:
    def __init__(
        self,
        prompt: str,
        client: str = "NihalGazi/Text-To-Speech-Unlimited",
        emotion: str = "excited and joyful",
        use_random_seed: bool = True,
        specific_seed: int = 12345,
        api_name: str = "/text_to_speech_app",
    ):
        self.prompt = prompt
        self.client = client
        self.emotion = emotion
        self.use_random_seed = use_random_seed
        self.specific_seed = specific_seed
        self.api_name = api_name

    def __tts_result(self, voice: str):
        client = Client(self.client)
        result = client.predict(
            prompt=self.prompt,
            voice=voice,
            emotion=self.emotion,
            use_random_seed=self.use_random_seed,
            specific_seed=self.specific_seed,
            api_name=self.api_name,
        )
        return result

    def __female(self):
        return self.__tts_result(voice="alloy")

    def __male(self):
        return self.__tts_result(voice="dan")

    def generateAudio(self):
        mp3_files = []

        for script in self.prompt.get("script", []):
            prompt = script.get("line", "")
            if script.get("host") == "Emma":
                audio = TTS(prompt=prompt).__female()
                if audio[0] is None:
                    print(f"Retrying female voice for: {prompt}")
                    audio = TTS(prompt=prompt).__female()
            else:
                audio = TTS(prompt=prompt).__male()

                if audio[0] is None:
                    print(f"Retrying male voice for: {prompt}")
                    audio = TTS(prompt=prompt).__male()

            mp3_files.append(audio[0])

        return mp3_files


if __name__ == "__main__":
    scripts = [
        {
            "host": "Emma",
            "line": "Welcome back to The Weekly Roundup! John, I have to say, my week was completely dominated by...",
        },
        {
            "host": "John",
            "line": "Oh no, don't tell me. Did they start another global conflict or did space tourism finally get approved by the UN?",
        },
        {
            "host": "John",
            "line": "I don't know if that's a good or bad thing, but at least it gives us something to talk about. What happened, Emma?",
        },
        {
            "host": "Emma",
            "line": "Oh, John, you have no idea! Cricket fans, gather 'round! The England women's cricket team just had the most exhilarating match against the West Indies.",
        },
        {
            "host": "Emma",
            "line": "It was at the County Ground in Taunton, and you should have seen that crowd! They were absolutely bouncing. If enthusiasm could be bottled, that stadium would be sold out.",
        },
        {
            "host": "Emma",
            "line": "Then there's this incredible news that colleges in the US are about to change forever - they're about to start paying players millions, thanks to a $2.8 billion settlement. I tried to wrap my head around that, but it felt like quantum physics.",
        },
        {
            "host": "John",
            "line": "That's right, and it's a game-changer. You know, Emma, just like that dropped catch in the cricket game was a game-changer. Ugh, don't remind me about that one. I seriously thought section 47 was a key wicket or something.",
        },
        {
            "host": "John",
            "line": "Anyway, you can binge all the highlights on BBC. It was an absolute thriller. I mean, tea?",
        },
        {
            "host": "Emma",
            "line": "Lunch? Definitely not just tea. Those players stayed completely composed under pressure. My panic levels were off the charts. What happened to cool Jim? I mean, no pressure buddy.",
        },
        {
            "host": "Emma",
            "line": "And just when I thought sports were our week, along comes breakdancing in swimming! Seriously, Summer McIntosh is this 15-year-old phenom who just smashed the 400m freestyle world record by doing a headstand underwater. That has to be a new Olympic event, right?",
        },
        {
            "host": "John",
            "line": "Now you're talking my language. Headstands, check. Breaking records while nearly suffocating, give me strength. Thankfully, the stars don't fall from the sky just yet, unlike in some tournaments.",
        },
        {
            "host": "Emma",
            "line": "Exactly! Texas Longhorns just won the Women's College World Series in dominating fashion, 10-4. And then, right after that, in Canada, this girl sets a new record. It feels like every good thing is happening simultaneously.",
        },
        {
            "host": "Emma",
            "line": "Meanwhile, in France, the French Open is heating up. Tennis on clay, everyone's getting excited like it's prom night all over again.",
        },
        {
            "host": "John",
            "line": "Not just anyone gets excited, Emma. It's almost like people spontaneously combust with joy as if it's their native language. But okay, let's stick to what we know: these giant ice hockey games that go to five minutes of sheer madness.",
        },
        {
            "host": "Emma",
            "line": "The Panthers defeated the Oilers 5-4 in double overtime. It was the kind of game that makes you question why we can't have hockey indoors all year.",
        },
        {
            "host": "Emma",
            "line": "Then there's the Belmont Stakes! Believed to be the oldest running race in America, or at least old enough that nobody remembers who started it really.",
        },
        {
            "host": "John",
            "line": "And the hero? A 3-year-old horse who's clearly been doing this since he was basically knee-high to a gnat, except it's been his whole life apparently. What a concept, living only for glory.",
        },
        {
            "host": "Emma",
            "line": "Then, on a completely different wavelength, the BBC dropped a story about this observatory in the Atacama Desert that's mapping the universe. That's got to be one of the coolest hideouts in fiction, right?",
        },
        {
            "host": "John",
            "line": "Yeah, a robotic hand that senses touch is pretty dope though. Maybe if I got fired from my six-figure job, I'd be considering that observatory spot.",
        },
        {
            "host": "Emma",
            "line": "But then we have more serious topics: the civil war in Syria and the political tensions in Moldova. Hundreds of thousands dead, millions displaced in Syria. Then, not so far away geographically, Moldova trying to navigate between West and Russia.",
        },
        {
            "host": "John",
            "line": "Talk about pressure! Just like those athletes are dealing with pressure now, countries the world over are putting their contestants into tricky positions. I wonder what happens if they lose? Will the substitutes get a penalty, or do they just bench the whole team?",
        },
        {
            "host": "Emma",
            "line": "Either way, John, it makes you appreciate the England cricket team even more. Which is why, every week, we should remind everyone to just go out, enjoy some sports, and maybe not worry too much about who's messing with a country torn between two giants.",
        },
        {
            "host": "Emma",
            "line": "Wow, we've covered such different stories this week. But let's know what you thought - did any story surprise you or make you stop watching YouTube videos for 15 minutes straight?",
        },
        {
            "host": "Emma",
            "line": "Thanks for sticking with us this week. Until next time, keep rounding up the week! Goodnight!",
        },
    ]

    mp3_files = []
    for script in scripts:
        if script.get("host") == "Emma":
            audio = TTS(prompt=script.get("line")).female()
            if audio[0] is None:
                print(f"Failed to generate audio for: {script.get('line')}")
                audio = TTS(prompt=script.get("line")).female()
            mp3_files.append(audio[0])
        else:
            audio = TTS(prompt=script.get("line")).male()
            if audio[0] is None:
                print(f"Failed to generate audio for: {script.get('line')}")
                audio = TTS(prompt=script.get("line")).male()
            mp3_files.append(audio[0])

    print(mp3_files)
