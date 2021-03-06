"""empty message

Revision ID: 2fa53dee76bf
Revises: 016ac8854c18
Create Date: 2021-07-18 16:42:24.454855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2fa53dee76bf"
down_revision = "016ac8854c18"
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("preco_medio")
    # ### end Alembic commands ###
