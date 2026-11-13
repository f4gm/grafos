# Grafos

Proyecto de Matemáticas Discretas II, Entrega 1.

## Integrantes

- Santiago Hurtado Rodríguez - 202538363
- Fernando Andrés Giraldo Mejía - 202537774

## Archivos

- `graphs/directed_graph.py`: grafo dirigido (matriz de adyacencia).
- `graphs/undirected_graph.py`: grafo no dirigido (lista de adyacencia).
- `graphs/graph_loader.py`: carga un grafo desde un CSV.
- `graphs/plot_graph.py`: función útil para imprimir un grafo dirigido o no dirigido.
- `csv/ejemplo_1.csv` a `csv/ejemplo_6.csv`: archivos de prueba.
- `ejemplo_1.ipynb` a `ejemplo_1.ipynb`: notebooks con pruebas de las clases y sus métodos sobre cada archivo CSV de prueba.

## Uso

```python
from graphs.graph_loader import load_graph_from_file

graph = load_graph_from_file("ejemplo_1.csv")
print(graph.get_vertices())
```

## Por qué estas representaciones

- **No dirigido:** lista de adyacencia. Guardamos cada vértice con sus vecinos y pesos en un diccionario. Cada arista se guarda en los dos sentidos, así que buscar los vecinos de un vértice es directo. Además, los puntos 6 a 9 necesitan recorrer el grafo vecino por vecino, y esta forma lo hace natural. Con pocas aristas también ocupa menos memoria que una matriz.
- **Dirigido:** matriz de adyacencia. Cada celda guarda el peso de una arista o `None`. La elegimos para probar una forma distinta a la de la lista y comparar las dos. Con un grafo denso (muchas aristas) la matriz es una buena opción.

## Cómo nos fue

La lista de adyacencia fue la parte más fácil. Un diccionario de diccionarios se entiende rápido y el código para agregar vértices y aristas quedó muy corto.

La matriz costó más. Cada vez que aparece un vértice nuevo hay que agregar una fila y una columna, y para buscar la posición de un vértice usamos `list.index`, que recorre la lista completa. Por eso, con grafos grandes, esta implementación sería lenta. Un diccionario que guarde la posición de cada vértice lo mejoraría, pero preferimos mantener el código simple.

Probamos la carga con los archivos `ejemplo_1.csv` a `ejemplo_6.csv`, y los resultados coincidieron con lo que esperábamos. Un problema que tuvimos fue que los vértices se guardan como texto, así que hay que consultarlos con `"1"` y no con `1`. Lo aprendimos al probar el código.

Otra decisión fue no validar errores. Si el CSV está mal escrito, Python muestra el error tal cual. Esto hace el código más corto, pero para un proyecto más grande habría que agregar validaciones.
