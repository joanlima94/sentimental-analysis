from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
from bert_sentiment_analyzer import BERTSentimentAnalyzer
import os

class PubSubSentimentAnalyzer:
    def __init__(self, project_id, subscription_id):
        self.project_id = project_id
        self.subscription_id = subscription_id
        self.subscriber = pubsub_v1.SubscriberClient()
        self.subscription_path = self.subscriber.subscription_path(
            project_id, subscription_id
        )
        self.bert_analyzer = BERTSentimentAnalyzer()

    def callback(self, message):
        try:
            data = message.data.decode("utf-8")
            print(f"Mensagem recebida: {data}")

            sentiment, confidence = self.bert_analyzer.analyze_sentiment(data)
            
            print(f"Análise de Sentimento:")
            print(f"Texto: {data}")
            print(f"Sentimento: {sentiment}")
            print(f"Confiança: {confidence:.2f}")
            print("-" * 50)

            message.ack()

        except Exception as e:
            print(f"Erro ao processar mensagem: {e}")
            message.nack()

    def listen(self, timeout=None):
        streaming_pull_future = self.subscriber.subscribe(
            self.subscription_path, callback=self.callback
        )
        print(f"Escutando mensagens na subscription: {self.subscription_path}")

        try:
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            streaming_pull_future.cancel()
            streaming_pull_future.result()
        except Exception as e:
            streaming_pull_future.cancel()
            print(f"Erro durante a execução: {e}")
        finally:
            streaming_pull_future.cancel()
            self.subscriber.close()

def main():
    project_id = "my-project-1070912"
    subscription_id = "twitter-mentions-sub"

    if not project_id or not subscription_id:
        print("Error: As variáveis de ambiente GOOGLE_CLOUD_PROJECT e PUBSUB_SUBSCRIPTION_ID precisam estar definidas")
        return

    analyzer = PubSubSentimentAnalyzer(project_id, subscription_id)
    
    try:
        analyzer.listen()
    except KeyboardInterrupt:
        print("\nEncerrando o programa...")

if __name__ == "__main__":
    main()
