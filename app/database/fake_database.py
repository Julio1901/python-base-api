import random

# Lista de descrições fakes
fake_descriptions = [
    "Um paraíso escondido com águas cristalinas.",
    "Perfeita para quem gosta de esportes aquáticos.",
    "Uma praia tranquila ideal para famílias.",
    "Muito movimentada no verão, cheia de vida.",
    "Famosa por seus pores do sol inesquecíveis.",
    "Boa opção para quem curte trilhas próximas.",
    "Conhecida pela areia branca e fofa.",
    "Um ponto turístico cheio de bares e restaurantes.",
    "Frequentada por surfistas o ano todo.",
    "Lugar calmo para quem busca paz e descanso."
]

beaches = [
    {
        "id": 0,
        "name": "Praia de Itaúna",
        "state": "Rio de Janeiro",
        "description": random.choice(fake_descriptions),
        "image": "/static/images/itauna.png"
    },
    {
        "id": 1,
        "name": "Praia da Joaquina",
        "state": "Santa Catarina",
        "description": random.choice(fake_descriptions),
        "image": "/static/images/joaquina.png"
    },
    {
        "id": 2,
        "name": "Praia de Itamambuca",
        "state": "São Paulo",
        "description": random.choice(fake_descriptions),
        "image": "/static/images/itamambuca.png"
    },
    {
        "id": 3,
        "name": "Praia de Maresias",
        "state": "São Paulo",
        "description": random.choice(fake_descriptions),
        "image": "/static/images/maresias.png"
    },
    {
        "id": 4,
        "name": "Praia de Fernando de Noronha",
        "state": "Pernambuco",
         "description": random.choice(fake_descriptions),
        "image": "/static/images/fernando-de-noronha.png"
    }
]