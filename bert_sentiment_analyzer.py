from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

class BERTSentimentAnalyzer:
    def __init__(self):
        self.model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        
    def analyze_sentiment(self, text):
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512
        )
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
            
        predicted_class = torch.argmax(predictions).item()
        confidence = predictions[0][predicted_class].item()
        
        sentiment_map = {
            0: "Muito Negativo",
            1: "Negativo",
            2: "Neutro",
            3: "Positivo",
            4: "Muito Positivo"
        }
        
        return sentiment_map[predicted_class], confidence

def main():
    analyzer = BERTSentimentAnalyzer()
    
    textos = [
        "Esse produto é incrível, superou todas as minhas expectativas!",
        "Não gostei do atendimento, foi muito ruim.",
        "O dia está normal, nada de especial aconteceu.",
        "A qualidade do produto é excelente, recomendo muito!",
        "Péssimo serviço, nunca mais volto.",
        "O preço está na média do mercado."
    ]
    
    print("Analisando sentimentos em textos em português...")
    print("-" * 50)
    
    for texto in textos:
        sentimento, confianca = analyzer.analyze_sentiment(texto)
        print(f"\nTexto: {texto}")
        print(f"Sentimento: {sentimento}")
        print(f"Confiança: {confianca:.2f}")

if __name__ == "__main__":
    main()
