from flask import Blueprint, render_template, request, url_for
from app.models import Crawled_urls

bp = Blueprint('article', __name__, url_prefix='/article')

@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    article_list = Crawled_urls.query.order_by(Crawled_urls.id.desc())
    article_list = article_list.paginate(page, per_page=10)
    return render_template('article/article_list.html', article_list=article_list)

@bp.route('/detail/<int:article_id>/')
def detail(article_id):
    article = Crawled_urls.query.get_or_404(article_id)
    return render_template('article/article_detail.html', article=article)