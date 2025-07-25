from flask import Flask, jsonify, render_template
import random, time
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Flask app
app = Flask(__name__, static_folder='static')
FlaskInstrumentor().instrument_app(app)

WORDS = [
    {"word": "nebula", "definition": "Interstellar cloud of dust and gas"},
    {"word": "quantum", "definition": "Smallest possible discrete unit"},
    {"word": "echo", "definition": "Sound reflected off a surface"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/random')
def random_word():
    time.sleep(random.uniform(0.2, 1.0))  # simulate latency
    return jsonify(random.choice(WORDS))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
