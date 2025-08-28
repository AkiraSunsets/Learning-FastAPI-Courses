#criando uma classe 

from typing import Optional

from pydantic import BaseModel #importa o BaseModel para validar dados

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str #definiu este atributo como uma string, somente caracteres
    aulas: int 
    horas: int #definiu este atributo como int, somente números inteiros

    
