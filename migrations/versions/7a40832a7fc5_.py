"""empty message

Revision ID: 7a40832a7fc5
Revises: 
Create Date: 2021-08-11 18:35:11.651521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a40832a7fc5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('keywords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=15), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('crawled_urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('keyword_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('word', sa.String(length=15), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.Column('summary', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['keyword_id'], ['keywords.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('crawled_urls')
    op.drop_table('keywords')
    # ### end Alembic commands ###
