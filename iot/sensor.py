import time
import random
import paho.mqtt.client as mqtt

BROKER = "localhost"   # conecta ao broker exposto pelo docker
PORT = 1883
TOPIC = "sensor/irrigacao"

def main():
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    print("🔵 Sensor iniciado. Publicando dados em:", TOPIC)

    try:
        while True:
            umidade = random.randint(20, 80)  # %
            payload = str(umidade)
            client.publish(TOPIC, payload)
            print(f"🌱 Umidade: {umidade}% → publicado")
            time.sleep(3)
    except KeyboardInterrupt:
        print("Sensor finalizado pelo usuário.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()
