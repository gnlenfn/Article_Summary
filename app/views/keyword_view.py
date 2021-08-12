from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from datetime import datetime

from app import db
from app.forms import QueryCreateForm
from app.models import Crawled_urls, Keywords
from app.services import summarize, crawling

bp = Blueprint('query', __name__, url_prefix='/query')

@bp.route('/keyword/', methods=['GET', 'POST'])
def add_query():
    form = QueryCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        query = Keywords.query.filter_by(word=form.word.data).first()
        if not query:
            query = Keywords(word=form.word.data, create_date=datetime.now())
            db.session.add(query)
            db.session.commit()

            # crawling & add to db
            df = crawling.crawling_article(form.word.data, form.nums.data)
            for _, (title, url, que) in df.iterrows():
                c = Crawled_urls(word=que, keyword=query, 
                                title=title, url=url, 
                                summary=summarize.summarize_article(url), 
                                create_date=datetime.now())
                db.session.add(c)
            db.session.commit()

            return redirect(url_for('query.add_query'))
        else:
            flash('이미 존재하는 키워드 입니다.')

    

    keyword_list = Keywords.query.order_by(Keywords.id.desc())
    return render_template("keyword/set_keyword.html", form=form, keyword_list=keyword_list)

@bp.route("/delete/<int:keyword_id>")
def delete(keyword_id):
    q = Keywords.query.get_or_404(keyword_id)
    db.session.delete(q)
    db.session.commit()

    return redirect(url_for('article._list'))

