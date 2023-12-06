# Hotel Reservations Predict

Trata-se de um projeto que utiliza um dataset de reservas de hotel para fazer previsões com o algoritmo RandomForestClassifier para clasfificar qual tipo de acomodação o cliente precisa por faixa de preço.
É feito um consumo do modelo treinado no Sagemaker através de um endpoint dispnibilidado por uma API simples disponibilizada por meio do FLASK.

## Referência

 - [Dataset utilizado](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset)
 


## Desenvolvimento do projeto

1. Foi realizada a seleção de um modelo adequado para a análise dos parâmetros dos dados. Depois, ocorreu o carregamento do _dataset_ e filtragem das colunas que seriam relevantes para a classificação. Depois, foi feita a preparação e treinamento do modelo. Finalmente, o modelo foi enviado para um Bucket S3, onde foi salvo.

2. Neste passo, icia-se o desenvolvimento da API, onde é realizada a integração do código com a AWS para a extração do modelo do Bucket e, com o modelo criado, a rota POST para que possa receber os dados, respondendo com uma classificação.

A classificação funciona da seguinte forma:

    1 = avg_price_per_room tiver valor menor ou igual a 85
    2 = avg_price_per_room tiver valor maior que 85 e menor que 115
    3 = avg_price_per_room tiver valor maior ou igual a 115.

3. Nesta etapa, rodamos a aplicação dentro de um container do Docker inserindo os parâmetros necessários para sua execução. Uma vez que a aplicação funcionou em um container, criamos o arquivo docker-compose.yaml, testamos localmente e seguimos para a próxima etapa.

4. Finalmente a aplicação foi colocada no Amazon ElasticBeanstalk para ficar disponível para o público.

## Exemplo

1- Entrada via POSTMAN
```json
{
	"no_of_adults":1,
	"no_of_children":0,
	"no_of_weekend_nights":2,
	"no_of_week_nights":3,
	"required_car_parking_space":0,
	"room_type_reserved":1,
	"lead_time":244,
	"arrival_year":2018,
	"arrival_month":10,
	"arrival_date":30,
	"repeated_guest":0,
	"no_of_previous_cancellations":0,
	"no_of_previous_bookings_not_canceled":0,
	"no_of_special_requests":0
}
```

2- Saída
```json
{
	"result": 1
}
```
### Accuracy 
![Accuracy Score](https://github.com/well651/hotelreservationspredict/blob/main/public/accuracyscore.png)
