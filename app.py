import os
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# State
bot_state = {
    "is_running": False,
    "paper_trading": True,
    "logs": ["Bot initialized successfully."],
    "stats": {
        "trades": 0,
        "profit_sda": 0.0,
        "active_pairs": ["TRL/SDA", "REGS/SDA"]
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Sidra Auto Arbitrage Bot</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; background: #0f172a; color: #f8fafc; padding: 20px; }
        .card { background: #1e293b; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        .btn { padding: 12px 24px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; }
        .btn-start { background: #22c55e; color: white; }
        .btn-stop { background: #ef4444; color: white; }
        .status { font-size: 18px; margin-bottom: 15px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Sidra DEX Auto-Arbitrage Bot</h2>
        <div class="status">Status: <strong>{{ "RUNNING" if state.is_running else "STOPPED" }}</strong></div>
        <form method="POST" action="/toggle">
            <button class="btn {{ 'btn-stop' if state.is_running else 'btn-start' }}">
                {{ "SAYAR / TSAIDA (STOP)" if state.is_running else "FARA (START BOT)" }}
            </button>
        </form>
    </div>
    <div class="card">
        <h3>Dashboard Stats</h3>
        <p>Total Trades: <strong>{{ state.stats.trades }}</strong></p>
        <p>Total Profit: <strong>{{ state.stats.profit_sda }} SDA</strong></p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, state=bot_state)

@app.route('/toggle', methods=['POST'])
def toggle_bot():
    bot_state["is_running"] = not bot_state["is_running"]
    status_msg = "Bot Started" if bot_state["is_running"] else "Bot Stopped"
    bot_state["logs"].append(status_msg)
    return render_template_string(HTML_TEMPLATE, state=bot_state)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
  
