from fastapi import APIRouter, HTTPException, status
from dependencias import obter_rep_produtos, obter_rep_cardapio
from utils.utils import Utilidades

router = APIRouter()
REP_PRODUTO = obter_rep_produtos()
REP_CARDAPIO = obter_rep_cardapio()

# READ
@router.get("/produto")
async def listar_produtos():
    return REP_PRODUTO.listar_produtos()

@router.get("/produto/{codigo_produto}")
async def ler_entidade(codigo_produto):
    return REP_PRODUTO.ler_entidade(codigo_produto)


# CREATE 
@router.post("/produto")
async def criar_produto(
    nome: str,
    descricao: str,
    preco: float,
    restricao: str,
    codigo_cardapio: str
):
    restricoes_validas = ["padrao", "vegano", "vegetariano"]

    # VALIDAÇÃO (SE NÃO EXISTIR O CARDÁPIO; OU RESTRIÇÃO FOR INVÁLIDA)
    if REP_CARDAPIO.ler_entidade(codigo_cardapio) is None or restricao not in restricoes_validas:
                raise HTTPException(status.HTTP_400_BAD_REQUEST, "produto inválido!")


    REP_PRODUTO.criar_produto(
        codigo=Utilidades.criar_codigo(nome),
        nome=nome,
        descricao=descricao,
        preco=preco,
        restricao=restricao,
        codigo_cardapio=codigo_cardapio
    )
    
    REP_PRODUTO.ler_entidade(Utilidades.criar_codigo(nome))
    reponse = {"mensagem": "produto criado com sucesso!"}
    return reponse, status.HTTP_201_CREATED

# UPDATE
@router.put("/produto/{codigo_produto}")
async def alterar_produto(
    nome: str,
    descricao: str,
    preco: float,
    restricao: str,
    codigo_cardapio: str,
    codigo_produto: str
):
    REP_PRODUTO.alterar_produto(nome, descricao, preco, restricao, codigo_cardapio, codigo_produto)
    response = {"mensagem": "produto alterado!"}
    return response, status.HTTP_200_OK

# DELETE 
@router.delete("/produto/{codigo_produto}")
async def deletar_produto(codigo_produto):
      REP_PRODUTO.deletar_produto(codigo_produto)
      response = {"mensagem": "produto deletado!"}
      return response, status.HTTP_200_OK