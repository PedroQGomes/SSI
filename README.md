# SSI
# 4ºAno - Segurança de Sistemas Informáticos 
Trabalhos práticos sobre pen testing e scan ativo e passivo de serviços  

## TP1 -
O primeiro trabalho pratico consiste na descrição de potenciais incidentes de segurança que um sistema, que consiste em duas aplicações moveis e um backend do sistema, pode estar exposto durante produção. 

Algumas das técnicas usadas neste trabalho foram as seguintes

* Catalogação de vulnerabilidades e exploits
* Catalogação de fraquezas típicas 
* Modelação de ameaças, orientado aos ativos, atacantes e software
* Analise de risco


## TP2 -

O segundo trabalho pratico tem duas fases em que a primeira consiste em escolher duas empresas, uma local e uma grande corporação, e efetuar técnicas de procura passiva de informação sobre as mesmas e comparar as diferenças nos resultados.\
Na Segunda fase do trabalho foi configurado um ambiente de testes, uma maquina virtual com kali linux e outra maquina virtual com um sistema com diferentes vulnerabilidades `metasploitable 3`,  no qual técnicas de procura ativa de informação são usadas(scanning) para detetar vulnerabilidades e fraquezas num sistema remoto.

Algumas das ferramentas utilizadas para a segunda fase do trabalho pratico 2 foram as seguintes

* Scanner de Vulnerabilidades - Nessus
* Scan de ports - nmap
* Sistemas de deteção de intrusão (IDS) - Suricata
* Analisador de trafico - Wireshark


## TP3 -

O terceiro trabalho pratico consiste na implementação de um mecanismo adicional de autorização de operações de aberturas de ficheiros. Este mecanismo foi implementado com base na `libfuse` e tem as seguintes funcionalidades 

* Autorizar a operação de abertura apenas depois da introdução de um código
de segurança único enviado ao utilizador que o despoletou
* Manter o registo de todos os utilizadores que poderão aceder ao sistema de
ficheiros
* Ao invocar a operação open() de abertura de ficheiros, deve ser retornado,
sucesso quando tiver recebido o código de segurança enviado ao utilizador ou
insucesso, quando não corresponde ao código ou tiverem sido ultrapassados 30
segundos
* Criar uma interface para o servidor, ao qual o utilizador irá comunicar o
código de segurança recebido
