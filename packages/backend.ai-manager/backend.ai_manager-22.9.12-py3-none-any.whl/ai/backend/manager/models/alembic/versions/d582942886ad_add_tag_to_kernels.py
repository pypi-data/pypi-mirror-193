"""add tag to kernels

Revision ID: d582942886ad
Revises: a1fd4e7b7782
Create Date: 2018-10-25 10:51:39.448309

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d582942886ad"
down_revision = "a1fd4e7b7782"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("kernels", sa.Column("tag", sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("kernels", "tag")
    # ### end Alembic commands ###
