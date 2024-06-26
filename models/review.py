#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """Representation of Review """
    __tablename__ = 'reviews'

    product_id = Column(String(60), ForeignKey('products.id'))  # Foreign key to relate review to its product
    user_id = Column(String(60), ForeignKey('users.id'))  # Foreign key to relate review to its author
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
