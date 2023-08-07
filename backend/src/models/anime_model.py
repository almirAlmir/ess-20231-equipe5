from src.config.database import Base
from sqlalchemy import Column, Integer, Boolean, Float, String

class Anime(Base):
    __tablename__ = 'animes'
    
    id = Column(Integer, primary_key=True, index=True)
    nome_anime = Column(String)
    qtd_assistido = Column(Integer)
    likes = Column(Float)
     