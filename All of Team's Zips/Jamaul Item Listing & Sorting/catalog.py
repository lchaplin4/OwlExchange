from flask import Blueprint, request, render_template
from sqlalchemy import asc, desc
from models import db, Product, Category

bp = Blueprint('catalog', __name__)

@bp.route('/products')
def products():
    q = request.args.get('q', '', type=str).strip()
    cat = request.args.get('cat', type=int)
    sort = request.args.get('sort', 'new')
    page = request.args.get('page', 1, type=int)
    per_page = 12

    query = Product.query

    if q:
        like = f"%{q}%"
        query = query.filter(Product.title.ilike(like))

    if cat:
        query = query.filter(Product.category_id == cat)

    sort_map = {
        'new': desc(Product.created_at),
        'price_asc': asc(Product.price_cents),
        'price_desc': desc(Product.price_cents),
        'name_asc': asc(Product.title),
    }
    order_by = sort_map.get(sort, desc(Product.created_at))
    query = query.order_by(order_by, Product.id.asc())

    paginated = query.paginate(page=page, per_page=per_page, error_out=False)

    categories = Category.query.order_by(Category.name.asc()).all()
    return render_template(
        'products.html',
        products=paginated.items,
        pagination=paginated,
        categories=categories,
        q=q, cat=cat, sort=sort
    )
