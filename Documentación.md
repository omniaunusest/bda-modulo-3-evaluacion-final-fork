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

Sin anomalías.

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
<center><img src="visual/visual1.png" width="236" height="258"></center>




---
---

### Dollar Cost Points Redeemed

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
||652627ㅤㅤ0.01%<br><br>Valores únicos: **16737**<br>Número de registros: **16737**<br>Valores nulos: **0**<br>Registros duplicados: **0**

---
---

### Country

|    dtype: object  |   Country   |
|-----------|---------------|
||Canadaㅤㅤ100.0<br><br>Valores únicos: **1**<br>Número de registros: **16737**<br>Valores nulos: **0**<br>Registros duplicados: **16736**|
---

    > 

---
---

### Province

    >

### City

    >

### Postal Code

    >

### Gender

    >

### Education

    >

### Salary

    >

### Marital Status

    >

### Loyalty Card

### CLV (Customer Lifetime Value)

### Enrollment Type

### Enrollment Year

### Enrollment Month

### Cancelation Year

### Cancelation Month