# 🔎 HackerNews Scraper

A simple Python tool that scrapes the [Hacker News](https://news.ycombinator.com/) front page and filters stories based on their point score.

## 📌 Features

- Scrapes top posts from Hacker News
- Filters posts with a minimum number of points (e.g., 100+)
- Sorts filtered posts in descending order of points
- Outputs a clean list of titles, links, and scores

## 🚀 Tech Stack

- Python 3
- `requests`
- `BeautifulSoup` (bs4) for HTML parsing

## 🛠 How to Use

1. **Clone the repo**
   ```bash
   git clone https://github.com/rkd1989/HackerNews.git
   cd HackerNews
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**
   ```bash
   python main.py
   ```

## 📂 Project Structure

```
HackerNews/
├── main.py         # Entry point
├── scrape.py       # Scraper logic
└── requirements.txt
```

## 📸 Sample Output

```
[145] Show HN: HackerTool – AI-driven CLI for developers – https://news.ycombinator.com/item?id=123456
[112] Launch HN: New AI Startup does XYZ – https://news.ycombinator.com/item?id=654321
```

## ✍️ Author

- [Rishabh Kavidayal](https://github.com/rkd1989)

---

Feel free to fork, star, or contribute!
