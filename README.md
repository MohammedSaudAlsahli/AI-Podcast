# 🎙️ AI Podcast Automation

Automate the creation of a weekly AI-generated podcast using trending news, conversational scripts, realistic AI voices, and automatic YouTube uploads.

![AI Podcast Banner](https://img.shields.io/github/languages/top/MohammedSaudAlsahli/AI-Podcast)
[![AI Podcast Automation](https://github.com/MohammedSaudAlsahli/AI-Podcast/actions/workflows/podcast.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/MohammedSaudAlsahli/AI-Podcast/actions/workflows/podcast.yml)
---

## 🚀 Features

- 📥 **News Fetching** — Automatically collects trending news from sources like CNN, BBC, etc.
- 📝 **Script Generation** — Converts news into dynamic podcast conversations between hosts.
- 🗣️ **Text-to-Speech** — Uses realistic AI voices for podcast narration.
- 📼 **Podcast Generation** — Compiles voice files into an audio episode.
- 📺 **YouTube Upload** — Uploads the final podcast to your YouTube channel with a generated thumbnail.
- ⏱️ **Fully Automated** — Runs every Saturday via GitHub Actions.

---

## 🧠 How It Works

1. **News API** pulls top headlines.
2. **LLM via OpenRouter** creates a script for two podcast hosts.
3. **TTS module** turns the script into spoken dialogue.
4. **FFmpeg** assembles audio clips into a full episode.
5. **Uploader** publishes it to YouTube with title, description, and thumbnail.
6. **GitHub Actions** automates the entire pipeline weekly.

---

## 📂 Project Structure

```bash
AI-Podcast/
│
├── .github/workflows/         # GitHub Actions automation
├── src/
│   ├── news_fetch.py          # Fetch trending news
│   ├── script_generator.py    # Generate podcast dialogue script
│   ├── text_to_speech.py      # Convert script to audio
│   ├── podcast_generator.py   # Stitch audio into episode
│   ├── uploader.py            # Upload to YouTube
│   └── utils.py               # Shared utilities and settings
├── main.py                    # Main runner script
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
````

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/MohammedSaudAlsahli/AI-Podcast.git
cd AI-Podcast
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Set your API keys and secrets in GitHub Actions (`Settings > Secrets and variables`) or in a `.env` file (if running locally):

* `NEWS_API_KEY`
* `GOOGLE_API_KEY`
* `GOOGLE_CLIENT_ID`
* `GOOGLE_CLIENT_SECRET`
* `GOOGLE_PROJECT_ID`
* `TOKEN_URI`
* `ACCESS_TOKEN`
* `REFRESH_TOKEN`
* `OPENROUTER_API_KEY`

### 5. Run the Script Locally

```bash
python main.py
```

---

## 🤖 Automation with GitHub Actions

This project is fully automated with GitHub Actions.

* The workflow is defined in `.github/workflows/main.yml`.
* It runs every **Saturday at 6 AM UTC** using this cron schedule:

```yaml
schedule:
  - cron: "0 6 * * 6"
```

* You can also manually trigger it from the Actions tab.

---

## 📸 Example Output

| 🎧 Podcast Audio    | 🖼️ Thumbnail                | 📺 YouTube Upload      |
| ------------------- | ---------------------------- | ---------------------- |
| AI-generated voices | Auto-generated (coming soon) | Uploaded automatically |

---

## 🧠 Powered By

* [OpenRouter](https://openrouter.ai/) — LLM API
* [NewsAPI.org](https://newsapi.org/) — News data
* [Google Text-to-Speech](https://cloud.google.com/text-to-speech) — Realistic voice synthesis
* [FFmpeg](https://ffmpeg.org/) — Audio processing
* [YouTube Data API](https://developers.google.com/youtube/v3) — Video publishing
* [GitHub Actions](https://docs.github.com/en/actions) — Workflow automation

---

## 🙋‍♂️ Author

**Mohammed Saud Alsahli**
Digital Product Manager & Python Developer
🔗 [LinkedIn](https://www.linkedin.com/in/mohammed-saud-alsahli/)
📫 Email: [contact@alsahli.dev](mailto:contact@alsahli.dev)

---

## 📌 TODO

* [ ] Add auto-thumbnail generation using AI image tools
* [ ] Add support for Arabic and other languages
* [ ] Add web dashboard for configuration and analytics
* [ ] Publish podcast to Spotify & Apple Podcasts

---

## 📝 License

This project is licensed under the MIT License.
Feel free to use, share, and improve!


