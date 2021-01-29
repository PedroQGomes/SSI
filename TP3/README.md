- [x] Instalar a libraria fusepy

- [x] Criar duas diretorias uma onde o sistema de ficheiros vai ser montado,diretoriaMount, e outra para ser o ponto de partida do mesmo,diretoriaFicheiro 

- [x] Na diretoria /diretoriaFicheiro criar alguns ficheiros, com ou sem texto, de modo a no futuro testar o sistema de ficheiros

- [x] Num terminal correr python3 FileSystem.py /diretoriaFicheiro/ /diretoriaMount/ . Nao é necessario qualquer interaçao neste terminal depois de estar a correr
- Em caso de erro de permissoes na /diretoriaMount/ -> chmod 777 /diretoriaMount

- [x] Num segundo terminal correr python3 server.py . É aqui que o utilizador ira introduzir o seu codigo de segurança quando for pedido.

- [x] Caso seja pretendido testar, num terceiro terminal é necessario ir para a diretoria do sistema de ficheiros, cd /diretoriaMount, e executar um comando que abra os ficheiros que se encontrem na diretoria, por exemplo cat,vim,nano etc...


