from newspaper import Article
from gensim.summarization import summarize
from newspaper import Config

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.229 Whale/2.10.123.42 Safari/537.36"
config = Config()
config.browser_user_agent = user_agent

def get_article(url):
    news = Article(url, language='ko', config=config)
    news.download()
    news.parse()
    return news.title, news.text

def summarize_article(url, words=50):
    _, text = get_article(url)
    return summarize(text, word_count=words)

# url = 'https://zdnet.co.kr/view/?no=20210810213922'
# title, text = get_article(url)
# print(title)
# print(summarize_article(url, 50))