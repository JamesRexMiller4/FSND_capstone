"""Change cascade delete implementation to delete_orphan

Revision ID: 591f7dca4fd0
Revises: 1f1ca7c73348
Create Date: 2020-04-24 09:10:46.408412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '591f7dca4fd0'
down_revision = '1f1ca7c73348'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('cast_movie_id_fkey', 'cast', type_='foreignkey')
    op.drop_constraint('cast_actor_id_fkey', 'cast', type_='foreignkey')
    op.create_foreign_key(None, 'cast', 'movie', ['movie_id'], ['id'])
    op.create_foreign_key(None, 'cast', 'actors', ['actor_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cast', type_='foreignkey')
    op.drop_constraint(None, 'cast', type_='foreignkey')
    op.create_foreign_key('cast_actor_id_fkey', 'cast', 'actors', ['actor_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('cast_movie_id_fkey', 'cast', 'movie', ['movie_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
