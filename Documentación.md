## Customer Flight Analysis

### Loyalty Number

|    Tipo   |   Loyalty Number   |
|-----------|---------------|
| Top 5: |678205ㅤㅤ0.02%
||499874ㅤㅤ0.01%
||411734ㅤㅤ0.01%
||255475ㅤㅤ0.01%
||528447ㅤㅤ0.01%
|Bottom 5: |100590ㅤㅤ0.01%
||100642ㅤㅤ0.01%
||100644ㅤㅤ0.01%
||100646ㅤㅤ0.01%
||999891ㅤㅤ0.01%<br><br>Valores únicos: **16737**<br>Número de registros: **405624**<br>Valores nulos: **0**<br>Registros duplicados: **388887**|
---

El **identificador único** presenta duplicados, probablemente debido al número de vuelos realizados por el cliente.

        > El computo total de las frecuencias de vuelo por cliente registrado, nos arroja un gran número de clientes habituales que sostienen el grueso de los vuelos.

| #clientes | #vuelos|
|----------|--------|
|   24 | 16574 |
| 48 | 162 |
| 72 | 1 |
---
     
       

Ir a [customer loyalty](#customer-loyalty-history) para comparar con la columna de Identificación única de clientes.

---
---

### Year

|    dtype: int64  |   Flight activity per year   |
|-----------|---------------|
||2017ㅤㅤ50.0
||2018ㅤㅤ50.0<br><br>Valores únicos: **2**<br>Número de registros: **405624**<br>Valores nulos: **0**|
---
ㅤㅤ   
- Registrados 405624 actividades de vuelto en total entre los años 2017 y 2018.

---
---

### Month

|    dtype: int64  |   Flight activity per months   |
|-----------|---------------|
||1ㅤㅤ8.33
||9ㅤㅤ8.33
||2ㅤㅤ8.33
||3ㅤㅤ8.33
||11ㅤㅤ8.33
||4ㅤㅤ8.33
||5ㅤㅤ8.33
||7ㅤㅤ8.33
||6ㅤㅤ8.33
||8ㅤㅤ8.33
||10ㅤㅤ8.33
||12ㅤㅤ8.33<br><br>Valores únicos: **12**<br>Número de registros: **405624**<br>Valores nulos: **0**|
---

    > La aerolínea presenta un patrón regular en la actividad de sus vuelos.

---
---

### Flights booked

|    dtype: int64  |   Flights Booked   |
|-----------|---------------|
||0ㅤㅤ48.81
||3ㅤㅤ4.49
||11ㅤㅤ3.87
||5ㅤㅤ3.72
||7ㅤㅤ3.59
||8ㅤㅤ3.54
||9ㅤㅤ3.49
||6ㅤㅤ3.41
||2ㅤㅤ3.36
||10ㅤㅤ3.29
||4ㅤㅤ3.16
||1ㅤㅤ3.12
||13ㅤㅤ2.66
||12ㅤㅤ2.56
||14ㅤㅤ1.74
||15ㅤㅤ1.62
||16ㅤㅤ1.07
||17ㅤㅤ0.96
||18ㅤㅤ0.73
||19ㅤㅤ0.37
||20ㅤㅤ0.28
||21ㅤㅤ0.13<br><br>Valores únicos: **22**<br>Número de registros: **405624**<br>Valores nulos: **0**|
---

    > No queda muy claro a qué mes se refiere el epígrafe que describre la columna. Habrá que cruzar información con otras celdas.

---
---

### Flights with Companions

|    dtype: int64  |   Flights booked with Companions   |
|-----------|---------------|
||0ㅤㅤ73.19
||2ㅤㅤ4.75
||3ㅤㅤ4.69
||1ㅤㅤ4.41
||4ㅤㅤ3.37
||5ㅤㅤ3.31
||6ㅤㅤ2.44
||7ㅤㅤ1.75
||8ㅤㅤ0.98
||9ㅤㅤ0.73
||10ㅤㅤ0.26
||11ㅤㅤ0.12<br><br>Valores únicos: **12**<br>Número de registros: **405624**<br>Valores nulos: **0**<br>Registros duplicados: **405612**|
---

    > Una mayoría reservó sus vueltos sin acompañante.


---
---

### Total Flights

|    dtype: int64  |   Total Flights   |
|-----------|---------------|
||Top 5:
||0ㅤㅤ48.81%
||6ㅤㅤ3.77%
||10ㅤㅤ3.55%
||8ㅤㅤ3.47%
||4ㅤㅤ3.37%
||Bottom 5:
||28ㅤㅤ0.08%
||29ㅤㅤ0.05%
||30ㅤㅤ0.04%
||31ㅤㅤ0.02%
||32ㅤㅤ0.01%<br><br>Valores únicos: **33**<br>Número de registros: **405624**<br>Valores nulos: **0**<br>Registros duplicados: **405591**|
---

    > Casi la mitad de la base de clientes no reservó vuelo alguno.

---
---

### Distance

|    dtype: int64  |   Total distance per month  |
|-----------|---------------|
||Top 5:
||0ㅤㅤㅤ 48.81%
||2520ㅤㅤ0.1%
||2880ㅤㅤ0.1%
||1680ㅤㅤ0.1%
||2160ㅤㅤ0.09%
||Bottom 5:
||2963ㅤㅤ0.0%
||4997ㅤㅤ0.0%
||947 ㅤㅤ 0.0%
||3187ㅤㅤ0.0%
||671 ㅤㅤ 0.0%<br><br>Valores únicos: **4746**<br>Número de registros: **405624**<br>Valores nulos: **0**<br>Registros duplicados: **400878**|
---

Contaremos para la observación sólo con la base de clientes que sí realizó vuelos.

    > Representando el valor central real de las cifras, la mediana de vuelo es de 2298 km.

---
---

### Points Accumulated

|    dtype: float64  |   Points Accumulated per Distance & Other  |
|-----------|---------------|
||Top 5:
||0.0ㅤㅤㅤㅤ48.81%
||180.0 ㅤㅤㅤ 0.19%
||270.0 ㅤㅤㅤ 0.18%
||288.0 ㅤㅤㅤ 0.18%
||189.0 ㅤㅤㅤ 0.17%
||Bottom 5:
||649.5 ㅤㅤㅤ 0.0%
||471.96 ㅤㅤㅤ0.0%
||565.5 ㅤㅤㅤ 0.0%
||474.12 ㅤㅤㅤ0.0%
||556.25 ㅤㅤㅤ0.0%<br><br>Valores únicos: **1549**<br>Número de registros: **405624**<br>Valores nulos: **0**|
---

    > La mediana de puntos acumulados es 235.

---
---

### Points Redeemed

|    dtype: int64  |   Points Redeemed   |
|-----------|---------------|
||Top 5:
||0 ㅤ ㅤ  94.04%
||447ㅤㅤ0.03%
||523ㅤㅤ0.02%
||443ㅤㅤ0.02%
||516ㅤㅤ0.02%
||Bottom 5:
||858ㅤㅤ0.0%
||869ㅤㅤ0.0%
||834ㅤㅤ0.0%
||859ㅤㅤ0.0%
||862ㅤㅤ0.0%<br><br>Valores únicos: **587**<br>Número de registros: **405624**<br>Valores nulos: **0**<br>Registros duplicados: **405037**|
---

    > Una gran mayoría (94.04%) no ha redimido sus puntos de viaje.

    > El número de clientes que usa sus puntos es 11560 de una base con 16737 clientes registrados.

[Ir a visualización](#programa-de-fidelización-y-puntos)

---
---

### Dollar Cost Points Redeemed

*Valor en dólares de los puntos que el cliente ha redimido*

|    dtype: int64  |   Dollar Cost Points Redeemed   |
|-----------|---------------|
||Top 5:
||0ㅤㅤ94.04%
||36ㅤㅤ0.26%
||38ㅤㅤ0.25%
||40ㅤㅤ0.24%
||42ㅤㅤ0.24%
||Bottom 5:
||68ㅤㅤ0.02%
||67ㅤㅤ0.02%
||70ㅤㅤ0.01%
||69ㅤㅤ0.01%
||71ㅤㅤ0.0%<br><br>Valores únicos: **49**<br>Número de registros: **405624**<br>Valores nulos: **0**<br>Registros duplicados: **405575**|
---
ㅤㅤ    

    > La mayoría de las liquidaciones de puntos no tienen un valor en dólares asociado (el 94.04% está relacionado con 0$).

    > Sólo un pequeño porcentaje de liquidaciones tiene un valor monetario asociado (5.96%).

Puede deberse a:

    > Los puntos se redimen por servicios que no tienen un valor monetario directo.
    > Los clientes no están intercambiando puntos por servicios con valor monetario.

---
---

# Customer Loyalty History


### Loyalty Number

|    dtype: int64  |   Loyalty Number   |
|-----------|---------------|
||Top 5: <br>480934ㅤㅤ0.01%
||549612ㅤㅤ0.01%
||429460ㅤㅤ0.01%
||608370ㅤㅤ0.01%
||530508ㅤㅤ0.01%
||Bottom 5:
||823768ㅤㅤ0.01%
||680886ㅤㅤ0.01%
||776187ㅤㅤ0.01%
||906428ㅤㅤ0.01%
||652627ㅤㅤ0.01%<br><br>Valores únicos: **16737**<br>Número de registros: **16737**<br>Valores nulos: **0**<br>Registros duplicados: **0**|
---


---

### Country

*País de residencia del cliente.*

|    dtype: object  |   Country   |
|-----------|---------------|
||Canadaㅤㅤ100.0<br><br>Valores únicos: **1**<br>Número de registros: **16737**<br>Valores nulos: **0**<br>Registros duplicados: **16736**|
---

Los datos provienen de operativa de vuelos para residentes en Canadá, dado que utilizan el sistema métrico para las distancias, daremos por hecho que éstas usan *Km*.

---
---

### Province

*Provincia o estado de residencia del cliente.*

|    dtype: object  |   Province   |
|-----------|--------------|
||Ontarioㅤㅤㅤㅤㅤㅤ32.29
||British Columbiaㅤㅤ 26.34
||Quebecㅤㅤㅤㅤㅤㅤ19.72
||Alberta ㅤ ㅤㅤㅤㅤㅤ 5.79
||Manitoba ㅤㅤㅤㅤ ㅤ 3.93
||New Brunswickㅤㅤ ㅤ 3.8
||Nova Scotiaㅤㅤㅤㅤㅤ3.09
||Saskatchewanㅤㅤㅤㅤ 2.44
||Newfoundlandㅤㅤㅤㅤ1.54
||Yukonㅤㅤㅤㅤㅤㅤㅤㅤ0.66
||Prince Edward Island ㅤ  0.39<br><br>Valores únicos: **11**<br>Número de registros: **16737**<br>Valores nulos: **0**<br>Registros duplicados: **16726**|
---
ㅤ  
La operativa gestiona vuelos entre 11 provincias.

---
---

### City

*Ciudad de residencia del cliente.*

|    dtype: object  |   City   |
|-----------|---------------|
||Top 5:
||Torontoㅤㅤㅤ 20.02%
||Vancouverㅤㅤ 15.43% 
||Montreal ㅤ ㅤ  12.3%
||Winnipegㅤㅤㅤ3.93%
||Whistlerㅤㅤ ㅤ 3.48%
||Bottom 5:
||Londonㅤ ㅤ ㅤ 1.04%
||Peace River ㅤㅤ0.68%
||Whitehorseㅤㅤ 0.66%
||Kelowna ㅤㅤㅤ  0.53%
||Charlottetownㅤ0.39%<br><br>Valores únicos: **29**<br>Número de registros: **16737**<br>Valores nulos: **0**<br>Registros duplicados: **16708**|
---
---

### Postal Code

*Código postal del cliente.*

|    dtype: object  |   Postal Code   |
|-----------|---------------|
||Top 5:
||V6E 3D9ㅤㅤ5.44%
||V5R 1W3 ㅤ 4.09%
||V6T 1Y8ㅤㅤ3.48%
||V6E 3Z3ㅤㅤ3.25%
||M2M 7K8ㅤ 3.19%
||Bottom 5:
||H3T 8L4ㅤㅤ0.53%
||V09 2E9ㅤㅤ0.53%
||C1A 6E8ㅤㅤ0.39%
||H3J 5I6 ㅤㅤ 0.04%
||M3R 4K8ㅤㅤ0.02%<br><br>Valores únicos: **55**<br>Número de registros: **16737**<br>Valores nulos: **0**<br>Registros duplicados: **16682**|
---

Observamos que los clientes se ubican en 29 ciudades, con 55 diferentes códigos postales.

---
---

### Gender

*Género del cliente*

|    dtype: object  |   Gender   |
|-----------|---------------|
||Femaleㅤㅤ50.25
||Maleㅤㅤㅤ49.75<br><br>Valores únicos: **2**<br>Número de registros: **16737**<br>Valores nulos: **0**|
---

---


### Education

*Nivel educativo alcanzado por el cliente (ej. Bachelor para licenciatura, College para estudios universitarios o técnicos, etc.).*

|    dtype: object  |   Education   |
|-----------|---------------|
||Bachelor ㅤㅤㅤㅤ ㅤㅤㅤ 62.59
||Collegeㅤㅤㅤㅤㅤ ㅤㅤㅤ25.32
||High School or Belowㅤ ㅤ 4.67
||Doctorㅤㅤㅤㅤㅤㅤㅤㅤㅤ4.39
||Masterㅤㅤㅤㅤㅤㅤㅤㅤㅤ3.04<br><br>Valores únicos: **5**<br>Número de registros: **16737**<br>Valores nulos: **0**|
---

El grueso de los clientes se encuentra entre la población con estudios superiores universitarios, pero no especializados mediante maestrías o doctorados.

[Ir a visualización](#nivel-educativo)

**Propuesta de mejora**:

- La diferencia en el mundo anglosajón entre Bachelor y College es tan ínfima, que podríamos unificarlo y sugerirlo a la empresa de cara a su registro de datos futuros. Ventajas: descarta el espejismo de fragmentación poblacional en el sistema que no es tal.

        Por ejemplo:
            
            University studies      87.9%
            High School or Below     4.67%
            Doctor                   4.39%
            Master                   3.04%

                        frente a

            Bachelor                 62.59%
            College                  25.32%
            High School or Below      4.67%
            Doctor                    4.39%
            Master                    3.04          


---
---

### Salary

*Ingreso anual estimado del cliente.*

|    dtype: floatㅤㅤ64  |   Salary   |
|-----------|---------------|
||Top 5:
||NaNㅤㅤㅤㅤ25.32%
||101933.0ㅤ ㅤ 0.14%
||51573.0ㅤㅤㅤ 0.08%
||61809.0ㅤㅤㅤ 0.08%
||62283.0ㅤㅤㅤ 0.08%
||Bottom 5:
||59314.0ㅤㅤㅤ  0.01%
||104138.0 ㅤ ㅤ 0.01%
||73400.0 ㅤㅤㅤ  0.01%
||65798.0 ㅤㅤㅤ 0.01%
||30767.0 ㅤㅤㅤ 0.01%<br><br>Valores únicos: **5890**<br>Número de registros: **16737**<br>Valores nulos: **4238**<br>Registros duplicados: **10847**|
---

Hay un 25% de estimación de ingreso desconocida.

---
---

### Marital Status

*Estado civil del cliente*

|    dtype: object  |   Marital Status   |
|-----------|---------------|
||Marriedㅤㅤ 58.16
||Singleㅤㅤㅤ26.79
||Divorcedㅤㅤ15.04<br><br>Valores únicos: **3**<br>Número de registros: **16737**<br>Valores nulos: **0**|
---

---

### Loyalty Card

*Tipo de tarjeta de lealtad que posee el cliente. Esto podría indicar distintos niveles o categorías dentro del programa de lealtad.*

|    dtype: object  |   Loyalty Card   |
|-----------|---------------|
||Starㅤㅤ45.63
||Novaㅤㅤ33.88
||Auroraㅤㅤ20.49<br><br>Valores únicos: **3**<br>Número de registros: **16737**<br>Valores nulos: **0**|
---

---

### CLV (Customer Lifetime Value)

*Valor total estimado (beneficio) que el cliente aporta a la empresa durante toda la relación que mantiene con ella.*

|    dtype: float64  |   CLV   |
|-----------|---------------|
||Top 5:
||8564.77ㅤㅤ0.08%
||7582.11ㅤㅤ0.07%
||5380.9 ㅤㅤ 0.07%
||10972.07 ㅤ  0.07%
||5332.46ㅤㅤ 0.07%
||Bottom 5:
||37939.49ㅤㅤ0.01%
||36168.34ㅤㅤ0.01%
||33288.16ㅤㅤ0.01%
||31864.86ㅤㅤ0.01%
||31758.35ㅤㅤ0.01%<br><br>Valores únicos: **7984**<br>Número de registros: **16737**<br>Valores nulos: **0**<br>Registros duplicados: **8753**|
---

    > La mediana del beneficio total estimado por cliente sería 5780.18$

    > Por otro lado, la media estimada tiende al alza: 7988,89$.
      
Esta disparidad nos indica:

- Hay clientes cuyo beneficio estimado diverge tan por encima de la media que desvirtúan la estimación.
- El grueso de la base de clientes es más modesta en estimación de beneficio pero con una media robusta en cantidad.

Ir a visualización.

---
---

### Enrollment Type

*Tipo de inscripción del cliente en el programa de lealtad.*
ㅤㅤ
|    dtype: object  |   Enrollment Type   |
|-----------|---------------|
||Standardㅤㅤㅤㅤㅤ94.2
||2018 Promotion ㅤㅤ 5.8<br><br>Valores únicos: **2**<br>Número de registros: **16737**<br>Valores nulos: **0**|
---

---


### Enrollment Year

*Año en que el cliente se inscribió en el programa de lealtad.*

|    dtype: int64  |   Enrollment Year   |
|-----------|---------------|
||2018ㅤㅤ17.98
||2017ㅤㅤ14.86
||2016ㅤㅤ14.67
||2013ㅤㅤ14.32
||2014ㅤㅤ14.16
||2015ㅤㅤ13.93
||2012ㅤㅤ10.07<br><br>Valores únicos: **7**<br>Número de registros: **16737**<br>Valores nulos: **0**|
---

Ir a visualización.

---
---

### Enrollment Month

*Mes en que el cliente se inscribió en el programa de lealtad.*

|    dtype: int64  |   Enrollment Month   |
|-----------|---------------|
||5ㅤㅤ8.98
||12 ㅤ 8.84
||7ㅤㅤ8.8
||11 ㅤ 8.64
||10 ㅤ 8.63
||8ㅤㅤ8.54
||6ㅤㅤ8.44
||9ㅤㅤ8.31
||4ㅤㅤ8.29
||3ㅤㅤ8.11
||2ㅤㅤ7.29
||1ㅤㅤ7.12<br><br>Valores únicos: **12**<br>Número de registros: **16737**<br>Valores nulos: **0**<br>|
---

No se aprecia significativamente una tendencia diferencial entre meses, salvo por los dos primeros meses de mes que no parece que favorezcan la adhesión.

Ir a visualización.

---
---

### Cancellation Year

*Año en que el cliente canceló su membresía en el programa de lealtad, si aplica.*

|    dtype: float64  |   Cancellation Year   |
|-----------|---------------|
||NaN ㅤㅤ 87.65
||2018.0ㅤㅤ3.85
||2017.0ㅤㅤ3.02
||2016.0ㅤㅤ2.55
||2015.0ㅤㅤ1.58
||2014.0ㅤㅤ1.08
||2013.0ㅤㅤ0.26<br><br>Valores únicos: **6**<br>Número de registros: **16737**<br>Valores nulos: **14670**|
---

En ausencia de un dato afirmativo, parece indicar que la falta de datos implica la cifra de clientes que siguen adheridos al programa de lealtad.

No obstante, la cancelación parece una tendencia creciente.


---
---

### Cancellation Month

*Mes en que el cliente canceló su membresía en el programa de lealtad, si aplica.*

|    dtype: float64  |   Cancellation Month   |
|-----------|---------------|
||NaNㅤㅤ 87.65
||12.0ㅤㅤㅤ1.27
||11.0ㅤㅤㅤ1.27
||8.0 ㅤㅤㅤ 1.24
||7.0 ㅤㅤㅤ 1.11
||10.0ㅤㅤㅤ1.08
||9.0 ㅤㅤㅤ 1.05
||6.0 ㅤㅤㅤ 0.99
||1.0 ㅤㅤㅤ 0.93
||3.0 ㅤㅤㅤ 0.89
||5.0 ㅤㅤㅤ 0.88
||2.0 ㅤㅤㅤ 0.83
||4.0 ㅤㅤㅤ 0.81<br><br>Valores únicos: **12**<br>Número de registros: **16737**<br>Valores nulos: **14670**|
---

Los registros nulos en el campo asociado al mes, son la misma cantidad que en el campo asociado al año.

Por lo que podemos afirmar:

    > El 87.65% de los miembros que se han registrado en el programa de fidelidad, mantienen su membresía activa a día de hoy.

---
---
ㅤ  
# Visualización de datos

### Programa de fidelización y puntos

<figure>
    <img src='img/v1.png '
         alt="Uso de puntos del programa de fidelidad"
         width="336" height="340">
    <figcaption>El uso de los puntos del programa de fidelidad muestra un mayor número de clientes que los han usado.</figcaption>
</figure>

---

### Nivel Educativo

<figure>
<img src='img/v2.png '
         alt="Nivel educativo de los clientes"
         width="336" height="340">
    <figcaption>El registro mayoritario de clientes se encuentra entre la población con estudios universitarios de Licenciaturas y Grados: equivale a un 87.9% </figcaption>
</figure>

---

### Distribución del CLV

<figure>
<img src='img/v3.png '
         alt="Nivel educativo de los clientes"
         width="700" height="400">
    <figcaption>El grueso de la mayor parte de beneficios por cliente es modesto, pero más sustancial en cantidad que los 'outliers', o casos excepcionales, cuyo beneficio estimado es mayor.</figcaption>
</figure>