"""initial migration

Revision ID: 36c05bec0e3c
Revises: 
Create Date: 2024-04-07 20:39:46.920079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36c05bec0e3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ingredients', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('restaurant_pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('pizza_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pizza_id'], ['pizzas.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant_pizzas')
    op.drop_table('restaurants')
    op.drop_table('pizzas')
    # ### end Alembic commands ###
