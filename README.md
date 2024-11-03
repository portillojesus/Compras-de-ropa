Este proyecto es una aplicación simple para gestionar un inventario de prendas de ropa, con clases que representan prendas específicas para hombres y mujeres. Los usuarios pueden ver el inventario y procesar compras, reduciendo el stock de los artículos comprados.
La estructura se basa en
Clase Prenda: Clase base que define los atributos generales de una prenda (nombre, precio y cantidad). Incluye métodos para mostrar la información de una prenda y para reducir el stock al procesar una compra.
Clase RopaHombre y RopaMujer: Clases específicas que heredan de Prenda, añadiendo el atributo talla para diferenciar las prendas según género. Además, sobreescriben el método mostrar_info para mostrar la talla.
Clase Inventario: Encargada de gestionar todas las prendas, permite agregar prendas, mostrar el inventario completo y procesar compras, verificando la disponibilidad y el stock de cada prenda.

Algunas de las funcionalidades que tiene el proyecto es
Visualización del Inventario: Lista todas las prendas disponibles, mostrando su nombre, precio, stock y talla.
Procesamiento de Compras: Permite seleccionar una prenda por su nombre y procesar la compra de una cantidad específica, ajustando el stock disponible y mostrando el total a pagar.
Interacción con el Usuario: La aplicación cuenta con un menú interactivo donde el usuario puede ver el inventario y procesar compras.

Y como podemos utilizar el proyecto
Para ejecutar el programa, solo necesitas correr el archivo principal. Podrás ver el inventario y realizar compras. Hay una función de entrada (input) que te permitirá agregar nuevas prendas de manera interactiva.

