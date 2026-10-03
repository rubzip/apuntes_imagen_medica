# Módulo 0. Caja de herramientas básicas

*Cómo sobrevivir a la física sin ser matemático*

> **Al terminar este módulo sabrás:**
> - Expresar una medida con su magnitud y su unidad, y distinguir las unidades del Sistema Internacional.
> - Convertir unidades usando los prefijos (kilo, mili, micro, nano…).
> - Leer y escribir números muy grandes o muy pequeños en notación científica.
> - Reconocer una relación directamente proporcional y una inversamente proporcional.
> - Despejar una incógnita en una fórmula sencilla y comprobar las unidades del resultado.
> - Manejar fracciones, porcentajes y potencias sencillas, y leer una gráfica.

---

## ¿Para qué sirve este módulo?

Si llevas años sin tocar una calculadora, es normal que las letras griegas y los números con exponentes te den respeto. **No te preocupes.** Este módulo repasa, desde cero y sin rodeos, el «idioma» básico que necesitas para entender los equipos del hospital.

Estas son las herramientas que vas a usar en el resto del libro:

| Herramienta | Para qué te servirá |
|---|---|
| **Unidades y prefijos** | Entender qué significan 80 kV, 200 mA, 100 MHz o 500 nm |
| **Notación científica** | Manejar la velocidad de la luz (3 × 10⁸ m/s) o el tamaño de un átomo (10⁻¹⁰ m) |
| **Proporcionalidad** | Entender cómo se relacionan frecuencia y longitud de onda, o kilovoltaje y energía |
| **Despejar fórmulas** | Calcular una longitud de onda, una distancia o un tiempo |
| **Fracciones y porcentajes** | Calcular cuánta cantidad queda de una muestra radiactiva |
| **Leer gráficas** | Interpretar las curvas y los espectros del libro |

> **Idea clave:** no hace falta memorizar nada «como un loro». Solo hay que entender **cómo se relacionan las cosas**. Vas a hacer pocos cálculos y todos son sencillos.

---

## 0.1. Magnitudes y unidades: el idioma de medir

En física, **todo lo que se puede medir** se llama **magnitud**: el tiempo, la longitud, la temperatura, la masa…

Pero **un número solo no significa nada**. Si te digo «el paciente pesa 80», ¿80 kilos? ¿80 gramos? ¿80 libras? Falta algo.

> **La unidad es el «apellido» del número.** Sin ella, el número no dice nada.

| Medida | ¿Vale? |
|---|---|
| «El paciente pesa 80» | ❌ falta la unidad |
| «El paciente pesa **80 kg**» | ✅ |
| «El tubo funciona a 100» | ❌ |
| «El tubo funciona a **100 kV**» | ✅ |

### El Sistema Internacional (SI)

Para que todo el mundo mida igual, existe un acuerdo mundial: el **Sistema Internacional de Unidades (SI)**. Estas son las unidades que más vas a ver:

| Magnitud | Unidad SI | Símbolo | Dónde la verás |
|---|---|---|---|
| **Longitud** | metro | m | Longitud de onda (Módulo 4) |
| **Tiempo** | segundo | s | Periodo, vida media (Módulos 4 y 6) |
| **Masa** | kilogramo | kg | Masa de las partículas (Módulo 1) |
| **Frecuencia** | hercio | Hz | Ondas (Módulos 4 y 5) |
| **Tensión eléctrica** | voltio | V | Tubo de rayos X (Módulo 5) |
| **Intensidad de corriente** | amperio | A | Equipos de rayos X |
| **Energía** | julio (J) y electronvoltio (eV) | J, eV | Fotones (Módulos 1 y 5) |
| **Campo magnético** | tesla | T | Resonancia magnética (Módulo 7) |
| **Actividad** | becquerel | Bq | Radiactividad (Módulo 6) |

> **El hercio (Hz) en una frase:** 1 Hz es **una vez por segundo**. Es decir, Hz = 1 / s. Una onda de 50 Hz hace 50 ciclos cada segundo.

> **Cuidado con las letras:** la misma letra puede ser una magnitud o una unidad. Por ejemplo, **m** puede ser la **masa** o el **metro**. Fíjate siempre en el contexto.

---

## 0.2. Los prefijos multiplicadores: de lo gigante a lo diminuto

En un hospital se miden cosas **inmensamente grandes** (como la frecuencia de un ecógrafo) y cosas **ridículamente pequeñas** (como una célula o una onda de rayos X). Para no escribir chorros de ceros, ponemos un **prefijo** delante de la unidad.

![Escalera de prefijos del Sistema Internacional](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NDAgMzA1IiBmb250LWZhbWlseT0iQXJpYWwsSGVsdmV0aWNhLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTUiPjxyZWN0IHdpZHRoPSI2NDAiIGhlaWdodD0iMzA1IiBmaWxsPSIjZmZmIi8+PGRlZnM+PG1hcmtlciBpZD0ibWIiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjMjU2M2ViIi8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibXIiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjZGMyNjI2Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWciIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjMTU4MDNkIi8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWsiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjNTU1NTU1Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibW8iIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjZWE1ODBjIi8+PC9tYXJrZXI+PC9kZWZzPjxyZWN0IHg9IjE0IiB5PSI0NCIgd2lkdGg9IjY2IiBoZWlnaHQ9IjE0NiIgZmlsbD0iI2MyNDEwYyIgc3Ryb2tlPSIjMzMzIiBzdHJva2Utd2lkdGg9IjEiLz48dGV4dCB4PSI0NyIgeT0iNzIiIGZpbGw9IiNmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMjQiIGZvbnQtd2VpZ2h0PSJib2xkIj5UPC90ZXh0Pjx0ZXh0IHg9IjQ3IiB5PSIyMDgiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTQiIGZvbnQtd2VpZ2h0PSJib2xkIj50ZXJhPC90ZXh0Pjx0ZXh0IHg9IjQ3IiB5PSIyMjUiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiPjEwwrnCsjwvdGV4dD48dGV4dCB4PSI0NyIgeT0iMjQxIiBmaWxsPSIjNTU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIj51biBiaWxsw7NuPC90ZXh0PjxyZWN0IHg9Ijg0IiB5PSI1OCIgd2lkdGg9IjY2IiBoZWlnaHQ9IjEzMiIgZmlsbD0iI2VhNTgwYyIgc3Ryb2tlPSIjMzMzIiBzdHJva2Utd2lkdGg9IjEiLz48dGV4dCB4PSIxMTciIHk9Ijg2IiBmaWxsPSIjZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjI0IiBmb250LXdlaWdodD0iYm9sZCI+RzwvdGV4dD48dGV4dCB4PSIxMTciIHk9IjIwOCIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9ImJvbGQiPmdpZ2E8L3RleHQ+PHRleHQgeD0iMTE3IiB5PSIyMjUiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiPjEw4oG5PC90ZXh0Pjx0ZXh0IHg9IjExNyIgeT0iMjQxIiBmaWxsPSIjNTU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIj5taWwgbWlsbG9uZXM8L3RleHQ+PHJlY3QgeD0iMTU0IiB5PSI3MiIgd2lkdGg9IjY2IiBoZWlnaHQ9IjExOCIgZmlsbD0iI2Y5NzMxNiIgc3Ryb2tlPSIjMzMzIiBzdHJva2Utd2lkdGg9IjEiLz48dGV4dCB4PSIxODciIHk9IjEwMCIgZmlsbD0iI2ZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIyNCIgZm9udC13ZWlnaHQ9ImJvbGQiPk08L3RleHQ+PHRleHQgeD0iMTg3IiB5PSIyMDgiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTQiIGZvbnQtd2VpZ2h0PSJib2xkIj5tZWdhPC90ZXh0Pjx0ZXh0IHg9IjE4NyIgeT0iMjI1IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIj4xMOKBtjwvdGV4dD48dGV4dCB4PSIxODciIHk9IjI0MSIgZmlsbD0iIzU1NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSI+dW4gbWlsbMOzbjwvdGV4dD48cmVjdCB4PSIyMjQiIHk9Ijg2IiB3aWR0aD0iNjYiIGhlaWdodD0iMTA0IiBmaWxsPSIjZmI5MjNjIiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMSIvPjx0ZXh0IHg9IjI1NyIgeT0iMTE0IiBmaWxsPSIjZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjI0IiBmb250LXdlaWdodD0iYm9sZCI+azwvdGV4dD48dGV4dCB4PSIyNTciIHk9IjIwOCIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9ImJvbGQiPmtpbG88L3RleHQ+PHRleHQgeD0iMjU3IiB5PSIyMjUiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiPjEwwrM8L3RleHQ+PHRleHQgeD0iMjU3IiB5PSIyNDEiIGZpbGw9IiM1NTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiPm1pbDwvdGV4dD48cmVjdCB4PSIyOTQiIHk9IjEwMCIgd2lkdGg9IjY2IiBoZWlnaHQ9IjkwIiBmaWxsPSIjNmI3MjgwIiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMSIvPjx0ZXh0IHg9IjMyNyIgeT0iMTI4IiBmaWxsPSIjZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjI0IiBmb250LXdlaWdodD0iYm9sZCI+4oCUPC90ZXh0Pjx0ZXh0IHg9IjMyNyIgeT0iMjA4IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjE0IiBmb250LXdlaWdodD0iYm9sZCI+dW5pZGFkPC90ZXh0Pjx0ZXh0IHg9IjMyNyIgeT0iMjI1IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIj4xMOKBsDwvdGV4dD48dGV4dCB4PSIzMjciIHk9IjI0MSIgZmlsbD0iIzU1NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSI+dW5vPC90ZXh0PjxyZWN0IHg9IjM2NCIgeT0iMTE0IiB3aWR0aD0iNjYiIGhlaWdodD0iNzYiIGZpbGw9IiM2MGE1ZmEiIHN0cm9rZT0iIzMzMyIgc3Ryb2tlLXdpZHRoPSIxIi8+PHRleHQgeD0iMzk3IiB5PSIxNDIiIGZpbGw9IiNmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMjQiIGZvbnQtd2VpZ2h0PSJib2xkIj5tPC90ZXh0Pjx0ZXh0IHg9IjM5NyIgeT0iMjA4IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjE0IiBmb250LXdlaWdodD0iYm9sZCI+bWlsaTwvdGV4dD48dGV4dCB4PSIzOTciIHk9IjIyNSIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyI+MTDigbvCszwvdGV4dD48dGV4dCB4PSIzOTciIHk9IjI0MSIgZmlsbD0iIzU1NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSI+bWlsw6lzaW1hPC90ZXh0PjxyZWN0IHg9IjQzNCIgeT0iMTI4IiB3aWR0aD0iNjYiIGhlaWdodD0iNjIiIGZpbGw9IiMzYjgyZjYiIHN0cm9rZT0iIzMzMyIgc3Ryb2tlLXdpZHRoPSIxIi8+PHRleHQgeD0iNDY3IiB5PSIxNTYiIGZpbGw9IiNmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMjQiIGZvbnQtd2VpZ2h0PSJib2xkIj7OvDwvdGV4dD48dGV4dCB4PSI0NjciIHk9IjIwOCIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9ImJvbGQiPm1pY3JvPC90ZXh0Pjx0ZXh0IHg9IjQ2NyIgeT0iMjI1IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIj4xMOKBu+KBtjwvdGV4dD48dGV4dCB4PSI0NjciIHk9IjI0MSIgZmlsbD0iIzU1NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSI+bWlsbG9uw6lzaW1hPC90ZXh0PjxyZWN0IHg9IjUwNCIgeT0iMTQyIiB3aWR0aD0iNjYiIGhlaWdodD0iNDgiIGZpbGw9IiMyNTYzZWIiIHN0cm9rZT0iIzMzMyIgc3Ryb2tlLXdpZHRoPSIxIi8+PHRleHQgeD0iNTM3IiB5PSIxNzAiIGZpbGw9IiNmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMjQiIGZvbnQtd2VpZ2h0PSJib2xkIj5uPC90ZXh0Pjx0ZXh0IHg9IjUzNyIgeT0iMjA4IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjE0IiBmb250LXdlaWdodD0iYm9sZCI+bmFubzwvdGV4dD48dGV4dCB4PSI1MzciIHk9IjIyNSIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyI+MTDigbvigbk8L3RleHQ+PHRleHQgeD0iNTM3IiB5PSIyNDEiIGZpbGw9IiM1NTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiPm1pbDwvdGV4dD48dGV4dCB4PSI1MzciIHk9IjI1NCIgZmlsbD0iIzU1NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSI+bWlsbG9uw6lzaW1hPC90ZXh0PjxyZWN0IHg9IjU3NCIgeT0iMTU2IiB3aWR0aD0iNjYiIGhlaWdodD0iMzQiIGZpbGw9IiMxZDRlZDgiIHN0cm9rZT0iIzMzMyIgc3Ryb2tlLXdpZHRoPSIxIi8+PHRleHQgeD0iNjA3IiB5PSIxODQiIGZpbGw9IiNmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMjQiIGZvbnQtd2VpZ2h0PSJib2xkIj5wPC90ZXh0Pjx0ZXh0IHg9IjYwNyIgeT0iMjA4IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjE0IiBmb250LXdlaWdodD0iYm9sZCI+cGljbzwvdGV4dD48dGV4dCB4PSI2MDciIHk9IjIyNSIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyI+MTDigbvCucKyPC90ZXh0Pjx0ZXh0IHg9IjYwNyIgeT0iMjQxIiBmaWxsPSIjNTU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIj5iaWxsb27DqXNpbWE8L3RleHQ+PGxpbmUgeDE9IjQwIiB5MT0iMjY4IiB4Mj0iNTkwIiB5Mj0iMjY4IiBzdHJva2U9IiM1NTU1NTUiIHN0cm9rZS13aWR0aD0iMyIgbWFya2VyLWVuZD0idXJsKCNtaykiIG1hcmtlci1zdGFydD0idXJsKCNtaykiLz48dGV4dCB4PSIzMTUiIHk9IjI5MCIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9ImJvbGQiPkNhZGEgZXNjYWzDs246IMOXIDEgMDAwIGhhY2lhIGxhIGl6cXVpZXJkYSwgw7cgMSAwMDAgaGFjaWEgbGEgZGVyZWNoYTwvdGV4dD48dGV4dCB4PSIzMTUiIHk9IjE4IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjE2IiBmb250LXdlaWdodD0iYm9sZCI+UHJlZmlqb3M6IGRlIGxvIGdpZ2FudGUgYSBsbyBkaW1pbnV0bzwvdGV4dD48L3N2Zz4=)

*Figura 1. La escalera de prefijos. Cada escalón multiplica por 1 000 (hacia la izquierda) o divide entre 1 000 (hacia la derecha).*

### Para hacer las cosas más grandes

| Prefijo | Símbolo | Significa | Ejemplo |
|---|---|---|---|
| **tera** | T | un billón (10¹²) | — |
| **giga** | G | mil millones (10⁹) | 3 GHz = 3 000 millones de hercios |
| **mega** | M | un millón (10⁶) | 100 MHz = 100 millones de hercios |
| **kilo** | k | mil (10³) | 80 kV = 80 000 voltios |

### Para hacer las cosas más pequeñas

| Prefijo | Símbolo | Significa | Ejemplo |
|---|---|---|---|
| **mili** | m | la milésima parte (10⁻³) | 1 mm = 0,001 m |
| **micro** | μ | la millonésima parte (10⁻⁶) | 1 μm = 0,000001 m |
| **nano** | n | la milmillonésima parte (10⁻⁹) | 500 nm = luz verde |
| **pico** | p | la billonésima parte (10⁻¹²) | — |

> **Cuidado: mayúscula y minúscula importan.** La **M mayúscula** es **mega** (un millón) y la **m minúscula** es **mili** (una milésima). Un megahercio (MHz) y un milihercio (mHz) se diferencian en **mil millones de veces**. En cambio, **kilo** siempre es **k minúscula**.

### Los prefijos en el hospital

| Lo que verás | Qué significa | Dónde |
|---|---|---|
| **80 kV** | 80 000 voltios | Tensión de un tubo de rayos X |
| **200 mA** | 0,2 amperios | Corriente de un equipo de rayos X |
| **100 MHz** | 100 millones de hercios | Frecuencia de una onda de radio |
| **500 nm** | 0,0000005 m | Longitud de onda de la luz verde |
| **60 keV** | 60 000 electronvoltios | Energía de un fotón de rayos X |
| **600 MBq** | 600 millones de becquerelios | Actividad de una dosis de tecnecio-99m |

### Cómo convertir unidades, paso a paso

1. **Mira el prefijo** y cambia su significado por su valor.
2. **Multiplica** (si es un prefijo «grande») o **divide** (si es «pequeño»).

#### Ejemplos resueltos

**1. Pasa 2,5 kV a voltios.**

- kilo = 1 000.
- 2,5 × 1 000 = **2 500 V**.

**2. Pasa 150 mA a amperios.**

- mili = una milésima, así que hay que dividir entre 1 000.
- 150 / 1 000 = **0,15 A**.

**3. Pasa 100 MHz a hercios.**

- mega = un millón.
- 100 × 1 000 000 = **100 000 000 Hz** (que es 10⁸ Hz).

**4. Pasa 0,5 mm a micrómetros.**

- De mili a micro se baja un escalón (Figura 1) y hay que multiplicar por 1 000.
- 0,5 × 1 000 = **500 μm**.

**5. Pasa 6 horas a segundos.**

- 1 hora = 3 600 s.
- 6 × 3 600 = **21 600 s**.

> **Truco:** si pasas a una unidad **más pequeña**, el número **sale mayor** (hay más «trocitos»). Si pasas a una **más grande**, el número **sale menor**. Compruébalo siempre.

---

## 0.3. Notación científica: el truco del «10»

Incluso con prefijos, a veces los números son inmanejables. La velocidad de la luz es aproximadamente **300 000 000 m/s**. Para simplificar, la física usa la **notación científica**, que consiste en un número multiplicado por **10 elevado a una potencia**:

> **número × 10 elevado a n**

### Exponente positivo: números grandes

El exponente nos dice **cuántos ceros** hay que añadir.

- Velocidad de la luz: **3 × 10⁸ m/s** = 3 seguido de 8 ceros = 300 000 000 m/s.

### Exponente negativo: números diminutos

El exponente nos dice **cuántos saltos da la coma hacia la izquierda**.

- Tamaño de un átomo: **10⁻¹⁰ m** = 0,0000000001 m.

> **Truco mental:** si el exponente lleva un **«menos»**, estás hablando de algo **microscópico**.

### Cómo pasar un número a notación científica

1. Coloca la coma **detrás de la primera cifra distinta de cero**.
2. Cuenta **cuántos lugares** has movido la coma: ese número es el exponente.
3. Si has movido la coma **hacia la izquierda**, el exponente es **positivo**. Si la has movido **hacia la derecha**, es **negativo**.

| Número | Cómo se mueve la coma | Notación científica |
|---|---|---|
| 150 000 | 5 lugares a la izquierda | **1,5 × 10⁵** |
| 4 500 000 | 6 lugares a la izquierda | **4,5 × 10⁶** |
| 0,0003 | 4 lugares a la derecha | **3 × 10⁻⁴** |
| 0,00072 | 4 lugares a la derecha | **7,2 × 10⁻⁴** |

Para hacerlo **al revés** (de notación científica a número normal): 2,4 × 10³ = **2 400** y 6 × 10⁻² = **0,06**.

### Para qué sirve ver el orden de magnitud

![Regla de tamaños de 10⁻¹⁵ m a 1 m](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MDAgMjg1IiBmb250LWZhbWlseT0iQXJpYWwsSGVsdmV0aWNhLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTUiPjxyZWN0IHdpZHRoPSI2MDAiIGhlaWdodD0iMjg1IiBmaWxsPSIjZmZmIi8+PGRlZnM+PG1hcmtlciBpZD0ibWIiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjMjU2M2ViIi8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibXIiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjZGMyNjI2Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWciIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjMTU4MDNkIi8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWsiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjNTU1NTU1Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibW8iIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjZWE1ODBjIi8+PC9tYXJrZXI+PC9kZWZzPjxsaW5lIHgxPSI0MCIgeTE9IjE1MCIgeDI9IjU2MCIgeTI9IjE1MCIgc3Ryb2tlPSIjNTU1NTU1IiBzdHJva2Utd2lkdGg9IjMiLz48bGluZSB4MT0iNDAuMCIgeTE9IjE0NSIgeDI9IjQwLjAiIHkyPSIxNTUiIHN0cm9rZT0iIzU1NTU1NSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48bGluZSB4MT0iNzIuNSIgeTE9IjE0NSIgeDI9IjcyLjUiIHkyPSIxNTUiIHN0cm9rZT0iIzU1NTU1NSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48bGluZSB4MT0iMTA1LjAiIHkxPSIxNDUiIHgyPSIxMDUuMCIgeTI9IjE1NSIgc3Ryb2tlPSIjNTU1NTU1IiBzdHJva2Utd2lkdGg9IjEuNSIvPjxsaW5lIHgxPSIxMzcuNSIgeTE9IjE0NSIgeDI9IjEzNy41IiB5Mj0iMTU1IiBzdHJva2U9IiM1NTU1NTUiIHN0cm9rZS13aWR0aD0iMS41Ii8+PGxpbmUgeDE9IjE3MC4wIiB5MT0iMTQ1IiB4Mj0iMTcwLjAiIHkyPSIxNTUiIHN0cm9rZT0iIzU1NTU1NSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48bGluZSB4MT0iMjAyLjUiIHkxPSIxNDUiIHgyPSIyMDIuNSIgeTI9IjE1NSIgc3Ryb2tlPSIjNTU1NTU1IiBzdHJva2Utd2lkdGg9IjEuNSIvPjxsaW5lIHgxPSIyMzUuMCIgeTE9IjE0NSIgeDI9IjIzNS4wIiB5Mj0iMTU1IiBzdHJva2U9IiM1NTU1NTUiIHN0cm9rZS13aWR0aD0iMS41Ii8+PGxpbmUgeDE9IjI2Ny41IiB5MT0iMTQ1IiB4Mj0iMjY3LjUiIHkyPSIxNTUiIHN0cm9rZT0iIzU1NTU1NSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48bGluZSB4MT0iMzAwLjAiIHkxPSIxNDUiIHgyPSIzMDAuMCIgeTI9IjE1NSIgc3Ryb2tlPSIjNTU1NTU1IiBzdHJva2Utd2lkdGg9IjEuNSIvPjxsaW5lIHgxPSIzMzIuNSIgeTE9IjE0NSIgeDI9IjMzMi41IiB5Mj0iMTU1IiBzdHJva2U9IiM1NTU1NTUiIHN0cm9rZS13aWR0aD0iMS41Ii8+PGxpbmUgeDE9IjM2NS4wIiB5MT0iMTQ1IiB4Mj0iMzY1LjAiIHkyPSIxNTUiIHN0cm9rZT0iIzU1NTU1NSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48bGluZSB4MT0iMzk3LjUiIHkxPSIxNDUiIHgyPSIzOTcuNSIgeTI9IjE1NSIgc3Ryb2tlPSIjNTU1NTU1IiBzdHJva2Utd2lkdGg9IjEuNSIvPjxsaW5lIHgxPSI0MzAuMCIgeTE9IjE0NSIgeDI9IjQzMC4wIiB5Mj0iMTU1IiBzdHJva2U9IiM1NTU1NTUiIHN0cm9rZS13aWR0aD0iMS41Ii8+PGxpbmUgeDE9IjQ2Mi41IiB5MT0iMTQ1IiB4Mj0iNDYyLjUiIHkyPSIxNTUiIHN0cm9rZT0iIzU1NTU1NSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48bGluZSB4MT0iNDk1LjAiIHkxPSIxNDUiIHgyPSI0OTUuMCIgeTI9IjE1NSIgc3Ryb2tlPSIjNTU1NTU1IiBzdHJva2Utd2lkdGg9IjEuNSIvPjxsaW5lIHgxPSI1MjcuNSIgeTE9IjE0NSIgeDI9IjUyNy41IiB5Mj0iMTU1IiBzdHJva2U9IiM1NTU1NTUiIHN0cm9rZS13aWR0aD0iMS41Ii8+PGxpbmUgeDE9IjU2MC4wIiB5MT0iMTQ1IiB4Mj0iNTYwLjAiIHkyPSIxNTUiIHN0cm9rZT0iIzU1NTU1NSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48dGV4dCB4PSI0MC4wIiB5PSIxNzIiIGZpbGw9IiM1NTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTIiPjEw4oG7wrnigbUgbTwvdGV4dD48dGV4dCB4PSIyMDIuNSIgeT0iMTcyIiBmaWxsPSIjNTU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEyIj4xMOKBu8K54oGwIG08L3RleHQ+PHRleHQgeD0iMzY1LjAiIHk9IjE3MiIgZmlsbD0iIzU1NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMiI+MTDigbvigbUgbTwvdGV4dD48dGV4dCB4PSI1MjcuNSIgeT0iMTcyIiBmaWxsPSIjNTU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEyIj4xIG08L3RleHQ+PGNpcmNsZSBjeD0iNDAuMCIgY3k9IjE1MCIgcj0iNiIgZmlsbD0iI2RjMjYyNiIgc3Ryb2tlPSIjMzMzIiBzdHJva2Utd2lkdGg9IjEiLz48bGluZSB4MT0iNDAuMCIgeTE9IjE0MyIgeDI9IjQwLjAiIHkyPSIxMTkiIHN0cm9rZT0iI2RjMjYyNiIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48dGV4dCB4PSIxNC4wIiB5PSI5OSIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9InN0YXJ0IiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iYm9sZCI+bsO6Y2xlbzwvdGV4dD48dGV4dCB4PSIxNC4wIiB5PSIxMTUiIGZpbGw9IiNkYzI2MjYiIHRleHQtYW5jaG9yPSJzdGFydCIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9ImJvbGQiPuKJiCAxMOKBu8K54oG1IG08L3RleHQ+PGNpcmNsZSBjeD0iMjAyLjUiIGN5PSIxNTAiIHI9IjYiIGZpbGw9IiNkYzI2MjYiIHN0cm9rZT0iIzMzMyIgc3Ryb2tlLXdpZHRoPSIxIi8+PGxpbmUgeDE9IjIwMi41IiB5MT0iMTQzIiB4Mj0iMjAyLjUiIHkyPSIxMTkiIHN0cm9rZT0iI2RjMjYyNiIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48dGV4dCB4PSIyMDIuNSIgeT0iOTkiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSJib2xkIj7DoXRvbW88L3RleHQ+PHRleHQgeD0iMjAyLjUiIHk9IjExNSIgZmlsbD0iI2RjMjYyNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9ImJvbGQiPuKJiCAxMOKBu8K54oGwIG08L3RleHQ+PGNpcmNsZSBjeD0iMzIyLjciIGN5PSIxNTAiIHI9IjYiIGZpbGw9IiMyNTYzZWIiIHN0cm9rZT0iIzMzMyIgc3Ryb2tlLXdpZHRoPSIxIi8+PGxpbmUgeDE9IjMyMi43IiB5MT0iMTU3IiB4Mj0iMzIyLjciIHkyPSIxOTIiIHN0cm9rZT0iIzI1NjNlYiIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48dGV4dCB4PSIzMjIuNyIgeT0iMjA4IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iYm9sZCI+bHV6IHZpc2libGUgKM67KTwvdGV4dD48dGV4dCB4PSIzMjIuNyIgeT0iMjI0IiBmaWxsPSIjMjU2M2ViIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iYm9sZCI+4omIIDUgw5cgMTDigbvigbcgbTwvdGV4dD48Y2lyY2xlIGN4PSIzNjAuMCIgY3k9IjE1MCIgcj0iNiIgZmlsbD0iIzE1ODAzZCIgc3Ryb2tlPSIjMzMzIiBzdHJva2Utd2lkdGg9IjEiLz48bGluZSB4MT0iMzYwLjAiIHkxPSIxNDMiIHgyPSIzNjAuMCIgeTI9IjExOSIgc3Ryb2tlPSIjMTU4MDNkIiBzdHJva2Utd2lkdGg9IjEuNSIvPjx0ZXh0IHg9IjM2MC4wIiB5PSI5OSIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9ImJvbGQiPmdsw7NidWxvIHJvam88L3RleHQ+PHRleHQgeD0iMzYwLjAiIHk9IjExNSIgZmlsbD0iIzE1ODAzZCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9ImJvbGQiPuKJiCA3IMOXIDEw4oG74oG2IG08L3RleHQ+PGNpcmNsZSBjeD0iMzk3LjUiIGN5PSIxNTAiIHI9IjYiIGZpbGw9IiMxNTgwM2QiIHN0cm9rZT0iIzMzMyIgc3Ryb2tlLXdpZHRoPSIxIi8+PGxpbmUgeDE9IjM5Ny41IiB5MT0iMTU3IiB4Mj0iMzk3LjUiIHkyPSIyMzYiIHN0cm9rZT0iIzE1ODAzZCIgc3Ryb2tlLXdpZHRoPSIxLjUiLz48dGV4dCB4PSIzOTcuNSIgeT0iMjUyIiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iYm9sZCI+Z3Jvc29yIGRlIHVuIHBlbG88L3RleHQ+PHRleHQgeD0iMzk3LjUiIHk9IjI2OCIgZmlsbD0iIzE1ODAzZCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9ImJvbGQiPuKJiCAxMOKBu+KBtCBtPC90ZXh0PjxjaXJjbGUgY3g9IjUzNS44IiBjeT0iMTUwIiByPSI2IiBmaWxsPSIjMTU4MDNkIiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMSIvPjxsaW5lIHgxPSI1MzUuOCIgeTE9IjE0MyIgeDI9IjUzNS44IiB5Mj0iMTE5IiBzdHJva2U9IiMxNTgwM2QiIHN0cm9rZS13aWR0aD0iMS41Ii8+PHRleHQgeD0iNTM1LjgiIHk9Ijk5IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iYm9sZCI+dW5hIHBlcnNvbmE8L3RleHQ+PHRleHQgeD0iNTM1LjgiIHk9IjExNSIgZmlsbD0iIzE1ODAzZCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9ImJvbGQiPuKJiCAyIG08L3RleHQ+PHRleHQgeD0iMjAyLjUiIHk9IjgwIiBmaWxsPSIjZWE1ODBjIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iYm9sZCI+cmF5b3MgWDogzrsg4omIIDEw4oG7wrnigbAgbTwvdGV4dD48dGV4dCB4PSIzMTAiIHk9IjIyIiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjE0IiBmb250LXdlaWdodD0iYm9sZCI+Q2FkYSBtYXJjYSB2YWxlIDEwIHZlY2VzIG3DoXMgcXVlIGxhIGFudGVyaW9yPC90ZXh0Pjwvc3ZnPg==)

*Figura 2. Una regla de tamaños, de 10⁻¹⁵ m a 1 m. Cada marca vale 10 veces más que la anterior. Los rayos X tienen una longitud de onda parecida al tamaño de un átomo.*

Esto explica muchas cosas: un átomo es **cien mil veces más grande que su núcleo**, y una persona es **unas 20 000 millones de veces más grande que un átomo**.

### Multiplicar y dividir con potencias de 10

Solo hay dos reglas:

- **Multiplicar:** se **suman** los exponentes.
- **Dividir:** se **restan** los exponentes.

| Operación | Cómo se hace | Resultado |
|---|---|---|
| (2 × 10³) · (3 × 10⁴) | 2 · 3 = 6 y 3 + 4 = 7 | **6 × 10⁷** |
| (6 × 10⁸) / (2 × 10³) | 6 / 2 = 3 y 8 − 3 = 5 | **3 × 10⁵** |
| (3 × 10⁸) / (1 × 10⁸) | 3 / 1 = 3 y 8 − 8 = 0 | **3 × 10⁰ = 3** |

> **Recuerda:** cualquier número elevado a 0 vale 1. Así, 10⁰ = 1.

Si el resultado no tiene una sola cifra delante de la coma, se ajusta. Ejemplo: (3 × 10⁸) / (5 × 10¹⁴) = 0,6 × 10⁻⁶ = **6 × 10⁻⁷** (moviendo la coma un lugar a la derecha, el exponente baja en uno). Es la cuenta de la longitud de onda de la luz verde que verás en el Módulo 5.

### Ejemplo resuelto: ¿cuánto tarda la luz del Sol en llegar a la Tierra?

- Distancia: 1,5 × 10¹¹ m. Velocidad: 3 × 10⁸ m/s.
- Tiempo = distancia / velocidad = (1,5 × 10¹¹) / (3 × 10⁸).
- 1,5 / 3 = 0,5 y 11 − 8 = 3, así que el tiempo es 0,5 × 10³ = **500 s**, es decir, unos **8 minutos**.

> **En la calculadora:** para escribir 3 × 10⁸, pulsa la tecla **EXP** (o **×10ˣ**): **3 · EXP · 8**. Si tu calculadora no la tiene, puedes escribir 3 × 10 ^ 8.

---

## 0.4. Proporcionalidad: la regla del «si tú subes, yo bajo»

En el libro encontrarás leyes y fórmulas muy sencillas. Solo hay **dos tipos de relaciones**.

![Proporcionalidad directa e inversa](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NDAgMzIwIiBmb250LWZhbWlseT0iQXJpYWwsSGVsdmV0aWNhLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTUiPjxyZWN0IHdpZHRoPSI2NDAiIGhlaWdodD0iMzIwIiBmaWxsPSIjZmZmIi8+PGRlZnM+PG1hcmtlciBpZD0ibWIiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjMjU2M2ViIi8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibXIiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjZGMyNjI2Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWciIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjMTU4MDNkIi8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWsiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjNTU1NTU1Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibW8iIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjZWE1ODBjIi8+PC9tYXJrZXI+PC9kZWZzPjx0ZXh0IHg9IjE3MCIgeT0iMTYiIGZpbGw9IiMyNTYzZWIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTYiIGZvbnQtd2VpZ2h0PSJib2xkIj5EaXJlY3RhbWVudGUgcHJvcG9yY2lvbmFsPC90ZXh0Pjx0ZXh0IHg9IjQ4MCIgeT0iMTYiIGZpbGw9IiNkYzI2MjYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTYiIGZvbnQtd2VpZ2h0PSJib2xkIj5JbnZlcnNhbWVudGUgcHJvcG9yY2lvbmFsPC90ZXh0PjxsaW5lIHgxPSI2MCIgeTE9IjIzMCIgeDI9IjI5MCIgeTI9IjIzMCIgc3Ryb2tlPSIjNTU1NTU1IiBzdHJva2Utd2lkdGg9IjIuNSIgbWFya2VyLWVuZD0idXJsKCNtaykiLz48bGluZSB4MT0iNjAiIHkxPSIyMzAiIHgyPSI2MCIgeTI9IjU1IiBzdHJva2U9IiM1NTU1NTUiIHN0cm9rZS13aWR0aD0iMi41IiBtYXJrZXItZW5kPSJ1cmwoI21rKSIvPjxsaW5lIHgxPSI2MCIgeTE9IjIzMCIgeDI9IjI3OS42IiB5Mj0iNTkuNjAwMDAwMDAwMDAwMDIiIHN0cm9rZT0iIzI1NjNlYiIgc3Ryb2tlLXdpZHRoPSIzLjUiLz48dGV4dCB4PSI2MCIgeT0iMzYiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJzdGFydCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9ImJvbGQiPmVuZXJnw61hIG3DoXhpbWEgKGtlVik8L3RleHQ+PHRleHQgeD0iMTc1IiB5PSIyNjYiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSJib2xkIj50ZW5zacOzbiBkZWwgdHVibyAoa1YpPC90ZXh0PjxjaXJjbGUgY3g9IjEzMy4yIiBjeT0iMTczLjIiIHI9IjYiIGZpbGw9IiMyNTYzZWIiIHN0cm9rZT0iIzMzMyIgc3Ryb2tlLXdpZHRoPSIxIi8+PHRleHQgeD0iMTMzLjIiIHk9IjI0NyIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMiI+NDA8L3RleHQ+PHRleHQgeD0iMTQyLjIiIHk9IjE4OS4yIiBmaWxsPSIjMjU2M2ViIiB0ZXh0LWFuY2hvcj0ic3RhcnQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSJib2xkIj4oNDA7IDQwKTwvdGV4dD48Y2lyY2xlIGN4PSIyMDYuNCIgY3k9IjExNi40IiByPSI2IiBmaWxsPSIjMjU2M2ViIiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMSIvPjx0ZXh0IHg9IjIwNi40IiB5PSIyNDciIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTIiPjgwPC90ZXh0Pjx0ZXh0IHg9IjIxNS40IiB5PSIxMzIuNCIgZmlsbD0iIzI1NjNlYiIgdGV4dC1hbmNob3I9InN0YXJ0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iYm9sZCI+KDgwOyA4MCk8L3RleHQ+PGNpcmNsZSBjeD0iMjc5LjYiIGN5PSI1OS42IiByPSI2IiBmaWxsPSIjMjU2M2ViIiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMSIvPjx0ZXh0IHg9IjI3OS42IiB5PSIyNDciIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTIiPjEyMDwvdGV4dD48dGV4dCB4PSIyODguNiIgeT0iNzUuNiIgZmlsbD0iIzI1NjNlYiIgdGV4dC1hbmNob3I9InN0YXJ0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iYm9sZCI+KDEyMDsgMTIwKTwvdGV4dD48dGV4dCB4PSIxNzAiIHk9IjI4OCIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyI+U2kgc2UgZHVwbGljYSBlbCBrViAoNDAg4oaSIDgwKSw8L3RleHQ+PHRleHQgeD0iMTcwIiB5PSIzMDUiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiPnNlIGR1cGxpY2EgbGEgZW5lcmfDrWEgKDQwIOKGkiA4MCkuPC90ZXh0PjxsaW5lIHgxPSIzODAiIHkxPSIyMzAiIHgyPSI2MTAiIHkyPSIyMzAiIHN0cm9rZT0iIzU1NTU1NSIgc3Ryb2tlLXdpZHRoPSIyLjUiIG1hcmtlci1lbmQ9InVybCgjbWspIi8+PGxpbmUgeDE9IjM4MCIgeTE9IjIzMCIgeDI9IjM4MCIgeTI9IjU1IiBzdHJva2U9IiM1NTU1NTUiIHN0cm9rZS13aWR0aD0iMi41IiBtYXJrZXItZW5kPSJ1cmwoI21rKSIvPjxwb2x5bGluZSBwb2ludHM9IjQzMi41LDYwLjAgNDM2LjAsNzAuNiA0MzkuNSw4MC4wIDQ0My4wLDg4LjMgNDQ2LjUsOTUuOCA0NTAuMCwxMDIuNSA0NTMuNSwxMDguNiA0NTcuMCwxMTQuMSA0NjAuNSwxMTkuMSA0NjQuMCwxMjMuOCA0NjcuNSwxMjguMCA0NzEuMCwxMzEuOSA0NzQuNSwxMzUuNiA0NzguMCwxMzguOSA0ODEuNSwxNDIuMSA0ODUuMCwxNDUuMCA0ODguNSwxNDcuNyA0OTIuMCwxNTAuMyA0OTUuNSwxNTIuNyA0OTkuMCwxNTUuMCA1MDIuNSwxNTcuMSA1MDYuMCwxNTkuMiA1MDkuNSwxNjEuMSA1MTMuMCwxNjIuOSA1MTYuNSwxNjQuNiA1MjAuMCwxNjYuMiA1MjMuNSwxNjcuOCA1MjcuMCwxNjkuMyA1MzAuNSwxNzAuNyA1MzQuMCwxNzIuMCA1MzcuNSwxNzMuMyA1NDEuMCwxNzQuNiA1NDQuNSwxNzUuNyA1NDguMCwxNzYuOSA1NTEuNSwxNzguMCA1NTUuMCwxNzkuMCA1NTguNSwxODAuMCA1NjIuMCwxODEuMCA1NjUuNSwxODEuOSA1NjkuMCwxODIuOCA1NzIuNSwxODMuNiA1NzYuMCwxODQuNSA1NzkuNSwxODUuMyA1ODMuMCwxODYuMCA1ODYuNSwxODYuOCA1OTAuMCwxODcuNSA1OTMuNSwxODguMiA1OTcuMCwxODguOSA2MDAuNSwxODkuNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjZGMyNjI2IiBzdHJva2Utd2lkdGg9IjMuNSIvPjx0ZXh0IHg9IjM4MCIgeT0iMzYiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJzdGFydCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9ImJvbGQiPnRpZW1wbyBwYXJhIDEyMCBrbSAoaCk8L3RleHQ+PHRleHQgeD0iNDk1IiB5PSIyNjYiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSJib2xkIj52ZWxvY2lkYWQgKGttL2gpPC90ZXh0PjxjaXJjbGUgY3g9IjQzMi41IiBjeT0iNjAuMCIgcj0iNiIgZmlsbD0iI2RjMjYyNiIgc3Ryb2tlPSIjMzMzIiBzdHJva2Utd2lkdGg9IjEiLz48dGV4dCB4PSI0MzIuNSIgeT0iMjQ3IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEyIj4zMDwvdGV4dD48dGV4dCB4PSI0NDEuNSIgeT0iNTIuMCIgZmlsbD0iI2RjMjYyNiIgdGV4dC1hbmNob3I9InN0YXJ0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iYm9sZCI+KDMwOyA0KTwvdGV4dD48Y2lyY2xlIGN4PSI0ODUuMCIgY3k9IjE0NS4wIiByPSI2IiBmaWxsPSIjZGMyNjI2IiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMSIvPjx0ZXh0IHg9IjQ4NS4wIiB5PSIyNDciIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTIiPjYwPC90ZXh0Pjx0ZXh0IHg9IjQ5NC4wIiB5PSIxMzcuMCIgZmlsbD0iI2RjMjYyNiIgdGV4dC1hbmNob3I9InN0YXJ0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iYm9sZCI+KDYwOyAyKTwvdGV4dD48Y2lyY2xlIGN4PSI1OTAuMCIgY3k9IjE4Ny41IiByPSI2IiBmaWxsPSIjZGMyNjI2IiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMSIvPjx0ZXh0IHg9IjU5MC4wIiB5PSIyNDciIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTIiPjEyMDwvdGV4dD48dGV4dCB4PSI1OTkuMCIgeT0iMTc5LjUiIGZpbGw9IiNkYzI2MjYiIHRleHQtYW5jaG9yPSJzdGFydCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9ImJvbGQiPigxMjA7IDEpPC90ZXh0Pjx0ZXh0IHg9IjQ4NSIgeT0iMjg4IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIj5TaSBzZSBkdXBsaWNhIGxhIHZlbG9jaWRhZCAoMzAg4oaSIDYwKSw8L3RleHQ+PHRleHQgeD0iNDg1IiB5PSIzMDUiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiPmVsIHRpZW1wbyBzZSByZWR1Y2UgYSBsYSBtaXRhZCAoNCDihpIgMikuPC90ZXh0Pjwvc3ZnPg==)

*Figura 3. A la izquierda, una relación directamente proporcional: una recta. A la derecha, una relación inversamente proporcional: una curva que baja.*

### Relación directamente proporcional: van de la mano

Si una cantidad **se duplica**, la otra **también se duplica**. Si se triplica, la otra se triplica.

- **Cotidiano:** el precio de las manzanas y los kilos que compras. Si 2 kg cuestan 3 €, entonces 4 kg cuestan 6 €.
- **Físico:** a **más kilovoltaje** del tubo de rayos X, **más energía** tienen los fotones. Con un tubo de 80 kV, los fotones más energéticos llegan a 80 keV; con 120 kV, a 120 keV.

### Relación inversamente proporcional: enemigas íntimas

Si una cantidad **se duplica**, la otra **se reduce a la mitad**.

- **Cotidiano:** a más velocidad, menos tiempo para hacer el mismo viaje. Para recorrer 120 km: a 60 km/h tardas 2 horas; a 120 km/h, solo 1 hora.
- **Físico:** a **más frecuencia** tiene una onda, **menos longitud de onda** tiene. Con 100 MHz, la longitud de onda es de 3 m; con 200 MHz, de 1,5 m.

> **Cuidado con una trampa:** que una cantidad suba cuando la otra sube **no basta** para que sean directamente proporcionales. Por ejemplo, «a más horas de estudio, más nota» es cierto, pero **si estudias el doble no sacas el doble de nota**. Para que sea proporcional, **el doble tiene que dar el doble**.

### ¿Cómo lo reconozco?

| | **Directa** | **Inversa** |
|---|---|---|
| **Si una se duplica…** | La otra se duplica | La otra se reduce a la mitad |
| **La gráfica es…** | Una recta que sale del origen | Una curva que baja |
| **Se calcula con…** | Una división constante (precio por kilo) | Una multiplicación constante (distancia = velocidad · tiempo) |
| **Ejemplo** | kV y energía máxima de los fotones | Frecuencia y longitud de onda |

> **Para ir más allá: la ley del cuadrado inverso.** En protección radiológica es clave: si te alejas de una fuente de radiación **al doble de distancia**, la radiación que recibes no baja a la mitad, sino a **la cuarta parte**. Y al triple de distancia, a la novena parte. Por eso, **alejarse** es tan eficaz.

---

## 0.5. Despejar fórmulas: dejar la incógnita sola

Habrá momentos (pocos) en los que tendrás que calcular algo, como la longitud de una onda. Para eso hay que **despejar** la fórmula.

**Analogía:** una **balanza**. Si quitas algo de un platillo, tienes que quitar lo mismo del otro para que siga equilibrada.

La regla de oro es la de la balanza: **para pasar algo al otro lado del signo igual (=), tiene que pasar haciendo lo contrario**.

| Si está… | Pasa al otro lado… |
|---|---|
| **Sumando** (+) | **Restando** (−) |
| **Restando** (−) | **Sumando** (+) |
| **Multiplicando** (·) | **Dividiendo** (/) |
| **Dividiendo** (/) | **Multiplicando** (·) |

> **Dónde falla la analogía:** en una balanza real, quitas peso de verdad. En una fórmula, no «quitas» nada: haces la **misma operación en los dos lados** para que la igualdad se mantenga.

### Ejemplo práctico: la fórmula de las ondas

Sabemos que **v = λ · f** (velocidad = longitud de onda × frecuencia). Si queremos saber la longitud de onda (λ), la frecuencia (f) que la está multiplicando pasa al otro lado **dividiendo**:

> **λ = v / f**

![Triángulo de la fórmula v = λ · f](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NDAgMjg1IiBmb250LWZhbWlseT0iQXJpYWwsSGVsdmV0aWNhLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTUiPjxyZWN0IHdpZHRoPSI2NDAiIGhlaWdodD0iMjg1IiBmaWxsPSIjZmZmIi8+PGRlZnM+PG1hcmtlciBpZD0ibWIiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjMjU2M2ViIi8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibXIiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjZGMyNjI2Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWciIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjMTU4MDNkIi8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWsiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjNTU1NTU1Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibW8iIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjZWE1ODBjIi8+PC9tYXJrZXI+PC9kZWZzPjxwb2x5Z29uIHBvaW50cz0iMTcwLDQwIDQwLDIzMCAzMDAsMjMwIiBmaWxsPSIjZWZmNmZmIiBzdHJva2U9IiMyNTYzZWIiIHN0cm9rZS13aWR0aD0iMyIvPjxsaW5lIHgxPSIxMDUiIHkxPSIxMzUiIHgyPSIyMzUiIHkyPSIxMzUiIHN0cm9rZT0iIzI1NjNlYiIgc3Ryb2tlLXdpZHRoPSIzIi8+PGxpbmUgeDE9IjE3MCIgeTE9IjEzNSIgeDI9IjE3MCIgeTI9IjIzMCIgc3Ryb2tlPSIjMjU2M2ViIiBzdHJva2Utd2lkdGg9IjMiLz48dGV4dCB4PSIxNzAiIHk9IjExMiIgZmlsbD0iIzI1NjNlYiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIzNCIgZm9udC13ZWlnaHQ9ImJvbGQiPnY8L3RleHQ+PHRleHQgeD0iMTEyIiB5PSIyMDUiIGZpbGw9IiNlYTU4MGMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMzQiIGZvbnQtd2VpZ2h0PSJib2xkIj7OuzwvdGV4dD48dGV4dCB4PSIyMjgiIHk9IjIwNSIgZmlsbD0iI2RjMjYyNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIzNCIgZm9udC13ZWlnaHQ9ImJvbGQiPmY8L3RleHQ+PHRleHQgeD0iMTcwIiB5PSIyMiIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxNiIgZm9udC13ZWlnaHQ9ImJvbGQiPnYgPSDOuyDCtyBmPC90ZXh0Pjx0ZXh0IHg9IjM0MCIgeT0iNjAiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJzdGFydCIgZm9udC1zaXplPSIxNiIgZm9udC13ZWlnaHQ9ImJvbGQiPlRydWNvOiB0YXBhIGNvbiBlbCBkZWRvPC90ZXh0Pjx0ZXh0IHg9IjM0MCIgeT0iODAiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJzdGFydCIgZm9udC1zaXplPSIxNiIgZm9udC13ZWlnaHQ9ImJvbGQiPmxhIGxldHJhIHF1ZSBxdWllcmVzIGNhbGN1bGFyPC90ZXh0Pjx0ZXh0IHg9IjM0MCIgeT0iMTIwIiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ic3RhcnQiIGZvbnQtc2l6ZT0iMTUiPlRhcGFzIHY6ICAgcXVlZGEgzrsgwrcgZjwvdGV4dD48dGV4dCB4PSIzNDAiIHk9IjEyNiIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxNSI+PC90ZXh0Pjx0ZXh0IHg9IjM0MCIgeT0iMTUwIiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ic3RhcnQiIGZvbnQtc2l6ZT0iMTQiPuKGkiAgdiA9IM67IMK3IGYgIChzZSBtdWx0aXBsaWNhbik8L3RleHQ+PHRleHQgeD0iMzQwIiB5PSIxOTAiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJzdGFydCIgZm9udC1zaXplPSIxNSI+VGFwYXMgzrs6ICAgcXVlZGEgdiBzb2JyZSBmPC90ZXh0Pjx0ZXh0IHg9IjM0MCIgeT0iMjEwIiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0ic3RhcnQiIGZvbnQtc2l6ZT0iMTQiPuKGkiAgzrsgPSB2IC8gZjwvdGV4dD48dGV4dCB4PSIzNDAiIHk9IjI0NSIgZmlsbD0iIzIyMiIgdGV4dC1hbmNob3I9InN0YXJ0IiBmb250LXNpemU9IjE1Ij5UYXBhcyBmOiAgIHF1ZWRhIHYgc29icmUgzrs8L3RleHQ+PHRleHQgeD0iMzQwIiB5PSIyNjUiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJzdGFydCIgZm9udC1zaXplPSIxNCI+4oaSICBmID0gdiAvIM67PC90ZXh0Pjwvc3ZnPg==)

*Figura 4. El triángulo de la fórmula v = λ · f. Tapa la letra que buscas y lo que queda te dice cómo calcularla.*

### Receta para resolver un problema

1. **Escribe la fórmula.**
2. **Despeja** la incógnita (la letra que buscas).
3. **Sustituye** los números, **con sus unidades**.
4. **Calcula.**
5. **Comprueba** que el resultado tiene sentido y que la **unidad** es la correcta.

### Ejemplos resueltos

#### Ejemplo 1: la longitud de onda de un sonido

**Un sonido de 1 000 Hz viaja a 340 m/s. ¿Qué longitud de onda tiene?**

1. Fórmula: v = λ · f.
2. Despejamos: **λ = v / f**.
3. Sustituimos: λ = 340 / 1 000.
4. Calculamos: λ = **0,34 m**.

#### Ejemplo 2: la frecuencia de la luz verde

**La luz verde tiene una longitud de onda de 6 × 10⁻⁷ m. ¿Cuál es su frecuencia?** (La velocidad de la luz es 3 × 10⁸ m/s.)

1. Despejamos: **f = v / λ**.
2. Sustituimos: f = (3 × 10⁸) / (6 × 10⁻⁷).
3. 3 / 6 = 0,5 y 8 − (−7) = 15, es decir, 0,5 × 10¹⁵ = **5 × 10¹⁴ Hz**.

#### Ejemplo 3: ¿a qué distancia ha caído el rayo?

Después de ver un relámpago, el trueno tarda **3 segundos** en llegar. El sonido viaja a 340 m/s. **¿A qué distancia ha caído?**

1. Fórmula: distancia = velocidad · tiempo.
2. Sustituimos: d = 340 · 3 = **1 020 m** (algo más de 1 km).

(La luz llega casi al instante, así que su tiempo no cuenta.)

#### Comprobar las unidades

Las **unidades también se despejan**. En el ejemplo 1: λ = v / f → (m/s) / (1/s) = **m**. Como el hercio es 1/s, la unidad sale en metros, que es lo que esperábamos. Si te sale otra unidad, algo has hecho mal.

---

## 0.6. Fracciones, porcentajes y potencias sencillas

Cuando llegues a la **radiactividad** (Módulo 6) te encontrarás con «la mitad de la mitad». Aquí tienes lo necesario.

### Fracciones y porcentajes

| Fracción | Decimal | Porcentaje | En palabras |
|---|---|---|---|
| 1/2 | 0,5 | **50 %** | la mitad |
| 1/4 | 0,25 | **25 %** | la cuarta parte |
| 1/8 | 0,125 | **12,5 %** | la octava parte |
| 1/10 | 0,1 | **10 %** | la décima parte |
| 3/4 | 0,75 | **75 %** | tres cuartos |

**Calcular un porcentaje:** el 25 % de 80 es 80 × 0,25 = **20** (o también 80 / 4).

### Potencias: multiplicar un número por sí mismo

**Elevar a n** significa multiplicar el número por sí mismo **n veces**:

- 2³ = 2 × 2 × 2 = **8**.
- (1/2)³ = 1/2 × 1/2 × 1/2 = **1/8**.

Así, «la mitad de la mitad de la mitad» es (1/2)³ = 1/8 = 12,5 %.

---

## 0.7. Cómo leer una gráfica

Las gráficas resumen mucha información en un dibujo. Hay que fijarse en cuatro cosas.

![Temperatura de un paciente a lo largo de 12 horas](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MDAgMzIwIiBmb250LWZhbWlseT0iQXJpYWwsSGVsdmV0aWNhLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTUiPjxyZWN0IHdpZHRoPSI2MDAiIGhlaWdodD0iMzIwIiBmaWxsPSIjZmZmIi8+PGRlZnM+PG1hcmtlciBpZD0ibWIiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjMjU2M2ViIi8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibXIiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjZGMyNjI2Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWciIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjMTU4MDNkIi8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWsiIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjNTU1NTU1Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibW8iIG1hcmtlcldpZHRoPSI5IiBtYXJrZXJIZWlnaHQ9IjkiIHJlZlg9IjgiIHJlZlk9IjQuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTTAgMEw5IDQuNUwwIDl6IiBmaWxsPSIjZWE1ODBjIi8+PC9tYXJrZXI+PC9kZWZzPjxsaW5lIHgxPSI4MCIgeTE9IjI2MCIgeDI9IjU2MCIgeTI9IjI2MCIgc3Ryb2tlPSIjZTVlN2ViIiBzdHJva2Utd2lkdGg9IjEiLz48dGV4dCB4PSI3MCIgeT0iMjY1IiBmaWxsPSIjNTU1IiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjEzIj4zNjwvdGV4dD48bGluZSB4MT0iODAiIHkxPSIyMDUiIHgyPSI1NjAiIHkyPSIyMDUiIHN0cm9rZT0iI2U1ZTdlYiIgc3Ryb2tlLXdpZHRoPSIxIi8+PHRleHQgeD0iNzAiIHk9IjIxMCIgZmlsbD0iIzU1NSIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSIxMyI+Mzc8L3RleHQ+PGxpbmUgeDE9IjgwIiB5MT0iMTUwIiB4Mj0iNTYwIiB5Mj0iMTUwIiBzdHJva2U9IiNlNWU3ZWIiIHN0cm9rZS13aWR0aD0iMSIvPjx0ZXh0IHg9IjcwIiB5PSIxNTUiIGZpbGw9IiM1NTUiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iMTMiPjM4PC90ZXh0PjxsaW5lIHgxPSI4MCIgeTE9Ijk1IiB4Mj0iNTYwIiB5Mj0iOTUiIHN0cm9rZT0iI2U1ZTdlYiIgc3Ryb2tlLXdpZHRoPSIxIi8+PHRleHQgeD0iNzAiIHk9IjEwMCIgZmlsbD0iIzU1NSIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSIxMyI+Mzk8L3RleHQ+PGxpbmUgeDE9IjgwIiB5MT0iNDAiIHgyPSI1NjAiIHkyPSI0MCIgc3Ryb2tlPSIjZTVlN2ViIiBzdHJva2Utd2lkdGg9IjEiLz48dGV4dCB4PSI3MCIgeT0iNDUiIGZpbGw9IiM1NTUiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iMTMiPjQwPC90ZXh0PjxsaW5lIHgxPSI4MCIgeTE9IjI2MCIgeDI9IjU3MCIgeTI9IjI2MCIgc3Ryb2tlPSIjNTU1NTU1IiBzdHJva2Utd2lkdGg9IjIuNSIgbWFya2VyLWVuZD0idXJsKCNtaykiLz48bGluZSB4MT0iODAiIHkxPSIyNjAiIHgyPSI4MCIgeTI9IjI4IiBzdHJva2U9IiM1NTU1NTUiIHN0cm9rZS13aWR0aD0iMi41IiBtYXJrZXItZW5kPSJ1cmwoI21rKSIvPjx0ZXh0IHg9IjgwIiB5PSIyODAiIGZpbGw9IiM1NTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiPjA8L3RleHQ+PHRleHQgeD0iMTYwIiB5PSIyODAiIGZpbGw9IiM1NTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiPjI8L3RleHQ+PHRleHQgeD0iMjQwIiB5PSIyODAiIGZpbGw9IiM1NTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiPjQ8L3RleHQ+PHRleHQgeD0iMzIwIiB5PSIyODAiIGZpbGw9IiM1NTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiPjY8L3RleHQ+PHRleHQgeD0iNDAwIiB5PSIyODAiIGZpbGw9IiM1NTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiPjg8L3RleHQ+PHRleHQgeD0iNDgwIiB5PSIyODAiIGZpbGw9IiM1NTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiPjEwPC90ZXh0Pjx0ZXh0IHg9IjU2MCIgeT0iMjgwIiBmaWxsPSIjNTU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIj4xMjwvdGV4dD48cG9seWxpbmUgcG9pbnRzPSI4MCwyMTYgMTYwLDE3OCAyNDAsMTI4IDMyMCw5NSA0MDAsMTM5IDQ4MCwxODMgNTYwLDIwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMjU2M2ViIiBzdHJva2Utd2lkdGg9IjMuNSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPjxjaXJjbGUgY3g9IjgwIiBjeT0iMjE2IiByPSI1IiBmaWxsPSIjMjU2M2ViIiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMSIvPjxjaXJjbGUgY3g9IjE2MCIgY3k9IjE3OCIgcj0iNSIgZmlsbD0iIzI1NjNlYiIgc3Ryb2tlPSIjMzMzIiBzdHJva2Utd2lkdGg9IjEiLz48Y2lyY2xlIGN4PSIyNDAiIGN5PSIxMjgiIHI9IjUiIGZpbGw9IiMyNTYzZWIiIHN0cm9rZT0iIzMzMyIgc3Ryb2tlLXdpZHRoPSIxIi8+PGNpcmNsZSBjeD0iMzIwIiBjeT0iOTUiIHI9IjUiIGZpbGw9IiMyNTYzZWIiIHN0cm9rZT0iIzMzMyIgc3Ryb2tlLXdpZHRoPSIxIi8+PGNpcmNsZSBjeD0iNDAwIiBjeT0iMTM5IiByPSI1IiBmaWxsPSIjMjU2M2ViIiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMSIvPjxjaXJjbGUgY3g9IjQ4MCIgY3k9IjE4MyIgcj0iNSIgZmlsbD0iIzI1NjNlYiIgc3Ryb2tlPSIjMzMzIiBzdHJva2Utd2lkdGg9IjEiLz48Y2lyY2xlIGN4PSI1NjAiIGN5PSIyMDUiIHI9IjUiIGZpbGw9IiMyNTYzZWIiIHN0cm9rZT0iIzMzMyIgc3Ryb2tlLXdpZHRoPSIxIi8+PGxpbmUgeDE9IjMyMCIgeTE9Ijk1IiB4Mj0iODAiIHkyPSI5NSIgc3Ryb2tlPSIjZGMyNjI2IiBzdHJva2Utd2lkdGg9IjIuNSIgc3Ryb2tlLWRhc2hhcnJheT0iNiA0Ii8+PGxpbmUgeDE9IjMyMCIgeTE9Ijk1IiB4Mj0iMzIwIiB5Mj0iMjYwIiBzdHJva2U9IiNkYzI2MjYiIHN0cm9rZS13aWR0aD0iMi41IiBzdHJva2UtZGFzaGFycmF5PSI2IDQiLz48Y2lyY2xlIGN4PSIzMjAiIGN5PSI5NSIgcj0iOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjZGMyNjI2IiBzdHJva2Utd2lkdGg9IjEiLz48dGV4dCB4PSIzMzYiIHk9IjgzIiBmaWxsPSIjZGMyNjI2IiB0ZXh0LWFuY2hvcj0ic3RhcnQiIGZvbnQtc2l6ZT0iMTQiIGZvbnQtd2VpZ2h0PSJib2xkIj7ikaIgYSBsYXMgNiBoOiAzOSwwIMKwQzwvdGV4dD48dGV4dCB4PSI4NiIgeT0iMjIiIGZpbGw9IiMyMjIiIHRleHQtYW5jaG9yPSJzdGFydCIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9ImJvbGQiPuKRoCBlamUgdmVydGljYWw6IGxhIHRlbXBlcmF0dXJhICjCsEMpPC90ZXh0Pjx0ZXh0IHg9IjU2MCIgeT0iMzA2IiBmaWxsPSIjMjIyIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjE0IiBmb250LXdlaWdodD0iYm9sZCI+4pGhIGVqZSBob3Jpem9udGFsOiBlbCB0aWVtcG8gKGhvcmFzKTwvdGV4dD48L3N2Zz4=)

*Figura 5. Ejemplo: la temperatura de un paciente a lo largo de 12 horas.*

1. **① Eje vertical (y):** dice **qué se mide** y en qué unidad (aquí, la temperatura en °C).
2. **② Eje horizontal (x):** suele ser el **tiempo** o la variable que cambia (aquí, las horas).
3. **③ Cada punto:** es un **par de valores**. El punto marcado dice: «a las 6 h, el paciente tenía 39,0 °C».
4. **La forma de la curva:** si **sube**, el valor aumenta; si **baja**, disminuye. La temperatura sube hasta las 6 h y luego baja.

**Para leer un valor:** busca el punto en la curva y traza una línea **hasta el eje**. A las 8 h, la temperatura es de unos 38,2 °C.

> **En el hospital:** los espectros, las curvas de desintegración y los mapas de intensidad de los siguientes módulos se leen igual: **dos ejes, una curva, un punto**.

---

## Resumen del módulo

- Una **magnitud** es algo medible; la **unidad** es su «apellido». El **SI** usa metro, segundo, kilogramo, hercio, voltio, amperio…
- Los **prefijos** acortan los números: **k** (mil), **M** (millón), **G** (mil millones), **m** (milésima), **μ** (millonésima), **n** (milmillonésima). Cada escalón es ×1 000 o ÷1 000. **M** y **m** no son lo mismo.
- La **notación científica** escribe números enormes o diminutos como **número × 10ⁿ**. Exponente **positivo**: grande. Exponente **negativo**: diminuto.
- Al **multiplicar** potencias de 10 se **suman** los exponentes; al **dividir**, se **restan**.
- **Directamente proporcional:** si una se duplica, la otra también. **Inversamente proporcional:** si una se duplica, la otra se reduce a la mitad.
- Para **despejar**, lo que está de un lado pasa al otro haciendo **la operación contraria**. Comprueba siempre las unidades.
- La mitad = 1/2 = 50 %; la cuarta parte = 25 %; la octava parte = 12,5 %. **Elevar a n** es multiplicar n veces.
- En una **gráfica**, mira los ejes, los puntos y la forma de la curva.

## Glosario

| Término | Significado |
|---|---|
| **Magnitud** | Cualquier cosa que se puede medir. |
| **Unidad** | Patrón con el que se mide una magnitud. |
| **Sistema Internacional (SI)** | Acuerdo mundial sobre las unidades. |
| **Hercio (Hz)** | Unidad de frecuencia: una vez por segundo. |
| **Prefijo** | Letra que se pone delante de una unidad para indicar múltiplos o submúltiplos. |
| **Notación científica** | Forma de escribir un número como «número × 10ⁿ». |
| **Exponente** | Número pequeño colocado arriba a la derecha que indica cuántas veces se multiplica. |
| **Directamente proporcional** | Relación en la que, si una se duplica, la otra también. |
| **Inversamente proporcional** | Relación en la que, si una se duplica, la otra se reduce a la mitad. |
| **Incógnita** | Cantidad que se busca. |
| **Despejar** | Dejar la incógnita sola a un lado de la igualdad. |
| **Porcentaje** | Cantidad expresada como partes por cada 100. |
| **Eje** | Cada una de las dos rectas de una gráfica que indica una variable. |

---

## Ejercicios propuestos

1. Indica qué falta en la frase «el tubo funciona a 120» y completa con una unidad correcta.
2. Convierte: a) 2,5 kV a V; b) 150 mA a A; c) 400 nm a m (en notación científica); d) 0,5 mm a μm; e) 3 GHz a Hz.
3. Escribe en notación científica: a) 450 000; b) 0,0008; c) 6 200 000 000.
4. Escribe como número normal: a) 2,4 × 10³; b) 6 × 10⁻².
5. Calcula: a) (6 × 10⁸) / (2 × 10³); b) (2 × 10⁵) · (4 × 10²).
6. Indica si la relación es directa o inversa: a) kilovoltaje y energía máxima de los fotones; b) número de trabajadores y tiempo para hacer una tarea; c) kilos de manzanas y su precio; d) frecuencia y longitud de onda.
7. Una emisora emite a 50 MHz y otra a 100 MHz. ¿Cuál tiene mayor longitud de onda? Calcula las dos con λ = c / f (c = 3 × 10⁸ m/s).
8. Despeja la letra indicada: a) v = λ · f, despeja f; b) d = v · t, despeja t; c) c = λ · ν, despeja λ.
9. Un sonido de 500 Hz viaja a 340 m/s. ¿Cuál es su longitud de onda?
10. Calcula el 12,5 % de 80.
11. Calcula (1/2) · (1/2) · (1/2) · (1/2) y exprésalo en fracción y en porcentaje.
12. Mira la Figura 5: ¿a qué hora se alcanza la temperatura máxima y cuál es? ¿Qué temperatura hay a las 10 h?

## Soluciones

1. Falta la **unidad**. Por ejemplo: «el tubo funciona a **120 kV**».
2. a) 2,5 × 1 000 = **2 500 V**. b) 150 / 1 000 = **0,15 A**. c) 400 nm = 400 × 10⁻⁹ m = **4 × 10⁻⁷ m**. d) 0,5 × 1 000 = **500 μm**. e) 3 × 10⁹ = **3 000 000 000 Hz**.
3. a) **4,5 × 10⁵**. b) **8 × 10⁻⁴**. c) **6,2 × 10⁹**.
4. a) **2 400**. b) **0,06**.
5. a) 6 / 2 = 3 y 8 − 3 = 5: **3 × 10⁵**. b) 2 · 4 = 8 y 5 + 2 = 7: **8 × 10⁷**.
6. a) **Directa.** b) **Inversa** (a más trabajadores, menos tiempo). c) **Directa.** d) **Inversa.**
7. 50 MHz = 5 × 10⁷ Hz → λ = (3 × 10⁸) / (5 × 10⁷) = **6 m**. 100 MHz = 10⁸ Hz → λ = **3 m**. Tiene **mayor** longitud de onda la de **50 MHz**.
8. a) **f = v / λ**. b) **t = d / v**. c) **λ = c / ν**.
9. λ = v / f = 340 / 500 = **0,68 m**.
10. 80 · 0,125 = **10**.
11. 1/2 · 1/2 · 1/2 · 1/2 = **1/16** = 0,0625 = **6,25 %**.
12. La temperatura máxima es **39,0 °C** y se alcanza a las **6 horas**. A las 10 h la temperatura es de unos **37,4 °C**.

---

**Siguiente módulo:** ya tienes la caja de herramientas. En el **Módulo 1** empezamos con la física: de qué está hecha la materia y cómo es un átomo.
