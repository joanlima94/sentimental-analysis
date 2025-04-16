# Análise de Sentimentos com BERT

Este repositório contém implementações de análise de sentimentos em textos em português utilizando o modelo BERT (Bidirectional Encoder Representations from Transformers).

## O que é o BERT?

BERT é um modelo de linguagem desenvolvido pelo Google que revolucionou o processamento de linguagem natural (NLP). Suas principais características são:

- **Bidirecional**: Diferente de modelos anteriores, o BERT analisa o contexto das palavras em ambas as direções (antes e depois), permitindo um entendimento mais profundo do significado.
- **Pré-treinado**: O modelo é treinado em um grande corpus de texto não rotulado, aprendendo representações ricas da linguagem.
- **Transformers**: Utiliza a arquitetura Transformer, que permite processar todas as palavras de uma frase simultaneamente, capturando relações complexas entre elas.

## Implementações

O repositório contém duas implementações de análise de sentimentos:

1. **BERT Multilíngue** (`bert_sentiment_analyzer.py`):
   - Utiliza o modelo `nlptown/bert-base-multilingual-uncased-sentiment`
   - Classifica textos em 5 níveis de sentimento (de Muito Negativo a Muito Positivo)
   - Ideal para análise mais granular de sentimentos

## Como usar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute um dos analisadores:
```bash
python bert_sentiment_analyzer.py
```

## Requisitos

- Python 3.6+
- PyTorch
- Transformers
- NumPy

## Exemplos de uso

Os scripts incluem exemplos de análise de sentimentos em diferentes tipos de textos, como avaliações de produtos, comentários sobre serviços e expressões cotidianas em português.
