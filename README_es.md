# Especificación de Requisitos de Gilded Rose  

Saludos y bienvenidos al gremio de la **Gilded Rose**. Como sabéis, somos una pequeña posada en un enclave privilegiado de una ciudad prominente, regentada por la amable posadera **Allison**. También compramos y vendemos únicamente los más finos bienes.  
Por desgracia, nuestras mercancías se degradan constantemente en su `Quality` a medida que se aproxima su fecha de venta.  

Disponemos de un sistema encantado que actualiza nuestro inventario por nosotros. Fue desarrollado por un aventurero de carácter férreo llamado **Leeroy**, quien ya ha partido hacia nuevas gestas. Vuestra misión es añadir una nueva característica a nuestro sistema, para que podamos comenzar a comerciar con una nueva categoría de objetos. Primero, una introducción a nuestro sistema:  

- Todo `Item` tiene un valor `SellIn` que indica los días que restan para venderlo.  
- Todo `Item` tiene un valor de `Quality` que representa lo valioso que es.  
- Al final de cada jornada, nuestro sistema reduce ambos valores en cada `Item`.  

Bastante sencillo, ¿verdad? Pues aquí es donde la cosa se pone interesante:  

- Una vez pasada la fecha de venta, la `Quality` se degrada el doble de rápido.  
- La `Quality` de un `Item` nunca puede ser negativa.  
- El __"Aged Brie"__ en realidad incrementa su `Quality` cuanto más viejo se hace.  
- La `Quality` de un `Item` jamás supera `50`.  
- __"Sulfuras"__, al ser un objeto legendario, nunca necesita ser vendido ni disminuye su `Quality`.  
- Las __"Lucas The Bard tickets"__, como el Aged Brie, aumentan en `Quality` a medida que se aproxima su `SellIn`;  
  - La `Quality` aumenta en `2` cuando quedan `10` días o menos, y en `3` cuando quedan `5` días o menos, pero  
  - La `Quality` cae a `0` después del concierto.  

Recientemente hemos firmado con un proveedor de objetos **Conjured**. Esto requiere una actualización en nuestro sistema:  

- Los objetos __"Conjured"__ se degradan en `Quality` el doble de rápido que los objetos normales.  

Sentíos libres de modificar el método `UpdateQuality` y añadir cualquier nuevo código, siempre que todo continúe funcionando correctamente. Sin embargo, no alteréis la clase `Item` ni la propiedad `Items`, pues pertenecen al goblin que habita en la esquina, quien entraría en cólera al instante y os despacharía de un solo golpe, ya que no cree en la propiedad compartida del código (podéis hacer que el método `UpdateQuality` y la propiedad `Items` sean estáticos si lo deseáis, nosotros os cubriremos).  

Para dejarlo claro: un `Item` nunca puede tener su `Quality` por encima de `50`. No obstante, __"Sulfuras"__ es un objeto legendario y, como tal, su `Quality` es de `80` y nunca varía.  
