# Análise de Sentimentos com BERT

Este repositório contém implementações de análise de sentimentos em textos em português utilizando o modelo BERT (Bidirectional Encoder Representations from Transformers).

## O que é o BERT?

BERT é um modelo de linguagem desenvolvido pelo Google que revolucionou o processamento de linguagem natural (NLP). Suas principais características são:

- **Bidirecional**: Diferente de modelos anteriores, o BERT analisa o contexto das palavras em ambas as direções (antes e depois), permitindo um entendimento mais profundo do significado.
- **Pré-treinado**: O modelo é treinado em um grande corpus de texto não rotulado, aprendendo representações ricas da linguagem.
- **Transformers**: Utiliza a arquitetura Transformer, que permite processar todas as palavras de uma frase simultaneamente, capturando relações complexas entre elas.

## Implementações

O repositório contém as seguintes implementações:

1. **BERT Multilíngue** (`bert_sentiment_analyzer.py`):
   - Utiliza o modelo `nlptown/bert-base-multilingual-uncased-sentiment`
   - Classifica textos em 5 níveis de sentimento (de Muito Negativo a Muito Positivo)
   - Ideal para análise mais granular de sentimentos

2. **Pub/Sub Integration** (`pubsub_sentiment_analyzer.py`):
   - Integração com Google Cloud Pub/Sub para análise em tempo real
   - Lê mensagens de uma subscription do Pub/Sub
   - Processa automaticamente cada mensagem usando o BERT Multilíngue
   - Exibe resultados da análise de sentimento em tempo real

## Como usar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente para o Pub/Sub:
```bash
export GOOGLE_CLOUD_PROJECT="seu-projeto-id"
export PUBSUB_SUBSCRIPTION_ID="sua-subscription-id"
```

3. Execute um dos analisadores:
```bash
# Para análise direta de textos
python bert_sentiment_analyzer.py

# Para análise de mensagens do Pub/Sub
python pubsub_sentiment_analyzer.py
```

## Requisitos

- Python 3.6+
- PyTorch
- Transformers
- NumPy
- Google Cloud Pub/Sub

## Exemplos de uso

Os scripts incluem exemplos de análise de sentimentos em diferentes tipos de textos, como avaliações de produtos, comentários sobre serviços e expressões cotidianas em português.

### Pub/Sub Integration

O componente Pub/Sub permite analisar mensagens em tempo real. Para usar:

1. Certifique-se de ter uma conta Google Cloud Platform configurada
2. Configure as credenciais do Google Cloud:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
   ```
3. Execute o script `pubsub_sentiment_analyzer.py`
4. As mensagens recebidas serão automaticamente analisadas e os resultados serão exibidos no console
