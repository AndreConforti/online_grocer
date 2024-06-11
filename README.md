# Quitanda Online

Este repositório contém uma aplicação web em desenvolvimento, de uma Quitanda Online, desenvolvida com HTML e Bootstrap 5 no front-end e Django no back-end. A aplicação permite login de usuários, envio de mensagens através da página de contato, e está contida em um container Docker para o aprendizado do uso de containers. Futuramente, a aplicação incluirá páginas de produtos, alteração de cadastro de usuário, carrinho de compras e finalização de pedidos, com a possibilidade de adicionar endereços para entrega e a forma de pagamento.

Este projeto está disponível para qualquer pessoa interessada em baixar e realizar testes seguindo os comandos fornecidos. Utilizando Docker, a aplicação será isolada do ambiente do usuário, garantindo que não haverá conflitos de software na máquina onde estiver sendo executada.

**Nota:** Para fins de conformidade com a Lei Geral de Proteção de Dados (LGPD), utilize apenas dados fictícios durante os testes. Os dados de usuários serão armazenados apenas no banco de dados local do ambiente de testes.

## Índice
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Benefícios do Uso do Docker](#benefícios-do-uso-do-docker)
- [Contribuição](#contribuição)
- [Agradecimentos](#agradecimentos)

## Funcionalidades

- Sistema de login e registro de usuários
- Envio de mensagens através da página de contato
- Contenção da aplicação em um container Docker
- **Futuras Funcionalidades:**
  - Páginas de produtos
  - Alteração de cadastro de usuário
  - Carrinho de compras
  - Finalização de pedidos
  - Adição de endereços para entrega e formas de pagamento

## Tecnologias Utilizadas

- Front-end: HTML, Bootstrap 5
- Back-end: Django, Django Allauth
- Contenção: Docker

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- [Git](https://git-scm.com)
- [Docker](https://www.docker.com)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Instalação

### Instalação no Linux ou no Windows

1. Clone o repositório:
   
   No Linux, abra uma janela de terminal. No Windows, abra o PowerShell ou o prompt de comando.
   
   Execute o comando:

   ```bash
   git clone git@github.com:AndreConforti/online_grocer.git
   cd online_grocer
   
2. Construa e inicie o container Docker:

   ```bash
   sudo docker-compose up --build

  Isso criará e iniciará o container definido no arquivo docker-compose.yml

## Uso

1. Acesse a aplicação no seu navegador através de URL:
   
   ```bash
   http://localhost:8000
   
3. Para parar a aplicação, utilize o comando no terminal, PowerShell ou prompt de comando:
   
   ```bash
   docker-compose down

## Benefícios do uso do Docker:

- **Isolamento de Ambiente:** A aplicação rodará em um ambiente contido, evitando conflitos de software com outros programas instalados na máquina do usuário.
- **Consistência:** Garante que a aplicação funcione da mesma forma em qualquer ambiente, já que todas as dependências são gerenciadas dentro do container.
- **Segurança:** Como a aplicação está isolada, há uma camada adicional de segurança, separando o ambiente de desenvolvimento/teste do restante do sistema operacional do usuário.

## Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

1. Fork o repositório
2. Crie uma branch com a nova funcionalidade (`git checkout -b nova-funcionalidade`)
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade`)
4. Push para a branch (`git push origin nova-funcionalidade`)
5. Abra um Pull Request

## Agradecimentos

Este projeto foi desenvolvido com o auxílio dos materiais disponibilizados pelo canal do YouTube [Maroquio](https://www.youtube.com/@maroquio). 
