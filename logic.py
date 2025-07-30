import numpy as np

def generate_pressure_waveform(level):
    t = np.linspace(0, 5, 1000)
    base_wave = np.sin(2 * np.pi * 1 * t) * 10

    if level == 'Light':
        waveform = base_wave + 20
        systolic_y, diastolic_y = 25, 15
    elif level == 'Medium':
        waveform = base_wave + 50
        systolic_y, diastolic_y = 55, 45
    elif level == 'Deep':
        waveform = base_wave + 80
        systolic_y, diastolic_y = 85, 75
    else:
        waveform = base_wave
        systolic_y, diastolic_y = None, None

    return t, waveform, systolic_y, diastolic_y

