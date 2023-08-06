# PyLibSuitETECSA

## Una librería escrita en Python para SuitETECSA

PyLibSuitETECSA es una API que interactúa con los servicios ofrecidos
por [ETECSA](https://www.etecsa.cu/), para facilitar el desarrollo de aplicaciones
Python dedicadas a la gestión de estos mediante los portales
[de usuario](https://www.portal.nauta.cu/) y [cautivo](https://secure.etecsa.net:8443/)
de nauta, ahorrándoles tiempo, esfuerzos y código a los desarrolladores.

Hasta el momento PyLibSuitETECSA implementa funciones para:

* En el caso del portal [de usuario](https://www.portal.nauta.cu/) de nauta:
  * Iniciar sesión.
  * Obtener información de la cuenta logueada.
  * Recargar la cuenta logueada.
  * Transferir saldo a otra cuenta nauta.
  * Transferir saldo para pago de cuota (`solo para cuentas Nauta Hogar`).
  * Cambiar la contraseña de la cuenta de acceso.
  * Cambiar la contraseña de la cuenta de correo asociada.
  * Obtener las conexiones realizadas en el periódo `año-mes` especificado.
  * Obtener las recargas realizadas en el periódo `año-mes` especificado.
  * Obtener las transferencias realizadas en el periódo `año-mes` especificado.
  * Obtener los pagos de cuotas realizados en el periódo `año-mes` especificado (`solo para cuentas Nauta Hogar`).
  * Obtener las útimas (`la cantidad puede ser definida por el desarrollador que use la librería; por defecto es 5`) operaciones (`las antes mencionadas`).
* En el caso del portal [cautivo](https://secure.etecsa.net:8443/) de nauta:
  * Inicia sesión.
  * Cierra sesión.
  * Obtiene el tiempo disponible en la cuenta.
  * Obtiene el saldo de la cuenta.

## Interactuar con el portal [de usuario](https://www.portal.nauta.cu/) de nauta

Para interactuar con el portal [de usuario](https://www.portal.nauta.cu/) de nauta
PyLibSuitETECSA proporciona dos clases; la más sencilla de usar es [UserPortalClient](#usando-userportalclient) ubicada en PyLibSuitETECSA.api y es la que se recomienda para
la mayoria de apps. Igualmente PyLibSuitETECSA proporciona la clase [UserPortal](#usando-userportal)
ubicada en PyLibSuitETECSA.core.protocol, un protocolo que permite a los desarrolladores
tener "más control" a la hora de interactuar con el portal.

### **Usando UserPortalClient**

Ejercicio donde:

* Iniciamos sesión en el portal.
* Tratamos de recargar la cuenta.
* Tratamos de transferir saldo a otra cuenta.
* Obtenemos las últimas 5 connexiones de la cuenta y las imprimimos en pantalla.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyLibSuitETECSA.api import UserPortalClient
from PyLibSuitETECSA.core.exception import RechargeException,\
    TransferException
from PyLibSuitETECSA.utils import Action

user_portal_cli = UserPortalClient(
    "user.name@nauta.com.cu",   # Cambiar por una cuenta real
    "password"                  # Cambiar por la contraseña de la cuenta
)

# Crea una sesión que se almacena en la variable
# user_portal_cli.session
user_portal_cli.init_session()

# Obtiene la imagen captcha del portal y la guarda
# en un archivo llamado 'captcha.png'
with open('captcha.png', 'wb') as fp:
    fp.write(
        user_portal_cli.captcha_as_bytes
    )

# Loguea la cuenta en el portal
user_portal_cli.login(
    input('captcha code: ')
)

# Trata de recargar la cuenta y en caso de error
# lo imprime en pantalla
try:
    user_portal_cli.recharge(
        "1234567890123456"
    )
except RechargeException as ex:
    print(f'Error al recargar :: {ex.args[0]}')

# Trata de transferir saldo a otra cuenta y en caso
# de errores los inprime en pantalla
try:
    user_portal_cli.transfer(
        250.25,
        "user.name@nauta.co.cu"
    )
except TransferException as ex:
    print(f'Error al transferir :: {ex.args[0]}')

# Obtiene las últimas 5 conexiones realizadas por la cuenta
# y las imprime en pantalla en formato json
connections = user_portal_cli.get_lasts(
    Action.GET_CONNECTIONS
)
for connection in connections:
    print(connection.__dict__)

```

Salida:

```console
captcha code: DCYTHZ
Error al recargar :: El código de recarga es incorrecto.
Error al transferir :: ['El campo saldo a transferir debe ser menor o igual que 14761']
{'start_session': datetime.datetime(2023, 1, 22, 22, 19, 11), 'end_session': datetime.datetime(2023, 1, 22, 22, 24, 8), 'duration': 297, 'uploaded': 275456, 'downloaded': 1782579, 'import_': 0.99}
{'start_session': datetime.datetime(2023, 1, 22, 11, 26, 8), 'end_session': datetime.datetime(2023, 1, 22, 14, 28, 13), 'duration': 10925, 'uploaded': 17637048, 'downloaded': 244454522, 'import_': 36.42}
{'start_session': datetime.datetime(2023, 1, 21, 16, 53, 29), 'end_session': datetime.datetime(2023, 1, 22, 1, 36, 8), 'duration': 31359, 'uploaded': 152746065, 'downloaded': 2168958484, 'import_': 104.53}
{'start_session': datetime.datetime(2023, 1, 20, 18, 19, 56), 'end_session': datetime.datetime(2023, 1, 20, 18, 25, 16), 'duration': 320, 'uploaded': 447488, 'downloaded': 8409579, 'import_': 1.07}
{'start_session': datetime.datetime(2023, 1, 20, 17, 29, 40), 'end_session': datetime.datetime(2023, 1, 20, 18, 12, 5), 'duration': 2545, 'uploaded': 7140802, 'downloaded': 113592238, 'import_': 8.49}
```

## Métodos y propiedades de UserPortalClient

### Métodos

<details>
    <summary>Nauta</summary>
    <table>
        <thead>
            <tr>
                <td>Método</td>
                <td>Función</td>
            </tr>
        </thead>
        <tr>
            <td>init_session</td>
            <td>Crea la sesión donde se guardan las cookies y datos</td>
        </tr>
        <tr>
            <td>login</td>
            <td>Loguea al usuario en el portal y carga la información de la cuenta</td>
        </tr>
        <tr>
            <td>recharge</td>
            <td>Recarga la cuenta logueada</td>
        </tr>
        <tr>
            <td>transfer</td>
            <td>Transfiere saldo a otra cuenta nauta</td>
        </tr>
        <tr>
            <td>change_password</td>
            <td>Cambia la contraseña de la cuenta logueada</td>
        </tr>
        <tr>
            <td>change_email_password</td>
            <td>Cambia la contraseña de la cuenta de correo asociada a la cuenta logueada</td>
        </tr>
        <tr>
            <td>get_lasts</td>
            <td>Devuelve las últimas <b>large</b> <b>action</b> realizadas, donde <b>large</b> es la cantidad Ex: 5 y <b>action</b> las operaciones realizadas Ex: <b>UserPortal.ACTION_CONNECTIONS</b> (las <b>action</b> disponibles son: <b>UserPortal.ACTION_CONNECTIONS</b>, <b>UserPortal.ACTION_RECHARGES</b>, <b>UserPortal.ACTION_TRANSFER</b> y <b>UserPortal.ACTION_QUOTE_FUNDS</b>, esta última solo para nauta hogar)</td>
        </tr>
        <tr>
            <td>get_connections</td>
            <td>Devuelve las conexiones realizadas en el mes especificado incluyendo el año (<b>año-mes</b>: 2022-03)</td>
        </tr>
        <tr>
            <td>get_recharges</td>
            <td>Devuelve las recargas realizadas en el mes especificado incluyendo el año (<b>año-mes</b>: 2022-03)</td>
        </tr>
        <tr>
            <td>get_transfers</td>
            <td>Devuelve las transferencias realizadas en el mes especificado incluyendo el año (<b>año-mes</b>: 2022-03)</td>
        </tr>
    </table>
</details>

<details>
    <summary>Nauta Hogar</summary>
    <table>
        <thead>
            <tr>
                <td>Método</td>
                <td>Función</td>
            </tr>
        </thead>
    <tr>
        <td>pay_nauta_home</td>
        <td>Transfiere saldo a la cuota de nauta hogar.</td>
    </tr>
    <tr>
        <td>get_quotes_fund</td>
        <td>Devuelve los fondos de cuota realizados en el mes especificado incluyendo el año (<b>año-mes</b>: 2022-03)</td>
    </tr>
    </table>
</details>

### Propiedades

<details>
    <summary>Nauta</summary>
    <table>
        <thead>
            <tr>
                <td>Propiedad</td>
                <td>Dato devuelto</td>
            </tr>
        </thead>
        <tr>
            <td>captcha_as_bytes</td>
            <td>Imagen captcha en bytes.</td>
        </tr>
        <tr>
            <td>blocking_date</td>
            <td>Fecha de bloqueo.</td>
        </tr>
        <tr>
            <td>date_of_elimination</td>
            <td>Fecha de eliminación.</td>
        </tr>
        <tr>
            <td>account_type</td>
            <td>Tipo de cuenta.</td>
        </tr>
        <tr>
            <td>service_type</td>
            <td>Tipo de servicio.</td>
        </tr>
        <tr>
            <td>credit</td>
            <td>Saldo.</td>
        </tr>
        <tr>
            <td>time</td>
            <td>Tiempo disponible.</td>
        </tr>
        <tr>
            <td>mail_account</td>
            <td>Cuenta de correo asociada.</td>
        </tr>
    </table>
</details>

<details>
    <summary>Nauta Hogar</summary>
    <table>
        <thead>
            <tr>
                <td>Propiedad</td>
                <td>Dato devuelto</td>
            </tr>
        </thead>
        <tr>
            <td>offer</td>
            <td>Oferta</td>
        </tr>
        <tr>
            <td>monthly_fee</td>
            <td>Cuota mensual</td>
        </tr>
        <tr>
            <td>download_speeds</td>
            <td>Velocidad de bajada</td>
        </tr>
        <tr>
            <td>upload_speeds</td>
            <td>Velocidad de subida</td>
        </tr>
        <tr>
            <td>phone</td>
            <td>Teléfono</td>
        </tr>
        <tr>
            <td>link_identifiers</td>
            <td>Identificador del enlace</td>
        </tr>
        <tr>
            <td>link_status</td>
            <td>Estado del enlace</td>
        </tr>
        <tr>
            <td>activation_date</td>
            <td>Fecha de activación</td>
        </tr>
        <tr>
            <td>blocking_date_home</td>
            <td>Fecha de bloqueo</td>
        </tr>
        <tr>
            <td>date_of_elimination_home</td>
            <td>Fecha de eliminación</td>
        </tr>
        <tr>
            <td>quota_fund</td>
            <td>Fondo de cuota</td>
        </tr>
        <tr>
            <td>voucher</td>
            <td>Bono</td>
        </tr>
        <tr>
            <td>debt</td>
            <td>Deuda</td>
        </tr>
    </table>
</details>

**Nota**: Los `métodos` y `propiedades` disponibles para `Nauta` también lo están para `Nauta Hogar`.

### **Usando UserPortal**

Mismo ejercicio que con la clase [UserPortalClient](#usando-nautaclient)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyLibSuitETECSA.core.protocol import UserPortal
from PyLibSuitETECSA.core.exception import RechargeException,\
    TransferException
from PyLibSuitETECSA.utils import Action

# Crea una sesión que se almacena en la variable
# session
session = UserPortal.create_session()

# Obtiene la imagen captcha del portal y la guarda
# en un archivo llamado 'captcha.png'
with open('captcha.png', 'wb') as fp:
    fp.write(
        UserPortal.get_captcha(session)
    )

# Loguea la cuenta en el portal
UserPortal.login(
    session=session,
    username="user.name@nauta.com.cu",
    password="password",
    captcha_code=input('captcha code: ')
)

# Trata de recargar la cuenta y en caso de error
# lo imprime en pantalla
try:
    UserPortal.recharge(
        session=session,
        recharge_code="1234567890123456"
    )
except RechargeException as ex:
    print(f'Error al recargar :: {ex.args[0]}')

# Trata de transferir saldo a otra cuenta y en caso
# de errores los inprime en pantalla
try:
    UserPortal.transfer(
        session=session,
        mount_to_transfer=250.25,
        account_to_transfer="lesly.cintra@nauta.co.cu"
    )
except TransferException as ex:
    print(f'Error al transferir :: {ex.args[0]}')

# Obtiene las últimas 5 conexiones realizadas por la cuenta
# y las imprime en pantalla en formato json
connections = UserPortal.get_lasts(
    session=session,
    action=Action.GET_CONNECTIONS
)
for connection in connections:
    print(connection.__dict__)

```

Salida:

```console
captcha code: 2GH9SV
Error al recargar :: El código de recarga es incorrecto.
Error al transferir :: ['El campo saldo a transferir debe ser menor o igual que 14761']
{'start_session': datetime.datetime(2023, 1, 22, 22, 19, 11), 'end_session': datetime.datetime(2023, 1, 22, 22, 24, 8), 'duration': 297, 'uploaded': 275456, 'downloaded': 1782579, 'import_': 0.99}
{'start_session': datetime.datetime(2023, 1, 22, 11, 26, 8), 'end_session': datetime.datetime(2023, 1, 22, 14, 28, 13), 'duration': 10925, 'uploaded': 17637048, 'downloaded': 244454522, 'import_': 36.42}
{'start_session': datetime.datetime(2023, 1, 21, 16, 53, 29), 'end_session': datetime.datetime(2023, 1, 22, 1, 36, 8), 'duration': 31359, 'uploaded': 152746065, 'downloaded': 2168958484, 'import_': 104.53}
{'start_session': datetime.datetime(2023, 1, 20, 18, 19, 56), 'end_session': datetime.datetime(2023, 1, 20, 18, 25, 16), 'duration': 320, 'uploaded': 447488, 'downloaded': 8409579, 'import_': 1.07}
{'start_session': datetime.datetime(2023, 1, 20, 17, 29, 40), 'end_session': datetime.datetime(2023, 1, 20, 18, 12, 5), 'duration': 2545, 'uploaded': 7140802, 'downloaded': 113592238, 'import_': 8.49}
```

## Usando NautaClient

```python
import time

from PyLibSuitETECSA.api import NautaClient  # se importa el cliente para el portal cautivo de nauta

nauta_ci = NautaClient(  # se instancia el cliente
    "usuario@nauta.com.cu",
    "Contraseña"
)

nauta_ci.init_session()  # se inicia la session donde se guardan las cookies y datos

with nauta_ci.login():  # se inicia sesión en el portal y se mantiene abierta durante un minuto
    print(nauta_ci.remaining_time)
    time.sleep(60)

```

## Funciones y propiedades de UserPortalClient

### Funciones

* init_session: Crea la session donde se guardan las cookies y datos
* login: Loguea al usuario en el portal
* logout: Cierra la sesión abierta
* load_last_session: Carga la última session creada

### Propiedades

* is_logged_in: Si se está loagueado en el portal
* user_credit: Saldo de la cuenta
* remaining_time: Tiempo restante

## Contribuir

**IMPORTANTE**: PyLibSuitETESA necesita compatibilidad con nauta hogar.

Todas las contribuciones son bienvenidas. Puedes ayudar trabajando en uno de los issues existentes.
Clona el repo, crea una rama para el issue que estés trabajando y cuando estés listo crea un Pull Request.

También puedes contribuir difundiendo esta herramienta entre tus amigos y en tus redes. Mientras
más grande sea la comunidad más sólido será el proyecto.

Si te gusta el proyecto dale una estrella para que otros lo encuentren más fácilmente.

## Dependencias

```text
requests~=2.27.1
beautifulsoup4~=4.10.0
pytest~=7.1.2
setuptools~=60.2.0
```
