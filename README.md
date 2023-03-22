# API para Predição de Locais em Imagem

Rest Api construida em FastApi que possui um endpoint que recebe um imagem (arquivo .png, .jpg, jpeg) e faz um predição para indentificar o tipo de local da imagem.

## Como rodar

A aplicação foi feita utilizando Docker, então você pode executar seguindo os seguintes passos:

Criando/Buildando a aplicação.
```bash
docker build -t api-place-classifier .
```

Criando um container e rodando a aplicação.
```bash
docker run -d --name api-place-classifier -p 8000:8000 fastapi-classifier
```

## Como acessar a aplicação?

A aplicação por default irá rodar na porta 8000 do seu localhost.

[http://localhost:8000](localhost:8000)

Você pode testar a aplicação através dos docs da API, que permite realizar chamadas http para a aplicação:
[http://localhost:8000/docs](localhost:8000/docs)

## Deploy

Você pode acessar um ambiente teste da aplicação em deploy:

[https://place-classifier-api.onrender.com/docs](https://place-classifier-api.onrender.com/docs)