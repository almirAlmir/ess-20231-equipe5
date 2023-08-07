from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Assistido(BaseModel):
    data_assistido: Optional[datetime.date] = None
        
class Assistindo(BaseModel):
    data_assistindo: Optional[datetime.date] = None

class Anime(BaseModel):
    id: int
    nome_anime: str
    qtd_assistido: int
    likes: Optional[float] = 0
    
    class Config:
        orm_mode = True
    