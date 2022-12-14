"""empty message

Revision ID: 86f39b0c1092
Revises: e57074d642b3
Create Date: 2022-11-11 15:42:12.947964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86f39b0c1092'
down_revision = 'e57074d642b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('cars_model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars_model',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='cars_model_pkey')
    )
    op.drop_table('product_table')
    # ### end Alembic commands ###
