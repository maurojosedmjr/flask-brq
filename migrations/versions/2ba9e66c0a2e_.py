"""empty message

Revision ID: 2ba9e66c0a2e
Revises: 8daac273607d
Create Date: 2021-07-18 19:02:52.415437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2ba9e66c0a2e"
down_revision = "8daac273607d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "preco_medio",
        sa.Column("id_preco_medio", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("neighbourhood_group", sa.String(length=150), nullable=True),
        sa.Column("room_type", sa.String(length=150), nullable=True),
        sa.Column("price", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("id_preco_medio"),
    )
    op.create_table(
        "residencias",
        sa.Column("id_residencia", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(length=150), nullable=True),
        sa.Column("host_id", sa.Integer(), nullable=True),
        sa.Column("host_name", sa.String(length=150), nullable=True),
        sa.Column("neighbourhood", sa.String(length=150), nullable=True),
        sa.Column("latitude", sa.Float(), nullable=True),
        sa.Column("longitude", sa.Float(), nullable=True),
        sa.Column("room_type", sa.String(length=150), nullable=True),
        sa.Column("price", sa.Float(), nullable=True),
        sa.Column("minimum_nights", sa.Integer(), nullable=True),
        sa.Column("number_of_reviews", sa.Integer(), nullable=True),
        sa.Column("last_review", sa.String(length=10), nullable=True),
        sa.Column("reviews_per_month", sa.Float(), nullable=True),
        sa.Column("calculated_host_listings_count", sa.Integer(), nullable=True),
        sa.Column("availability_365", sa.Integer(), nullable=True),
        sa.Column("neighbourhood_group", sa.String(length=150), nullable=True),
        sa.PrimaryKeyConstraint("id_residencia"),
        sa.UniqueConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("residencias")
    op.drop_table("preco_medio")
    # ### end Alembic commands ###
