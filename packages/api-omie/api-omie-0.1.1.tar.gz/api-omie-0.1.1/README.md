# ApiOmie (NÃO OFICIAL)

> este projeto não te ligação nenhuma com a omie

# Use a documentação oficial!

## download

``````shell
$pip install omieapi
``````

## como usar 

<p> Para usar basta chamar o metodo, 
e passar os argumentos-chave que seram empacotados e transmitidos para api como no exemplo</p>

``````python
from omieapi import Omie

meu_app = Omie('key#######', 'secreet######')

r = meu_app.listar_produtos(
    pagina=1
)

print(r)
``````
