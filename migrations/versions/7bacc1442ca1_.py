"""empty message

Revision ID: 7bacc1442ca1
Revises: 
Create Date: 2020-04-29 20:09:04.438083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bacc1442ca1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('user_id', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_admin_email'), 'admin', ['email'], unique=True)
    op.create_index(op.f('ix_admin_user_id'), 'admin', ['user_id'], unique=True)
    op.create_table('home_about_block',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('image', sa.String(length=256), nullable=True),
    sa.Column('content', sa.String(length=1024), nullable=True),
    sa.Column('link', sa.String(length=256), nullable=True),
    sa.Column('link_text', sa.String(length=64), nullable=True),
    sa.Column('editor_user_id', sa.String(length=64), nullable=True),
    sa.Column('edited_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['editor_user_id'], ['admin.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('home_client_block',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_logo', sa.String(length=256), nullable=True),
    sa.Column('editor_user_id', sa.String(length=64), nullable=True),
    sa.Column('edited_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['editor_user_id'], ['admin.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('home_functions_block',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('icon', sa.String(length=256), nullable=True),
    sa.Column('content', sa.String(length=256), nullable=True),
    sa.Column('editor_user_id', sa.String(length=64), nullable=True),
    sa.Column('edited_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['editor_user_id'], ['admin.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('home_functions_block')
    op.drop_table('home_client_block')
    op.drop_table('home_about_block')
    op.drop_index(op.f('ix_admin_user_id'), table_name='admin')
    op.drop_index(op.f('ix_admin_email'), table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###