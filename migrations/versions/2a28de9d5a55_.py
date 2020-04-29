"""empty message

Revision ID: 2a28de9d5a55
Revises: 7bacc1442ca1
Create Date: 2020-04-29 21:20:00.888562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a28de9d5a55'
down_revision = '7bacc1442ca1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('about_net_block',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('media', sa.String(length=1024), nullable=True),
    sa.Column('content', sa.String(length=1024), nullable=True),
    sa.Column('link', sa.String(length=256), nullable=True),
    sa.Column('link_text', sa.String(length=64), nullable=True),
    sa.Column('editor_user_id', sa.String(length=64), nullable=True),
    sa.Column('edited_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['editor_user_id'], ['admin.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('about_net_block')
    # ### end Alembic commands ###
