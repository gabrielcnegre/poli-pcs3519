from prometheus_client import start_http_server, Gauge
import random
import time
from datetime import datetime

consumo_total = Gauge('energy_consumption_total', 'Consumo total de energia (kWh)')
pico_consumo = Gauge('energy_peak_consumption', 'Pico de consumo recente (kWh)')
custo_estimado = Gauge('energy_cost', 'Custo estimado da energia (R$)')
consumo_por_comodo = Gauge('energy_consumption', 'Consumo de energia por cômodo (kWh)', ['room'])

portas_janelas = Gauge('door_window_status', 'Status de portas e janelas (1=aberta, 0=fechada)', ['componente'])
movimento_suspeito = Gauge('suspicious_movement_night', 'Movimento suspeito durante a noite (1 ou 0)')
visitantes = Gauge('visitors_count', 'Contagem de visitantes')
ocupacao_comodo = Gauge('room_occupancy', 'Ocupação por cômodo (1=ocupado, 0=vazio)', ['room'])

temperatura = Gauge('temperature', 'Temperatura (°C)', ['room'])
umidade = Gauge('humidity', 'Umidade relativa (%)', ['room'])

voc = Gauge('voc_level', 'Nível de VOCs (ppm)', ['room'])
co2 = Gauge('co2_level', 'Nível de CO2 (ppm)', ['room'])

comodos = ['sala', 'quarto', 'cozinha', 'banheiro']
componentes = ['porta_entrada', 'porta_quarto', 'janela_sala', 'janela_cozinha']

def hora_atual_entre(inicio, fim):
    agora = datetime.now().time()
    return inicio <= agora <= fim

if __name__ == "__main__":
    start_http_server(8000, addr="0.0.0.0")

    total_acumulado = 0

    while True:
        total = 0
        for room in comodos:
            consumo = random.uniform(0.1, 1.0)
            total += consumo
            total_acumulado += total
            consumo_por_comodo.labels(room).set(consumo)
        consumo_total.set(total)
        pico_consumo.set(max(total, random.uniform(1.0, 3.0)))
        custo_estimado.set(total_acumulado * 0.92)  

        for comp in componentes:
            portas_janelas.labels(comp).set(random.choice([0, 1]))

        if hora_atual_entre(datetime.strptime("00:00", "%H:%M").time(), datetime.strptime("05:59", "%H:%M").time()):
            movimento_suspeito.set(random.choice([0, 1]))
        else:
            movimento_suspeito.set(0)

        visitantes.set(random.randint(0, 5))

        for room in comodos:
            ocupacao_comodo.labels(room).set(random.choice([0, 1]))

        for room in comodos:
            temperatura.labels(room).set(random.uniform(20.0, 30.0))
            umidade.labels(room).set(random.uniform(30.0, 70.0))
            voc.labels(room).set(random.uniform(0.2, 1.2))
            co2.labels(room).set(random.uniform(350, 1200))

        time.sleep(1)
