from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received alert:", data)

    for alert in data.get('alerts', []):
        labels = alert.get('labels', {})
        annotations = alert.get('annotations', {})

        alertname = labels.get('alertname')
        severity = labels.get('severity')
        summary = annotations.get('summary')
        description = annotations.get('description')

        print(f"Alert: {alertname} | Severity: {severity}")
        print(f"Summary: {summary}")
        print(f"Description: {description}")
    return jsonify({"status": "success"}), 200

app.run(host='0.0.0.0', port=5000)

