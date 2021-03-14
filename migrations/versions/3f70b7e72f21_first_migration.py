"""first migration

Revision ID: 3f70b7e72f21
Revises: 
Create Date: 2021-03-12 11:53:14.213844

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3f70b7e72f21'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('state', sa.String(length=2), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('image_link', sa.String(length=250), nullable=True),
    sa.Column('facebook_link', sa.String(length=250), nullable=True),
    sa.Column('seeking_venue', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(length=100), nullable=True),
    sa.Column('genres', postgresql.ARRAY(sa.String(), dimensions=1), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('state', sa.String(length=2), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('image_link', sa.String(length=250), nullable=True),
    sa.Column('facebook_link', sa.String(length=250), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(length=100), nullable=True),
    sa.Column('genres', postgresql.ARRAY(sa.String(), dimensions=1), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('artist_shows',
    sa.Column('show_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['show_id'], ['show.id'], ),
    sa.PrimaryKeyConstraint('show_id', 'artist_id')
    )
    op.create_table('venue_shows',
    sa.Column('show_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['show_id'], ['show.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('show_id', 'venue_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venue_shows')
    op.drop_table('artist_shows')
    op.drop_table('venue')
    op.drop_table('show')
    op.drop_table('artist')
    # ### end Alembic commands ###
