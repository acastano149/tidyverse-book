"""
Datasets enriquecidos para el curso de Pandas para Sport Scientists.
Incluye datos de atletas, GPS/tracking, eventos y series temporales.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Seed para reproducibilidad
np.random.seed(42)

# =============================================================================
# DATASET 1: ATLETAS (Perfil físico completo)
# =============================================================================
def get_atletas():
    """
    Dataset de atletas con perfil físico completo.
    15 jugadores con 15+ variables.
    """
    nombres = ['García', 'López', 'Martínez', 'Sánchez', 'Fernández', 
               'González', 'Rodríguez', 'Pérez', 'Gómez', 'Ruiz',
               'Díaz', 'Moreno', 'Álvarez', 'Jiménez', 'Romero']
    
    posiciones = ['Delantero', 'Mediocentro', 'Defensa', 'Portero', 'Delantero',
                  'Mediocentro', 'Defensa', 'Delantero', 'Mediocentro', 'Defensa',
                  'Portero', 'Delantero', 'Mediocentro', 'Defensa', 'Extremo']
    
    edades = [25, 28, 23, 31, 22, 27, 29, 24, 26, 30, 33, 21, 25, 28, 23]
    
    return pd.DataFrame({
        'JugadorID': [f'ATL_{i:03d}' for i in range(1, 16)],
        'Nombre': nombres,
        'Posicion': posiciones,
        'Edad': edades,
        'Altura_cm': [178, 175, 182, 188, 176, 180, 185, 173, 177, 184, 190, 172, 179, 183, 175],
        'Peso_kg': [75, 72, 80, 85, 70, 76, 82, 68, 74, 81, 87, 67, 73, 79, 71],
        'VO2max': [58.5, 62.1, 55.0, 48.2, 60.5, 59.0, 54.5, 61.0, 57.5, 53.0, 46.0, 63.0, 58.0, 55.5, 59.5],
        'FC_Max': [195, 188, 192, 185, 198, 190, 186, 196, 191, 184, 180, 200, 193, 187, 197],
        'FC_Reposo': [52, 48, 55, 58, 50, 51, 54, 49, 53, 56, 60, 47, 52, 55, 50],
        'VelocidadMax_kmh': [32.5, 31.0, 30.2, 28.5, 33.8, 31.5, 29.8, 34.2, 30.5, 29.0, 27.5, 35.0, 31.2, 29.5, 33.0],
        'Potencia_W': [850, 780, 920, 950, 720, 810, 890, 700, 790, 880, 920, 680, 800, 860, 740],
        'SaltoCMJ_cm': [42, 38, 45, 48, 40, 41, 44, 39, 40, 43, 46, 37, 41, 44, 39],
        'T_Test_s': [9.2, 9.5, 9.8, 10.2, 9.0, 9.4, 9.7, 8.9, 9.3, 9.9, 10.5, 8.8, 9.3, 9.6, 9.1],
        'YoYo_IR1_m': [2120, 2400, 1840, 1280, 2280, 2200, 1720, 2360, 2040, 1680, 1120, 2520, 2080, 1800, 2240],
        'Grasa_Corporal_pct': [10.2, 9.8, 11.5, 13.2, 9.5, 10.0, 11.8, 9.2, 10.5, 12.0, 14.5, 8.8, 10.3, 11.2, 9.6],
        'Contrato_Hasta': ['2026-06-30', '2025-06-30', '2027-06-30', '2024-06-30', '2028-06-30',
                          '2025-12-31', '2026-06-30', '2027-12-31', '2025-06-30', '2024-12-31',
                          '2024-06-30', '2029-06-30', '2026-06-30', '2025-06-30', '2027-06-30'],
        'Valor_Mercado_EUR': [5_000_000, 8_000_000, 3_500_000, 2_000_000, 12_000_000,
                             6_500_000, 4_000_000, 15_000_000, 5_500_000, 3_000_000,
                             1_500_000, 25_000_000, 7_000_000, 4_500_000, 10_000_000]
    })


# =============================================================================
# DATASET 2: GPS SESIONES (Datos de entrenamiento y partidos)
# =============================================================================
def get_gps_sesiones():
    """
    Dataset de sesiones GPS con métricas de carga.
    30 sesiones con datos completos.
    """
    np.random.seed(42)
    n_sesiones = 60
    
    jugadores = ['ATL_001', 'ATL_002', 'ATL_003', 'ATL_004', 'ATL_005',
                 'ATL_008', 'ATL_012', 'ATL_015']
    
    tipos = ['Entrenamiento', 'Partido', 'Recuperación']
    fechas_base = pd.date_range('2024-01-01', periods=30, freq='D')
    
    data = []
    for i in range(n_sesiones):
        jugador = np.random.choice(jugadores)
        tipo = np.random.choice(tipos, p=[0.6, 0.25, 0.15])
        fecha = np.random.choice(fechas_base)
        
        # Ajustar métricas según tipo de sesión
        if tipo == 'Partido':
            dist = np.random.randint(9000, 12500)
            hsr = np.random.randint(600, 1100)
            sprint = np.random.randint(200, 450)
            duracion = np.random.randint(85, 98)
            rpe = np.random.randint(7, 10)
        elif tipo == 'Entrenamiento':
            dist = np.random.randint(4000, 7500)
            hsr = np.random.randint(100, 500)
            sprint = np.random.randint(30, 180)
            duracion = np.random.randint(60, 90)
            rpe = np.random.randint(4, 8)
        else:  # Recuperación
            dist = np.random.randint(2000, 4000)
            hsr = np.random.randint(0, 100)
            sprint = np.random.randint(0, 30)
            duracion = np.random.randint(30, 50)
            rpe = np.random.randint(2, 4)
        
        data.append({
            'SesionID': f'SES_{i+1:04d}',
            'JugadorID': jugador,
            'Fecha': fecha,
            'TipoSesion': tipo,
            'Duracion_min': duracion,
            'Distancia_Total_m': dist,
            'HSR_m': hsr,  # High Speed Running (>21 km/h)
            'Sprint_m': sprint,  # Sprints (>25 km/h)
            'Num_Sprints': sprint // 25 + np.random.randint(0, 5),
            'Aceleraciones': np.random.randint(20, 80),
            'Deceleraciones': np.random.randint(18, 75),
            'PlayerLoad': round(dist * 0.08 + np.random.uniform(-50, 50), 1),
            'RPE': rpe,
            'HR_Media': np.random.randint(130, 170),
            'HR_Max': np.random.randint(175, 198),
            'Zona_HR_5_pct': round(np.random.uniform(5, 25), 1)
        })
    
    return pd.DataFrame(data)


# =============================================================================
# DATASET 3: TRACKING (Series temporales 10Hz)
# =============================================================================
def get_tracking_sample():
    """
    Muestra de datos de tracking a 10Hz.
    Simula 30 segundos de juego para 4 jugadores.
    """
    np.random.seed(42)
    
    frames = 300  # 30 segundos a 10Hz
    jugadores = ['ATL_001', 'ATL_002', 'ATL_003', 'ATL_008']
    
    data = []
    for jugador in jugadores:
        # Posición inicial aleatoria
        x = np.random.uniform(20, 85)
        y = np.random.uniform(10, 58)
        
        for frame in range(frames):
            # Simular movimiento realista
            dx = np.random.normal(0, 0.5)  # cambio en x
            dy = np.random.normal(0, 0.3)  # cambio en y
            
            x = np.clip(x + dx, 0, 105)
            y = np.clip(y + dy, 0, 68)
            
            velocidad = np.sqrt(dx**2 + dy**2) * 10  # m/s
            aceleracion = np.random.normal(0, 1)  # m/s²
            
            data.append({
                'Frame': frame,
                'Tiempo_s': round(frame / 10, 1),
                'JugadorID': jugador,
                'Equipo': 'Local',
                'X': round(x, 2),
                'Y': round(y, 2),
                'Velocidad_ms': round(abs(velocidad), 2),
                'Aceleracion_ms2': round(aceleracion, 2),
                'Periodo': 1,
                'PartidoID': 'MATCH_001'
            })
    
    return pd.DataFrame(data)


# =============================================================================
# DATASET 4: EVENTOS (Estilo StatsBomb)
# =============================================================================
def get_eventos():
    """
    Dataset de eventos de partido estilo StatsBomb.
    Incluye pases, tiros, duelos, etc.
    """
    np.random.seed(42)
    n_eventos = 150
    
    tipos_evento = ['Pase', 'Pase', 'Pase', 'Tiro', 'Duelo', 'Recepción', 'Conducción', 'Despeje']
    jugadores = ['ATL_001', 'ATL_002', 'ATL_003', 'ATL_005', 'ATL_008', 
                 'ATL_009', 'ATL_012', 'ATL_013', 'ATL_014', 'ATL_015']
    
    data = []
    minuto = 0
    segundo = 0
    
    for i in range(n_eventos):
        tipo = np.random.choice(tipos_evento)
        jugador = np.random.choice(jugadores)
        
        # Coordenadas según tipo de evento
        if tipo == 'Tiro':
            x_ini = np.random.uniform(85, 105)
            y_ini = np.random.uniform(20, 48)
            x_fin = 105  # Portería
            y_fin = 34  # Centro portería
            resultado = np.random.choice(['Gol', 'A puerta', 'Fuera', 'Bloqueado'], p=[0.1, 0.3, 0.4, 0.2])
            xg = round(np.random.uniform(0.02, 0.35), 3)
            parte_cuerpo = np.random.choice(['Pie derecho', 'Pie izquierdo', 'Cabeza'], p=[0.5, 0.35, 0.15])
        else:
            x_ini = np.random.uniform(10, 95)
            y_ini = np.random.uniform(5, 63)
            x_fin = x_ini + np.random.uniform(-20, 30)
            y_fin = y_ini + np.random.uniform(-15, 15)
            resultado = np.random.choice(['Exitoso', 'Fallido'], p=[0.75, 0.25])
            xg = None
            parte_cuerpo = np.random.choice(['Pie derecho', 'Pie izquierdo'], p=[0.6, 0.4])
        
        # Avanzar tiempo
        segundo += np.random.randint(5, 45)
        if segundo >= 60:
            minuto += 1
            segundo = segundo % 60
        
        periodo = 1 if minuto < 45 else 2
        
        data.append({
            'EventoID': f'EVT_{i+1:05d}',
            'PartidoID': 'MATCH_001',
            'Tipo': tipo,
            'Minuto': minuto,
            'Segundo': segundo,
            'JugadorID': jugador,
            'Equipo': 'Local',
            'X_Inicio': round(x_ini, 1),
            'Y_Inicio': round(y_ini, 1),
            'X_Fin': round(np.clip(x_fin, 0, 105), 1),
            'Y_Fin': round(np.clip(y_fin, 0, 68), 1),
            'Resultado': resultado,
            'xG': xg,
            'Parte_Cuerpo': parte_cuerpo,
            'Periodo': periodo
        })
    
    return pd.DataFrame(data)


# =============================================================================
# DATASET 5: BIENESTAR (Wellness)
# =============================================================================
def get_bienestar():
    """
    Dataset de cuestionarios de bienestar diarios.
    """
    np.random.seed(42)
    
    jugadores = ['ATL_001', 'ATL_002', 'ATL_003', 'ATL_005', 'ATL_008']
    fechas = pd.date_range('2024-01-01', periods=14, freq='D')
    
    data = []
    for fecha in fechas:
        for jugador in jugadores:
            data.append({
                'Fecha': fecha,
                'JugadorID': jugador,
                'Sueno_Calidad': np.random.randint(1, 6),  # 1-5
                'Sueno_Horas': round(np.random.uniform(6, 9), 1),
                'Fatiga': np.random.randint(1, 6),
                'Estres': np.random.randint(1, 6),
                'Dolor_Muscular': np.random.randint(1, 6),
                'Estado_Animo': np.random.randint(1, 6),
                'HRV_ms': np.random.randint(45, 85)
            })
    
    return pd.DataFrame(data)


# =============================================================================
# FUNCIONES AUXILIARES
# =============================================================================
def print_dataset_info(df, name):
    """Imprime información básica de un dataset."""
    print(f"\n{'='*50}")
    print(f"📊 {name}")
    print(f"{'='*50}")
    print(f"Filas: {len(df):,} | Columnas: {len(df.columns)}")
    print(f"Columnas: {', '.join(df.columns[:8])}...")
    print(df.head(3).to_string())


if __name__ == "__main__":
    # Test de todos los datasets
    print("Cargando datasets...")
    
    atletas = get_atletas()
    print_dataset_info(atletas, "ATLETAS")
    
    gps = get_gps_sesiones()
    print_dataset_info(gps, "GPS SESIONES")
    
    tracking = get_tracking_sample()
    print_dataset_info(tracking, "TRACKING (10Hz)")
    
    eventos = get_eventos()
    print_dataset_info(eventos, "EVENTOS")
    
    bienestar = get_bienestar()
    print_dataset_info(bienestar, "BIENESTAR")
    
    print("\n✅ Todos los datasets cargados correctamente!")
