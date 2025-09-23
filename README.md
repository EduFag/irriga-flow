# Edge Computing

## 📋 Introdução
A computação em borda é uma abordagem que permite processar dados próximos à origem, reduzindo latência e aumentando a eficiência em sistemas IoT. Para exemplificar esse conceito na prática, vamos utilizar o caso do **IrrigaFlow**, um sistema de irrigação inteligente que aplica lógica fuzzy na borda para tomar decisões em tempo real.

### IrrigaFlow (Simulação):
[Bookmark do projeto IrrigaFlow] <!-- Substitua pelo link real, se desejar -->

## 💡 Conceito de Edge Computing
> 💡 **Edge Computing** é o processamento de dados **perto da fonte**, ou seja, nos próprios dispositivos ou em servidores próximos aos sensores (IoT).

- Diferente da nuvem, que centraliza dados em datacenters, a borda processa informações localmente, **reduzindo latência e uso de banda**.
- Essencial para aplicações **em tempo real**, como irrigação automática, carros autônomos, monitoramento industrial.

**Benefícios principais:**
- **⏱️ Latência baixa**: decisões são tomadas instantaneamente.
- **📶 Redução de banda**: não é preciso enviar todos os dados para a nuvem.
- **🔧 Resiliência**: sistema continua funcionando mesmo com conexão limitada.
- **⚡ Eficiência**: processamento local permite executar algoritmos complexos sem depender de datacenter remoto.

![Conceito de Edge Computing](URL_DA_IMAGEM_EDGE)

## ⚔️ Edge vs Cloud
| Aspecto        | Edge                               | Cloud                             |
|----------------|------------------------------------|-----------------------------------|
| Localização    | Próximo ao sensor/dispositivo      | Datacenter remoto                 |
| Latência       | Baixa                              | Maior                             |
| Processamento  | Decisões rápidas, filtragem de dados | Processamento pesado, análises históricas |
| Uso de banda   | Menor                              | Maior                             |
| Resiliência    | Funciona mesmo offline             | Depende da conexão                |
| Exemplo        | Irrigação automatizada             | Dashboards, análise de longo prazo|

**Conclusão:** Edge = decisões rápidas e locais; Cloud = armazenamento, análise estratégica e suporte à decisão.

## ▶️ Computação de borda na prática
**No IrrigaFlow (projeto real do artigo):**
- A borda é implementada com **Node-RED**, mas poderia ser implementada em **servidores locais, mini-PCs ou dispositivos industriais** próximos ao campo.
- Processa **em tempo real** dados do módulo IoT, aplicando **lógica fuzzy** para decisões de irrigação (tempo e volume).
- Mantém a operação contínua mesmo com conexão limitada à nuvem, garantindo **resiliência e baixa latência**.

## 🏗️ Arquitetura IrrigaFlow (artigo)
<!-- Imagem Arquitetura -->
![Arquitetura IrrigaFlow](https://www.akamai.com/site/en/images/article/2024/how-does-edge-computing-work.png)

**Três camadas principais:**
1. 🌡️ **Módulo IoT:**
   - Sensores e atuadores distribuídos no campo.
   - Coleta umidade, fluxo de água, temperatura, radiação solar, vento, evapotranspiração.
   - Publica dados para a borda.
2. ⚡ **Borda da Rede (Edge):**
   - Processa dados **localmente**, aplicando **lógica fuzzy**.
   - Integra dados do campo + informações do usuário (fase da cultura, textura do solo) + dados climáticos.
   - Decide **tempo e volume de irrigação** em tempo real.
   - Reduz envio de grandes volumes de dados para a nuvem, **diminuindo latência e aumentando eficiência**.
3. ☁️ **Nuvem:**
   - Armazena histórico, fornece dashboards e interface de monitoramento remoto (Node-RED).
   - Permite análise estratégica e ajustes, complementando o processamento da borda.

---

### 🔹 Node-RED como borda
- **Função:** recebe dados do módulo IoT, aplica a lógica de decisão (lógica fuzzy simplificada ou algoritmos mais complexos) e envia a decisão de irrigação para os atuadores.
- **Como funciona na prática:**
  - Normalmente, Node-RED é instalado em **um computador local, servidor ou dispositivo industrial próximo aos sensores**.
  - Esse computador é o que chamamos de **“ponto de borda”** ou **edge device**.
  - Ele faz o processamento **local**, para reduzir latência e não depender de conexão constante com a nuvem.

### 🔹 Node-RED na nuvem
- A nuvem fornece uma interface de monitoramento e controle remoto **via Node-RED**.
- **O que isso quer dizer:**
  - Esse Node-RED na nuvem **não está tomando decisões de irrigação em tempo real**.
  - Ele serve para **visualizar histórico, dashboards, gráficos, relatórios e ajustar parâmetros remotamente**.
  - É mais uma ferramenta de interface e integração, aproveitando a mesma plataforma Node-RED para facilitar o desenvolvimento.

## ⚖️ Decisão entre Borda e Nuvem
**Por que a decisão é feita na borda:**
- Latência mínima → a planta precisa de irrigação imediata.
- Operação contínua → não depende de conexão constante.
- Redução de banda → evita enviar todos os dados para a nuvem.

**Por que a nuvem existe:**
- Armazena histórico e gera dashboards.
- Permite ajustes estratégicos e análise de longo prazo.

**Custos:**
- **Edge:** investimento em hardware local (Raspberry Pi, servidores), manutenção local.
- **Cloud:** armazenamento e processamento remoto, escalável.
- **Combinação:** custo otimizado + alta eficiência.

## 🧪 Simulador (Exemplificação)
- **Sensor simulado:** valores de umidade gerados pelo script.
- **Borda (Node-RED):** decisão simples (`if umidade < 40 → ativar`).
- **Nuvem (Cloud Logger):** armazena histórico em CSV e imprime painel no terminal.

### Diagrama de Fluxo
