# Estante

Mini-projeto do bloco de Python da Trilha UFPE.

## O problema

Eu sempre esqueço o que já li ou assisti e o que ainda está na fila. A Estante é um programa de terminal para guardar livros e séries, marcar o que já terminei, dar uma nota e ver a média das notas.

## Como foi feito

O programa usa orientação a objetos:

- `Item` é a classe base, com título, status e nota
- `Livro` e `Serie` herdam de `Item` e acrescentam o autor ou o número de temporadas
- `Estante` guarda os itens e calcula os pendentes e a média das notas

## Como rodar

Precisa ter o Python 3 instalado.

```
python estante.py
```

Depois é só escolher as opções do menu.
