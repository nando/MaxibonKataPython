![The Cocktail logo][tcklogo] ❤ ![Karumi logo][karumilogo]
# Kata Maxibon for Python. [![Build Status](https://travis-ci.org/nando/MaxibonKataPython.svg?branch=master)](https://travis-ci.org/nando/MaxibonKataPython)

## Bonus track: The Maxiconf Problem

_Karumi_ y _The Cocktail_ traman la futura celebración de la Maxiconf, una conferencia que surge a raíz de la fascinación de algunes de sus desarrolladores por [la kata de _Property-based Testing_ del Maxibon](https://github.com/nando/MaxibonKataPython).

Por un malentendido con la empresa encargada de la organización del evento, el congelador del único frigorífico existente en el lugar en el que se celebrará la conferencia sólo tiene capacidad para contener los maxibons indicados por **KarumiHQs::MAX_MAXIBONS** (10 maxibons).

**KarumiHQs** es la clase que tiene toda la lógica necesaria para manejar la intendencia el evento: **MIN_MAXIBONS** (3 maxibons) es el umbral bajo el cual solicitará de forma automágica un nuevo pedido de los maxibons indicados por **MAX_MAXIBONS** (por correo electrónico o levantando una lambda, dependiendo del presupuesto final :P).

Si tenemos 3 maxibons y, por ejemplo, alguien nos pide uno más, se realizará el pedido y no tardaremos mucho en tener 12 maxibons en nuestro frigorífico: en la Maxiconf dos de ellos no entrarían en el congelador y esperarían en el frigorífico a que alguien llegue antes de que se derritan demasiado :pray::pray::pray:.

Sin embargo, si en esa misma situación la persona que llega pide 3 maxibons o más, el congelador se quedará vacío con espacio para los 10 maxibons que llegarán en breve.

**El Problema de la Maxiconf (R)** es establecer un orden de llegada que garantice que **todes les programadores de la Maxiconf toman su Maxibon sin derretirse** lo más mínimo. ;)

![Maxibon][maxibon]

# License

Copyright 2019 Karumi & The Cocktail Global

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[karumilogo]: https://cloud.githubusercontent.com/assets/858090/11626547/e5a1dc66-9ce3-11e5-908d-537e07e82090.png
[tcklogo]: https://avatars0.githubusercontent.com/u/1177560?s=40
[maxibon]: ./art/maxibon.jpg
