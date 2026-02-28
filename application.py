from flask import Flask, render_template_string, jsonify
import random
import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vibe Check HQ</title>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Mono:ital@0;1&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #0a0a0f;
            --card: #12121a;
            --accent: #00ff9d;
            --accent2: #ff006e;
            --accent3: #ffd60a;
            --text: #e8e8f0;
            --muted: #555570;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background: var(--bg);
            color: var(--text);
            font-family: 'DM Mono', monospace;
            min-height: 100vh;
            overflow-x: hidden;
        }

        /* Animated background grid */
        body::before {
            content: '';
            position: fixed;
            inset: 0;
            background-image: 
                linear-gradient(rgba(0,255,157,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0,255,157,0.03) 1px, transparent 1px);
            background-size: 40px 40px;
            animation: gridMove 20s linear infinite;
            pointer-events: none;
            z-index: 0;
        }

        @keyframes gridMove {
            0% { transform: translateY(0); }
            100% { transform: translateY(40px); }
        }

        .container {
            position: relative;
            z-index: 1;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        header {
            text-align: center;
            margin-bottom: 60px;
            animation: fadeDown 0.8s ease both;
        }

        @keyframes fadeDown {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 {
            font-family: 'Bebas Neue', sans-serif;
            font-size: clamp(60px, 12vw, 120px);
            letter-spacing: 4px;
            line-height: 1;
            background: linear-gradient(135deg, var(--accent), var(--accent3), var(--accent2));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .subtitle {
            color: var(--muted);
            font-size: 13px;
            letter-spacing: 4px;
            text-transform: uppercase;
            margin-top: 8px;
        }

        /* Vibe Card */
        .vibe-card {
            background: var(--card);
            border: 1px solid rgba(0,255,157,0.15);
            border-radius: 4px;
            padding: 50px 40px;
            text-align: center;
            margin-bottom: 30px;
            position: relative;
            overflow: hidden;
            animation: fadeUp 0.8s ease 0.2s both;
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .vibe-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 2px;
            background: linear-gradient(90deg, var(--accent), var(--accent2));
        }

        .vibe-label {
            font-size: 11px;
            letter-spacing: 5px;
            text-transform: uppercase;
            color: var(--muted);
            margin-bottom: 20px;
        }

        .vibe-emoji {
            font-size: 80px;
            display: block;
            margin-bottom: 20px;
            animation: bounce 2s ease infinite;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .vibe-text {
            font-family: 'Bebas Neue', sans-serif;
            font-size: clamp(30px, 6vw, 55px);
            letter-spacing: 2px;
            color: var(--accent);
            margin-bottom: 10px;
        }

        .vibe-description {
            color: var(--muted);
            font-size: 13px;
            font-style: italic;
            max-width: 400px;
            margin: 0 auto 30px;
            line-height: 1.6;
        }

        .btn {
            background: transparent;
            border: 1px solid var(--accent);
            color: var(--accent);
            font-family: 'DM Mono', monospace;
            font-size: 13px;
            letter-spacing: 3px;
            text-transform: uppercase;
            padding: 14px 40px;
            cursor: pointer;
            transition: all 0.2s ease;
            position: relative;
            overflow: hidden;
        }

        .btn::before {
            content: '';
            position: absolute;
            inset: 0;
            background: var(--accent);
            transform: translateX(-100%);
            transition: transform 0.2s ease;
            z-index: -1;
        }

        .btn:hover::before { transform: translateX(0); }
        .btn:hover { color: var(--bg); }
        .btn:active { transform: scale(0.97); }

        /* Stats row */
        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-bottom: 30px;
            animation: fadeUp 0.8s ease 0.4s both;
        }

        .stat-box {
            background: var(--card);
            border: 1px solid rgba(255,255,255,0.06);
            padding: 24px 16px;
            text-align: center;
            border-radius: 4px;
        }

        .stat-value {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 36px;
            letter-spacing: 2px;
        }

        .stat-value.green { color: var(--accent); }
        .stat-value.pink { color: var(--accent2); }
        .stat-value.yellow { color: var(--accent3); }

        .stat-label {
            font-size: 10px;
            letter-spacing: 3px;
            text-transform: uppercase;
            color: var(--muted);
            margin-top: 4px;
        }

        /* History */
        .history {
            background: var(--card);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 4px;
            padding: 30px;
            animation: fadeUp 0.8s ease 0.6s both;
        }

        .history-title {
            font-size: 11px;
            letter-spacing: 4px;
            text-transform: uppercase;
            color: var(--muted);
            margin-bottom: 20px;
        }

        .history-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .history-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 10px 14px;
            background: rgba(255,255,255,0.02);
            border-radius: 2px;
            font-size: 13px;
            animation: slideIn 0.3s ease both;
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-10px); }
            to { opacity: 1; transform: translateX(0); }
        }

        .history-emoji { font-size: 20px; }
        .history-vibe { color: var(--text); flex: 1; }
        .history-time { color: var(--muted); font-size: 11px; }

        footer {
            text-align: center;
            margin-top: 60px;
            color: var(--muted);
            font-size: 11px;
            letter-spacing: 3px;
            text-transform: uppercase;
            animation: fadeUp 0.8s ease 0.8s both;
        }

        .loading { opacity: 0.5; pointer-events: none; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Vibe Check</h1>
            <p class="subtitle">Powered by Flask &amp; Azure &mdash; Deployed &amp; Dangerous</p>
        </header>

        <div class="vibe-card" id="vibeCard">
            <p class="vibe-label">Today's Vibe</p>
            <span class="vibe-emoji" id="vibeEmoji">✨</span>
            <div class="vibe-text" id="vibeText">Loading...</div>
            <p class="vibe-description" id="vibeDesc">Fetching your cosmic energy...</p>
            <button class="btn" onclick="getVibe()">Check My Vibe</button>
        </div>

        <div class="stats">
            <div class="stat-box">
                <div class="stat-value green" id="checkCount">0</div>
                <div class="stat-label">Vibes Checked</div>
            </div>
            <div class="stat-box">
                <div class="stat-value pink" id="topVibe">—</div>
                <div class="stat-label">Top Vibe</div>
            </div>
            <div class="stat-box">
                <div class="stat-value yellow" id="currentTime">—</div>
                <div class="stat-label">Local Time</div>
            </div>
        </div>

        <div class="history">
            <p class="history-title">// Vibe History</p>
            <ul class="history-list" id="historyList">
                <li class="history-item">
                    <span class="history-emoji">👻</span>
                    <span class="history-vibe">No vibes checked yet...</span>
                    <span class="history-time">—</span>
                </li>
            </ul>
        </div>

        <footer>Running on Azure &bull; Built with Flask &bull; Deployed via GitHub</footer>
    </div>

    <script>
        let checkCount = 0;
        let history = [];
        let vibeCounts = {};

        function updateTime() {
            const now = new Date();
            document.getElementById('currentTime').textContent = 
                now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
        }

        setInterval(updateTime, 1000);
        updateTime();

        async function getVibe() {
            const card = document.getElementById('vibeCard');
            card.classList.add('loading');

            try {
                const res = await fetch('/api/vibe');
                const data = await res.json();

                document.getElementById('vibeEmoji').textContent = data.emoji;
                document.getElementById('vibeText').textContent = data.vibe;
                document.getElementById('vibeDesc').textContent = data.description;

                checkCount++;
                document.getElementById('checkCount').textContent = checkCount;

                vibeCounts[data.vibe] = (vibeCounts[data.vibe] || 0) + 1;
                const topVibe = Object.entries(vibeCounts).sort((a,b) => b[1]-a[1])[0][0];
                document.getElementById('topVibe').textContent = topVibe.split(' ')[0];

                const now = new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
                history.unshift({ emoji: data.emoji, vibe: data.vibe, time: now });
                if (history.length > 5) history.pop();

                const list = document.getElementById('historyList');
                list.innerHTML = history.map(h => `
                    <li class="history-item">
                        <span class="history-emoji">${h.emoji}</span>
                        <span class="history-vibe">${h.vibe}</span>
                        <span class="history-time">${h.time}</span>
                    </li>
                `).join('');

            } catch(e) {
                document.getElementById('vibeText').textContent = 'Error checking vibe';
            }

            card.classList.remove('loading');
        }

        // Load initial vibe
        getVibe();
    </script>
</body>
</html>
"""

VIBES = [
    {
        "vibe": "COSMIC GRINDSET",
        "emoji": "🚀",
        "description": "You're operating at galactic frequencies. Nothing can stop you today."
    },
    {
        "vibe": "CHAOTIC NEUTRAL",
        "emoji": "🌀",
        "description": "Unpredictable, unhinged, and somehow thriving. Classic you."
    },
    {
        "vibe": "SOFT LAUNCH MODE",
        "emoji": "🌸",
        "description": "Taking it easy today. Low key, low stress, high snacks."
    },
    {
        "vibe": "MAIN CHARACTER",
        "emoji": "🎬",
        "description": "The camera is always on you. Own it."
    },
    {
        "vibe": "GOBLIN MODE",
        "emoji": "👺",
        "description": "Feral. Unhinged. Eating snacks in bed. No regrets."
    },
    {
        "vibe": "BIG BRAIN DAY",
        "emoji": "🧠",
        "description": "Neurons firing on all cylinders. Drop everything and code."
    },
    {
        "vibe": "TOUCH GRASS",
        "emoji": "🌿",
        "description": "Step outside. The outside world called. It misses you."
    },
    {
        "vibe": "SIGMA GRINDSET",
        "emoji": "🐺",
        "description": "Lone wolf. Eyes on the prize. No distractions."
    },
    {
        "vibe": "NPC BEHAVIOR",
        "emoji": "🤖",
        "description": "Going through the motions today. That's okay, even NPCs have off days."
    },
    {
        "vibe": "LOCKED IN",
        "emoji": "🔒",
        "description": "Fully focused. Don't text back. Deep work mode activated."
    },
]

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/api/vibe')
def get_vibe():
    vibe = random.choice(VIBES)
    vibe['timestamp'] = datetime.datetime.now().isoformat()
    return jsonify(vibe)

@app.route('/health')
def health():
    return jsonify({"status": "alive", "message": "Vibe Check HQ is running!"})

if __name__ == '__main__':
    app.run(debug=True)
