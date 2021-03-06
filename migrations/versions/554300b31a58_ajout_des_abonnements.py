"""Ajout des abonnements

Revision ID: 554300b31a58
Revises: f22ed03a04ae
Create Date: 2020-03-04 10:28:18.226659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '554300b31a58'
down_revision = 'f22ed03a04ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('abonnements',
    sa.Column('abonne_id', sa.Integer(), nullable=True),
    sa.Column('abonnement_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['abonne_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['abonnement_id'], ['user.id'], ),
    sa.UniqueConstraint('abonne_id', 'abonnement_id', name='unicite_couple')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('abonnements')
    # ### end Alembic commands ###
