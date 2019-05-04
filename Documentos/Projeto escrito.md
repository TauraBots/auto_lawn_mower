# Taura_Mower
O objetivo do projeto é automatizar um cortador de grama comercial, ou seja, implementar dispositivos em um cortador de
grama com motor a gasolina convencional, para que consiga cumprir seu objetivo sem a necessidade de um operador.

## Materiais:
* **Cortador de grama:** Um cortador de grama a gasolina, onde será embarcada a inteligência para automação. A escolha
de um motor a gasolina, ao invés de um elétrico deve-se ao fator de autonomia, como o objetivo do projeto exige que o
cortador não fique ligado através de um cabo, mas sim que tenha sua navegação irrestrita, escolher um motor a
combustão é o mais inteligente, visando a economia em baterias, a facilidade de reabastecimento e a diminuição do peso
do projeto.

* **Motores:** Serão o que exerce a navegação do cortador, devem ter torque suficiente para movê-lo em terrenos
irregulares. São dois motores que devem atuar nas rodas trazeiras do cortador, e darão a capacidade de realizar todas as 
manobras necessárias para navegar.

* **Baterias:** Alimentarão os motores de navegação, os sensores e os computadores embarcados no cortador.

* **Alternador:** Utilizaremos um alternador para reabastecer as baterias com a rotação do motor a gasolina e aumentar a 
autonomia do cortador.

* **Ponte H:** Necessária para controle dos motores elétricos.

* **Rodas:** Serão as rodas trazeiras, que realizarão a tração do cortador.

* **Rodas bobas:** Serão as rodas dianteiras, elas precisam apenas apoiar o cortador no chão e permitirem a movimentação.

* **Arduino Uno:** Fará o controle dos motores e o tradamento dos dados dos sensores.

* **Raspberry Pi:** Rodará o software embarcado no cortador.

* **Dynamixel:** Realizará o controle do acelerador do motor a gasolina, também servirá como atuador de desligamento do
motor em caso de uma emergência.

* **Lidar:** Será o sensor faz a leitura do ambiente e permitirá que o cortador evite colisões com obstáculos móveis e imóveis.

* **GPS:** Responsável pela capacidade de o cortador saber onde se encontra na área delimitada para corte com uma precisão rasoável

* **Giroscópio:** Será utilizado na odometria do cortador e também como um dispositivo de segurança para desligamento da hélice em
cenários onde ela possa ficar exposta e ferir o operador.

* **Sensor de cor:** Permitirá o reconhecimento do terreno, servindo como redundância em caso de o cortador sair da área de atuação.

* **Sensor ultrasônico:** ...

* **Módulo LoRa:** Responsável pela capacidade de o cortador saber onde se encontra na área delimitada para corte com uma precisão
maior que a do GPS

* **Sensor de Efeito Hall:** ...
