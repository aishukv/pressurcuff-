from flask import Flask, render_template, request
from logic import generate_pressure_waveform
import matplotlib
matplotlib.use('Agg')  # Avoid tkinter error
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    pressure_level = request.form['pressure']
    speed = request.form['speed']

    t, waveform, systolic_y, diastolic_y = generate_pressure_waveform(pressure_level)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(t, waveform, label="Pressure Waveform")
    if systolic_y:
        ax.axhline(y=systolic_y, color='red', linestyle='--', label='Systolic Threshold')
    if diastolic_y:
        ax.axhline(y=diastolic_y, color='blue', linestyle='--', label='Diastolic Threshold')

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title(f"Simulated Waveform - {pressure_level} Pressure")
    ax.legend()
    ax.grid(True)

    if not os.path.exists("static"):
        os.makedirs("static")
    plt.savefig("static/plot.png")
    plt.close()

    return render_template("result.html", pressure=pressure_level, speed=speed)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=2025)


