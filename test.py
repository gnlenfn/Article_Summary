from app.services import crawling, summarize
from app.models import Keywords, Crawled_urls
from app import db
from datetime import datetime

q = Keywords(word='잔여백신', create_date=datetime.now())
db.session.add(q)
db.session.commit()

q.id
q.word

Keywords.query.all()

query, date, df = crawling.crawling_article(q.word)
for _, (title, url, que) in df.iterrows():
    c = Crawled_urls(word=que, keyword=q, title=title, 
                    url=url, summary=summarize.summarize_article(url), 
                    create_date=datetime.now())
    db.session.add(c)
db.session.commit()