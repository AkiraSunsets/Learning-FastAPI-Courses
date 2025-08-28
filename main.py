from fastapi import FastAPI, HTTPException, status, Depends
from routes import curso_router, usuario_router #faz com que o FASTAPI importe as rotas
from typing import Optional, Any

app = FastAPI(title="Cursos Disponíveis", version="0.0.1", description="Confira abaixo os cursos disponíveis")

app.include_router(curso_router.router, tags=['cursos']) #faz com que seja incluido as rotas 
app.include_router(usuario_router.router, tags=['usuario'])

def fake_db():
    try:
        print("Connecting to the bank")
    finally:
        print("Closing the bank")


cursos = { #foi criado um json para funcionar como armazenamento
    1: { 
        "titulo": "Ciências da Computação",
        "aulas" : 1,
        "horas" : 4
    },
    
    2: {
        "titulo" : "Windows",
        "aulas" : 4,
        "horas" : 16
    },

    3: {
        "titulo" : "Prototipagem Web",
        "aulas" : 4,
        "horas" : 16
    },

    4: {
        "titulo" : "FastAPI",
        "aulas" : 8,
        "horas" : 64
    }

}

@app.get("/")
async def raiz():
    return{"API - Cursos Disponiveis"} #funciona como o main

@app.get("/cursos") #categoria com nome opcional
async def get_cursos(db: Any = Depends(fake_db)): #verifica se há pelo menos um item verdadeiro
    return cursos

@app.get("/cursos/{curso_id}", description="Retorna um curso com um id especifico")
async def get_curso(curso_id: int): #usado no singular para realizar uma busca de um unico id
    try:
        curso = cursos[curso_id] 
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Este curso não foi encontrado")
    

if __name__ == '__main__':
    import uvicorn #é usado para que se houver a necessidade 
                   #de realizar alguma alteração de alguma informação na execução do código
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)

