import paho.mqtt.client as mqtt
import csv
from datetime import datetime
import os

# --- Configurações MQTT ---
BROKER = "localhost"
PORT = 1883
TOPIC = "decisao/irrigacao"

# --- CSV para histórico ---
CSV_FILE = os.path.join(os.path.dirname(__file__), "..", "log_irrigacao.csv")

# Cria CSV com cabeçalho se não existir
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Umidade", "Irrigacao"])

# Histórico em memória (para mostrar na tela)
historico = []

# --- Função para mostrar a interface no terminal ---
def print_interface(umidade, irrigacao):
    os.system('cls' if os.name == 'nt' else 'clear')  # limpa tela
    print("="*30)
    print("   SISTEMA DE IRRIGAÇÃO EDGE")
    print("="*30)
    print(f"Umidade atual do solo: {umidade}%\n")

    # Barra visual de umidade (20 posições)
    nivel = int((int(umidade)/100) * 20)
    barra = "💧" * nivel + " " * (20-nivel)
    status = "baixa" if int(umidade)<40 else "ok"
    print(f"[{barra}]  Umidade {status}\n")

    # Ação tomada
    if irrigacao == "ATIVADA":
        print("💡 Ação: Ativando irrigação...\n")
    else:
        print("💡 Ação: Irrigação desligada.\n")

    print("🌦️ Enviando dados para a Cloud...\n")

    # Histórico (últimos 5 registros)
    print("Histórico:")
    for h in historico[-5:]:
        print(f" - Umidade: {h[0]}% | Irrigação: {h[1]}")

# --- Callback MQTT quando uma mensagem chega ---
def on_message(client, userdata, msg):
    mensagem = msg.payload.decode()  # Ex: "23|ATIVADA"
    try:
        umidade, irrigacao = mensagem.split("|")
    except ValueError:
        # Se o formato estiver errado
        umidade = mensagem
        irrigacao = "N/A"

    # Atualiza histórico em memória
    historico.append((umidade, irrigacao))

    # Grava no CSV
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, umidade, irrigacao])

    # Mostra interface no terminal
    print_interface(umidade, irrigacao)

# --- Função principal ---
def main():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.subscribe(TOPIC)
    print("🟢 Cloud logger conectado e subscrito em:", TOPIC)
    client.loop_forever()

if __name__ == "__main__":
    main()
