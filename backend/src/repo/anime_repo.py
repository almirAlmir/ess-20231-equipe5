from sqlalchemy.orm import Session
from src.models import anime_model
from src.schemas import anime_schema

class RepositorioAnimes():
    
    def __init__(self, db: Session):
        self.db = db
        
    def criar(self, anime: anime_schema.Anime):
        db_anime = anime_model.Anime(nome_anime=anime.nome_anime,
                                     qtd_assitido=anime.qtd_assistido,
                                     likes=anime.likes)
        
        self.db.add(db_anime)
        self.db.commit()
        self.db.refresh() #Popula toda a tabela
        
        return db_anime