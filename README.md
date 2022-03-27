# ruleta

Clase Ruleta implementada en Python con generador aleatorio de jugadas.

## Instrucciones

```
ruleta = Ruleta()   #instanciación

tirada = {
    "jugada": "PLENO",
    "dinero": 700,
    "apuesta": 25        
}

ruleta.tirar(tirada)  #tirar de la ruleta
```

También se pueden generar aleatoriamente jugadas para alimentar a `ruleta.tirar()`:

```
ruleta = Ruleta()

tirada1 = Ruleta.generador() #genera aleatoriamente cualquier jugada con cualquier dinero

tirada2 = Ruleta.generador(350) #genera aleatoriamente cualquier jugada apostando 350

tirada3 = Ruleta.generador(350,"CUADRO") #genera una tirada jugando a CUADRO apostando 350

ruleta.tirar(tirada1)
ruleta.tirar(tirada2)
ruleta.tirar(tirada3)
```

## Tipos de Jugadas


| Apuesta     | Valor                 |
| ---         | ---                   |
| PLENO       | n(0-36)               |
| SEMI-PLENO  | [n(2-33),n-1 \| n+3]  |
| CALLE       | n(1-11)               |
| COLOR       | R \| N                |
| PAR-IMPAR   | PAR \| IMPAR          |
| DOCENA      | n(1-3)                |
| COLUMNA     | n(1-3)                |
| MITAD       | n(1-2)                |
| LINEA       | n(1-11)               |
| CUADRO      | [[n,n+3],[n-,n+2]]    |
| 0-1-2-3     | None                  |