from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey, UniqueConstraint, Computed
from sqlalchemy.orm import relationship
from core.database import Base
from core.Dataset.ThematicCategorization import  ThematicCategorizationModel

thematic_categorization_transition = Table(
    'thematic_categorization_transition', Base.metadata,
    Column('thematic_categorization_id', Integer, ForeignKey('thematic_categorization.id'), primary_key=True),
    Column('transition_id', Integer, ForeignKey('transition.id'), primary_key=True),
    # Ensure the combination is unique
    UniqueConstraint('thematic_categorization_id', 'transition_id', name='uq_thematic_categorization_transition')
)

class TransitionModel(Base):
    __tablename__ = "transition"
    id = Column(Integer, primary_key=True, autoincrement=True)
    repository_name = Column(String(), ForeignKey("repository.name"), nullable=False)
    source_framework = Column(String(), nullable=True)
    target_framework = Column(String(), nullable=False)
    __table_args__ = (
        UniqueConstraint(
            "repository_name",
            "source_framework",
            "target_framework",
            "summary",
            name="uq_transition_unique_fields"
        ),
    )
    summary = Column(Text(), nullable=False)
    type = Column(String(), Computed("CASE WHEN source_framework IS NULL THEN 'adoption' ELSE 'migration' END"))

    thematic_categorizations = relationship(ThematicCategorizationModel, secondary=thematic_categorization_transition, back_populates="transitions")

    commits = relationship("CommitModel", back_populates="transition")
    issues = relationship("IssueModel", back_populates="transition")
