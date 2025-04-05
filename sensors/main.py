from prometheus_client import start_http_server, Gauge
import random
import time

consumo = Gauge('residencia_consumo_kwh', 'Consumo atual em kWh', ['comodo'])
temperatura = Gauge('residencia_temperatura_celsius', 'Temperatura atual em Celsius', ['comodo'])
umidade = Gauge('residencia_umidade_percentual', 'Umidade relativa do ar (%)', ['comodo'])
voc = Gauge('residencia_voc_ppm', 'Nível de VOCs (ppm)', ['comodo'])
co2 = Gauge('residencia_co2_ppm', 'Nível de CO2 (ppm)', ['comodo'])
movimento = Gauge('residencia_movimento_detectado', 'Movimento detectado (0 ou 1)', ['comodo'])

comodos = ['sala', 'quarto', 'cozinha', 'porta', 'janela']

if __name__ == "__main__":
    start_http_server(8000, addr="0.0.0.0")
    while True:
        for comodo in comodos:
            consumo.labels(comodo).set(random.uniform(0, 1))
            temperatura.labels(comodo).set(random.uniform(20, 30))
            umidade.labels(comodo).set(random.uniform(30, 70))
            voc.labels(comodo).set(random.uniform(0, 1))
            co2.labels(comodo).set(random.uniform(0, 1))
            movimento.labels(comodo).set(random.choice([0, 1]))
        time.sleep(3)
