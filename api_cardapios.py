from fastapi import APIRouter, HTTPException, status
from utils.utils import Utilidades
from dependencias import obter_rep_cardapio

router = APIRouter()
REP_CARDAPIO = obter_rep_cardapio()

# GET (READ)
@router.get('/cardapio/')
async def listar_cardapios() -> None: 
    return REP_CARDAPIO.ler_cardapios()
    
@router.get('/cardapio/{codigo_cardapio}')
async def ler_entidade(codigo_cardapio):
    return REP_CARDAPIO.ler_entidade(codigo_cardapio)

# POST (CREATE)
@router.post('/cardapio')
async def criar_cardapio(nome: str, descricao: str):
    REP_CARDAPIO.criar_cardapio(
        codigo=Utilidades.criar_codigo(nome),
        nome=nome,
        descricao=descricao
    )
    response = {"mensagem": "cardápio criado com sucesso!"}
    return response, status.HTTP_201_CREATED

# PUT (UPDATE)
@router.put('/cardapio')
async def alterar_cardapio(nome: str, descricao: str, codigo: str):
    REP_CARDAPIO.alterar_cardapio(
        nome=nome,
        descricao=descricao,
        codigo=codigo
    )
    response = {"mensagem": "cardápio alterado!"}


# DELETE 
@router.delete('/cardapio/{codigo_cardapio}')
async def deletar_cardapio(codigo_cardapio: str):
    REP_CARDAPIO.deletar_cardapio(codigo_cardapio)
    response = {"mensagem": "cardápio deletado!"}
    return response, status.HTTP_200_OK