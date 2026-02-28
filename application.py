from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YOU MUST PLAY REMNANT TODAY</title>
    <link href="https://fonts.googleapis.com/css2?family=Black+Ops+One&family=Share+Tech+Mono&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #0d0a08;
            --red: #c0392b;
            --red-hot: #ff4500;
            --ember: #e67e22;
            --ash: #7f8c8d;
            --ash-light: #bdc3c7;
            --text: #f0e6d3;
            --dark-card: #150f0a;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body {
            background: var(--bg);
            color: var(--text);
            font-family: 'Share Tech Mono', monospace;
            overflow-x: hidden;
            cursor: crosshair;
        }
        body::after {
            content: '';
            position: fixed; inset: 0;
            background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.07) 2px, rgba(0,0,0,0.07) 4px);
            pointer-events: none;
            z-index: 9999;
        }
        #particles { position: fixed; inset: 0; pointer-events: none; z-index: 0; }

        /* HERO */
        .hero {
            min-height: 100vh;
            display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            text-align: center;
            padding: 100px 20px 60px;
            background: radial-gradient(ellipse at center, #2a0a00 0%, #0d0a08 70%);
            position: relative; overflow: hidden; z-index: 1;
        }
        .warning-tape {
            background: repeating-linear-gradient(-45deg, #c0392b, #c0392b 20px, #1a0a00 20px, #1a0a00 40px);
            width: 130%; padding: 12px 0;
            position: absolute; top: 55px;
            font-family: 'Black Ops One', cursive;
            font-size: 13px; letter-spacing: 3px; color: white;
            overflow: hidden; white-space: nowrap;
            box-shadow: 0 4px 20px rgba(192,57,43,0.5);
            transform: rotate(-1.5deg);
        }
        .tape-inner {
            display: inline-block;
            animation: scroll-tape 18s linear infinite;
        }
        @keyframes scroll-tape {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        .hero-eyebrow {
            font-size: 12px; letter-spacing: 6px;
            text-transform: uppercase; color: var(--ember);
            margin-bottom: 20px; position: relative; z-index: 1;
            animation: flicker 4s ease-in-out infinite;
        }
        @keyframes flicker {
            0%,88%,100% { opacity:1; }
            90% { opacity:0.3; }
            93% { opacity:1; }
            96% { opacity:0.2; }
            98% { opacity:1; }
        }
        .hero h1 {
            font-family: 'Black Ops One', cursive;
            font-size: clamp(40px, 9vw, 108px);
            line-height: 0.95;
            color: white;
            text-shadow: 0 0 20px var(--red-hot), 0 0 60px var(--red), 0 0 100px rgba(192,57,43,0.4);
            margin-bottom: 14px;
            position: relative; z-index: 1;
        }
        .hero h1 .line2 { color: var(--red-hot); display: block; }
        .hero-sub {
            font-size: clamp(14px, 2vw, 19px);
            color: var(--ash-light); margin-bottom: 44px;
            max-width: 580px; line-height: 1.7;
            position: relative; z-index: 1;
        }
        .hero-sub strong { color: var(--ember); }

        /* COUNTDOWN */
        .countdown-wrap { margin-bottom: 44px; position: relative; z-index: 1; }
        .countdown-label {
            font-size: 11px; letter-spacing: 5px;
            text-transform: uppercase; color: var(--red); margin-bottom: 12px;
        }
        .countdown { display: flex; gap: 14px; justify-content: center; }
        .count-box {
            background: var(--dark-card);
            border: 1px solid var(--red);
            padding: 16px 18px; min-width: 78px; text-align: center;
            box-shadow: 0 0 20px rgba(192,57,43,0.25), inset 0 0 20px rgba(192,57,43,0.05);
            position: relative; overflow: hidden;
        }
        .count-box::before {
            content: '';
            position: absolute; top:0; left:0; right:0; height:1px;
            background: linear-gradient(90deg, transparent, var(--red), transparent);
            animation: scan-line 2s linear infinite;
        }
        @keyframes scan-line { 0%{transform:translateY(0)} 100%{transform:translateY(80px)} }
        .count-num {
            font-family: 'Black Ops One', cursive;
            font-size: 40px; color: var(--red-hot);
            text-shadow: 0 0 20px var(--red);
            line-height: 1; display: block;
        }
        .count-lbl { font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--ash); margin-top:5px; }

        .hero-cta {
            display: inline-block; background: var(--red);
            color: white; font-family: 'Black Ops One', cursive;
            font-size: 17px; letter-spacing: 3px; padding: 18px 48px;
            text-decoration: none; text-transform: uppercase;
            position: relative; z-index: 1;
            clip-path: polygon(8px 0%, 100% 0%, calc(100% - 8px) 100%, 0% 100%);
            transition: all 0.2s;
            box-shadow: 0 0 30px rgba(192,57,43,0.5);
            animation: pulse-btn 2s ease-in-out infinite;
            cursor: pointer; border: none;
        }
        @keyframes pulse-btn {
            0%,100% { box-shadow: 0 0 30px rgba(192,57,43,0.5); }
            50% { box-shadow: 0 0 60px rgba(255,69,0,0.8), 0 0 100px rgba(192,57,43,0.4); }
        }
        .hero-cta:hover { background: var(--red-hot); transform: scale(1.05); }

        /* SECTIONS */
        section { padding: 80px 40px; position: relative; z-index: 1; }
        .section-label {
            text-align: center; font-size: 11px;
            letter-spacing: 6px; text-transform: uppercase;
            color: var(--red); margin-bottom: 14px;
        }
        .section-title {
            font-family: 'Black Ops One', cursive;
            font-size: clamp(26px, 5vw, 50px);
            text-align: center; color: white; margin-bottom: 10px;
            text-shadow: 0 0 30px rgba(192,57,43,0.4);
        }
        .section-sub {
            text-align: center; color: var(--ash); font-size: 15px;
            max-width: 500px; margin: 0 auto 52px;
        }

        /* EXCUSES */
        .excuses { background: #0f0b09; }
        .excuses-grid {
            display: grid; grid-template-columns: repeat(3,1fr);
            gap: 18px; max-width: 1100px; margin: 0 auto;
        }
        .excuse-card {
            background: var(--dark-card);
            border: 1px solid rgba(192,57,43,0.3);
            padding: 26px 22px; position: relative;
            transition: all 0.3s; overflow: hidden;
        }
        .excuse-card:hover {
            border-color: var(--red);
            transform: translateY(-4px);
            box-shadow: 0 10px 40px rgba(192,57,43,0.2);
        }
        .excuse-card::after {
            content: '✗'; position: absolute;
            top: 10px; right: 14px;
            font-size: 26px; color: var(--red);
            font-family: 'Black Ops One', cursive;
        }
        .excuse-text { font-size: 16px; color: var(--ash-light); margin-bottom: 12px; font-style: italic; line-height: 1.5; }
        .excuse-rebuttal { font-size: 14px; color: var(--ember); line-height: 1.5; }

        /* REASONS */
        .reasons { background: radial-gradient(ellipse at bottom, #1a0800 0%, #0d0a08 60%); }
        .reasons-list { max-width: 880px; margin: 0 auto; }
        .reason-item {
            display: grid; grid-template-columns: 72px 1fr;
            gap: 22px; align-items: start;
            padding: 28px 0;
            border-bottom: 1px solid rgba(192,57,43,0.15);
            transition: padding 0.3s;
        }
        .reason-item:hover { padding-left: 10px; }
        .reason-num {
            font-family: 'Black Ops One', cursive;
            font-size: 48px; color: var(--red); opacity: 0.45;
            line-height: 1; text-shadow: 0 0 20px var(--red);
        }
        .reason-title { font-family: 'Black Ops One', cursive; font-size: 21px; color: white; margin-bottom: 8px; }
        .reason-desc { color: var(--ash-light); font-size: 15px; line-height: 1.7; }
        .reason-desc strong { color: var(--ember); }

        /* THREAT METER */
        .meter-section { background: #0f0b09; text-align: center; }
        .meter-wrapper { max-width: 580px; margin: 36px auto; }
        .meter-bar-bg {
            height: 38px; background: rgba(255,255,255,0.04);
            border: 1px solid var(--red); position: relative;
            overflow: hidden;
            clip-path: polygon(8px 0%, 100% 0%, calc(100% - 8px) 100%, 0% 100%);
        }
        .meter-fill {
            height: 100%; width: 0%;
            background: linear-gradient(90deg, var(--red), var(--red-hot), var(--ember));
            transition: width 2s ease;
            box-shadow: 0 0 20px var(--red-hot);
        }
        .meter-scale {
            display: flex; justify-content: space-between;
            font-size: 11px; color: var(--ash);
            margin-top: 7px; letter-spacing: 2px;
        }
        .meter-verdict {
            font-family: 'Black Ops One', cursive;
            font-size: 24px; color: var(--red-hot);
            margin-top: 22px; text-shadow: 0 0 30px var(--red);
            min-height: 36px;
        }

        /* PEP TALK */
        .generator { background: radial-gradient(ellipse at top, #1a0800 0%, #0d0a08 60%); text-align: center; }
        .gen-btn {
            background: transparent; border: 1px solid var(--ember);
            color: var(--ember); font-family: 'Share Tech Mono', monospace;
            font-size: 13px; letter-spacing: 3px; text-transform: uppercase;
            padding: 14px 34px; cursor: pointer; transition: all 0.2s;
            margin: 28px auto; display: block;
        }
        .gen-btn:hover { background: var(--ember); color: var(--bg); }
        .gen-output {
            max-width: 680px; margin: 0 auto;
            background: var(--dark-card);
            border-left: 3px solid var(--red);
            padding: 22px 26px;
            font-size: 17px; color: var(--text);
            line-height: 1.75; min-height: 80px;
            display: flex; align-items: center; justify-content: center;
            font-style: italic;
            transition: opacity 0.3s;
        }

        /* FINAL CTA */
        .final-cta {
            padding: 100px 40px; text-align: center;
            background: radial-gradient(ellipse at center, #2a0500 0%, #0d0a08 70%);
            overflow: hidden;
        }
        .final-cta h2 {
            font-family: 'Black Ops One', cursive;
            font-size: clamp(34px, 7vw, 78px);
            line-height: 1; color: white;
            text-shadow: 0 0 40px var(--red);
            margin-bottom: 18px;
        }
        .final-cta h2 span { color: var(--red-hot); }
        .final-cta p { color: var(--ash-light); font-size: 17px; max-width: 500px; margin: 0 auto 36px; line-height: 1.7; }
        .big-btn {
            display: inline-block; background: var(--red);
            color: white; font-family: 'Black Ops One', cursive;
            font-size: 20px; letter-spacing: 3px; padding: 22px 56px;
            clip-path: polygon(12px 0%, 100% 0%, calc(100% - 12px) 100%, 0% 100%);
            transition: all 0.2s; cursor: pointer; border: none;
            animation: pulse-btn 1.5s ease-in-out infinite;
        }
        .big-btn:hover { background: var(--red-hot); transform: scale(1.05); }

        footer {
            padding: 28px 40px; text-align: center;
            color: var(--ash); font-size: 13px;
            border-top: 1px solid rgba(192,57,43,0.2);
            background: #0a0807; position: relative; z-index: 1;
        }
        footer span { color: var(--red); }

        @media(max-width:768px){
            .excuses-grid{grid-template-columns:1fr;}
            .reason-item{grid-template-columns:50px 1fr;}
            .countdown{gap:8px;}
            .count-box{min-width:62px;padding:10px 8px;}
        }
    </style>
</head>
<body>
<canvas id="particles"></canvas>

<!-- HERO -->
<section class="hero">
    <div class="warning-tape">
        <div class="tape-inner">
            ⚠ WARNING: ROOT WALKERS DETECTED &nbsp;&nbsp;&nbsp;&nbsp; ⚠ WARNING: ROOT WALKERS DETECTED &nbsp;&nbsp;&nbsp;&nbsp; ⚠ WARNING: ROOT WALKERS DETECTED &nbsp;&nbsp;&nbsp;&nbsp; ⚠ WARNING: ROOT WALKERS DETECTED &nbsp;&nbsp;&nbsp;&nbsp; ⚠ WARNING: ROOT WALKERS DETECTED &nbsp;&nbsp;&nbsp;&nbsp; ⚠ WARNING: ROOT WALKERS DETECTED &nbsp;&nbsp;&nbsp;&nbsp;
        </div>
    </div>

    <p class="hero-eyebrow">📡 Urgent Transmission — Priority Level: MAXIMUM</p>
    <h1>
        YOU NEED TO
        <span class="line2">PLAY REMNANT</span>
        TODAY.
    </h1>
    <p class="hero-sub">
        The Root has returned. The Ward is crumbling. And most importantly —
        <strong>you have absolutely no valid excuse not to play right now.</strong>
        This message is endorsed by the Pan, the Undying King, and your own conscience.
    </p>

    <div class="countdown-wrap">
        <p class="countdown-label">⏱ Time Remaining Until You Should Already Be Playing</p>
        <div class="countdown">
            <div class="count-box">
                <span class="count-num" id="hours">00</span>
                <span class="count-lbl">Hours</span>
            </div>
            <div class="count-box">
                <span class="count-num" id="minutes">00</span>
                <span class="count-lbl">Minutes</span>
            </div>
            <div class="count-box">
                <span class="count-num" id="seconds">00</span>
                <span class="count-lbl">Seconds</span>
            </div>
        </div>
    </div>

    <button class="hero-cta" onclick="document.getElementById('excuses').scrollIntoView({behavior:'smooth'})">
        Read Your Orders ↓
    </button>
</section>

<!-- EXCUSES -->
<section class="excuses" id="excuses">
    <p class="section-label">🚫 Official Excuse Registry</p>
    <h2 class="section-title">Your Excuses Are Invalid</h2>
    <p class="section-sub">Every submitted excuse has been reviewed, assessed, and firmly rejected by a panel of experts.</p>
    <div class="excuses-grid">
        <div class="excuse-card">
            <p class="excuse-text">"I'm too busy today..."</p>
            <p class="excuse-rebuttal">→ You had time to read this website. QED. Boot it up immediately.</p>
        </div>
        <div class="excuse-card">
            <p class="excuse-text">"I'm tired from work."</p>
            <p class="excuse-rebuttal">→ Nothing cures exhaustion like shooting a giant deer-god in the face. Science.</p>
        </div>
        <div class="excuse-card">
            <p class="excuse-text">"I was going to watch TV."</p>
            <p class="excuse-rebuttal">→ Remnant IS TV. With guns. And bosses that will disrespect you personally.</p>
        </div>
        <div class="excuse-card">
            <p class="excuse-text">"I haven't eaten dinner yet."</p>
            <p class="excuse-rebuttal">→ Eat it at the character select screen. Multitask like a true survivor.</p>
        </div>
        <div class="excuse-card">
            <p class="excuse-text">"It's too hard."</p>
            <p class="excuse-rebuttal">→ Dying 14 times to a boss builds character. And healthy rage. Mostly rage.</p>
        </div>
        <div class="excuse-card">
            <p class="excuse-text">"I'll play it tomorrow."</p>
            <p class="excuse-rebuttal">→ Tomorrow is a lie. The Root wins when you procrastinate. Is that what you want?</p>
        </div>
    </div>
</section>

<!-- REASONS -->
<section class="reasons">
    <p class="section-label">📋 Official Briefing</p>
    <h2 class="section-title">Why You Must Play TODAY</h2>
    <p class="section-sub">Intelligence gathered from multiple dimensions confirms the following critical facts:</p>
    <div class="reasons-list">
        <div class="reason-item">
            <div class="reason-num">01</div>
            <div>
                <h3 class="reason-title">The Co-op Is Unmatched</h3>
                <p class="reason-desc">Remnant with a friend turns every boss fight into a beautiful disaster. One of you will be revived <strong>at least 20 times</strong>. This is called bonding. Cherish it.</p>
            </div>
        </div>
        <div class="reason-item">
            <div class="reason-num">02</div>
            <div>
                <h3 class="reason-title">The Bosses Are Genuinely Unhinged</h3>
                <p class="reason-desc">You will fight a giant beetle, an undying king on a massive throne, and a literal god made of wood. <strong>None of this is normal</strong> and it rules completely.</p>
            </div>
        </div>
        <div class="reason-item">
            <div class="reason-num">03</div>
            <div>
                <h3 class="reason-title">The Loot Brain Goes BRRR</h3>
                <p class="reason-desc">New mods. New weapons. Rings. Amulets. Traits. You will spend <strong>30 minutes in the menu</strong> theorycrafting a build and love every single second of it.</p>
            </div>
        </div>
        <div class="reason-item">
            <div class="reason-num">04</div>
            <div>
                <h3 class="reason-title">It Still Slaps in 2025</h3>
                <p class="reason-desc">Remnant 2 exists and is incredible, but the original <strong>holds up beautifully</strong>. Don't disrespect the classic. Respect the roots. (Pun very much intended.)</p>
            </div>
        </div>
        <div class="reason-item">
            <div class="reason-num">05</div>
            <div>
                <h3 class="reason-title">You Will Absolutely Scream At Least Once</h3>
                <p class="reason-desc">Statistically guaranteed. A boss will do something <strong>completely cheap and unfair</strong> and you'll question your life choices. Then you'll beat it and feel like a god.</p>
            </div>
        </div>
    </div>
</section>

<!-- THREAT METER -->
<section class="meter-section">
    <p class="section-label">📊 Situation Assessment</p>
    <h2 class="section-title">Current Urgency Level</h2>
    <div class="meter-wrapper">
        <div class="meter-bar-bg">
            <div class="meter-fill" id="meterFill"></div>
        </div>
        <div class="meter-scale">
            <span>Mild Suggestion</span>
            <span>ABSOLUTE EMERGENCY</span>
        </div>
        <div class="meter-verdict" id="meterVerdict"></div>
    </div>
    <p style="color:var(--ash);font-size:14px;max-width:480px;margin:0 auto;">Threat level calculated using: time of day, Root activity index, your excuse inventory, and pure vibes.</p>
</section>

<!-- PEP TALK GENERATOR -->
<section class="generator">
    <p class="section-label">🎲 Motivational Unit</p>
    <h2 class="section-title">Generate Your Pep Talk</h2>
    <p class="section-sub">Press the button. Receive wisdom. Stop stalling.</p>
    <button class="gen-btn" onclick="generatePep()">⚡ GENERATE MOTIVATION</button>
    <div class="gen-output" id="genOutput">
        Awaiting your command, Traveler...
    </div>
</section>

<!-- FINAL CTA -->
<section class="final-cta">
    <h2>STOP READING.<br><span>START PLAYING.</span></h2>
    <p>You've read the briefing. You know the stakes. The Root isn't going to shoot itself. Put down your phone, open Steam, and launch Remnant: From the Ashes. Right now. Do it.</p>
    <button class="big-btn" onclick="launchGame()">🎮 I'M LAUNCHING IT NOW</button>
    <p style="color:var(--ash);font-size:13px;margin-top:18px;">(clicking this won't actually launch the game. but your honor is now on the line.)</p>
</section>

<footer>
    <p>This public service announcement was brought to you by <span>someone who wants you to have fun</span>.<br>
    Remnant: From the Ashes is made by Gunfire Games. Go play it. Right now. Seriously.</p>
</footer>

<script>
// EMBER PARTICLES
const canvas = document.getElementById('particles');
const ctx = canvas.getContext('2d');
function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

const embers = Array.from({length:55}, () => ({
    x: Math.random() * window.innerWidth,
    y: Math.random() * window.innerHeight + window.innerHeight,
    vx: (Math.random()-0.5)*0.8,
    vy: -(Math.random()*1.5+0.5),
    size: Math.random()*3+1,
    opacity: Math.random()*0.5+0.2,
    color: Math.random()>0.5?'#ff4500':'#e67e22'
}));

(function animateEmbers() {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    embers.forEach(e => {
        e.x += e.vx; e.y += e.vy; e.opacity -= 0.002;
        if(e.y < -10 || e.opacity <= 0) {
            e.y = canvas.height+10;
            e.x = Math.random()*canvas.width;
            e.opacity = Math.random()*0.5+0.2;
        }
        ctx.beginPath();
        ctx.arc(e.x,e.y,e.size,0,Math.PI*2);
        ctx.fillStyle = e.color;
        ctx.globalAlpha = e.opacity;
        ctx.fill();
    });
    ctx.globalAlpha = 1;
    requestAnimationFrame(animateEmbers);
})();

// COUNTDOWN to midnight
function updateCountdown() {
    const now = new Date();
    const midnight = new Date(); midnight.setHours(23,59,59,0);
    const diff = midnight - now;
    if(diff <= 0) { document.getElementById('hours').textContent='00'; document.getElementById('minutes').textContent='00'; document.getElementById('seconds').textContent='00'; return; }
    const h=Math.floor(diff/3600000), m=Math.floor((diff%3600000)/60000), s=Math.floor((diff%60000)/1000);
    document.getElementById('hours').textContent=String(h).padStart(2,'0');
    document.getElementById('minutes').textContent=String(m).padStart(2,'0');
    document.getElementById('seconds').textContent=String(s).padStart(2,'0');
}
setInterval(updateCountdown,1000); updateCountdown();

// THREAT METER
const h = new Date().getHours();
let level, verdict;
if(h>=6&&h<12){level=55;verdict="MORNING WINDOW OPEN — GREAT WARM-UP TIME";}
else if(h>=12&&h<17){level=74;verdict="AFTERNOON CONFIRMED — PRIME GAMING HOURS";}
else if(h>=17&&h<21){level=96;verdict="🔴 PEAK WINDOW — ZERO EXCUSES ACCEPTED";}
else{level=88;verdict="LATE NIGHT MODE — ONE MORE RUN ALWAYS APPLIES";}
setTimeout(()=>{
    document.getElementById('meterFill').style.width=level+'%';
    document.getElementById('meterVerdict').textContent=verdict;
},600);

// PEP TALKS
const pepTalks = [
    "Listen. The Root doesn't take days off. Why should you? Boot up the game, grab your rifle, and remind those tree monsters who runs this planet. That's you. You run this planet.",
    "Somewhere out there, a boss just dropped a sick weapon mod with YOUR name on it. It's just sitting there. You're not going to find it scrolling social media, are you? Didn't think so.",
    "You've survived Mondays, awful commutes, and pointless meetings. You can survive the Undying King. Probably. The point is you have to try. The Ward needs you.",
    "Your character is just standing in Ward 13 staring at the wall waiting for you. They're not mad, they're just... disappointed. Don't disappoint your character.",
    "Every minute you don't play Remnant, a Root Walker gains confidence. Is that what you want? Confident Root Walkers strutting around? Absolutely not. Get in there.",
    "People who are playing Remnant right now are having MORE fun than you. This is a verified fact. The study was conducted by me, personally, being very jealous. The data is clear.",
    "You know what feels better than finishing a Netflix episode? Beating a boss that's been humiliating you for 45 minutes. It's not even close. Go experience it immediately.",
    "Imagine your future self looking back on today. Do they say 'I'm glad I did nothing'? No. They say 'I wish I'd played more Remnant.' Don't let future you down. They've been through enough.",
];
function generatePep(){
    const out=document.getElementById('genOutput');
    out.style.opacity='0';
    setTimeout(()=>{out.textContent=pepTalks[Math.floor(Math.random()*pepTalks.length)];out.style.opacity='1';},280);
}

// LAUNCH
const responses=["GODSPEED, TRAVELER. 🎮","THE ROOT FEARS YOU. GO.","WE ARE SO PROUD OF YOU.","FINALLY. THE WARD REJOICES.","HONOR CONFIRMED. 🔥","THE UNDYING KING IS SHAKING."];
function launchGame(){ alert(responses[Math.floor(Math.random()*responses.length)]); }
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return jsonify({"status": "online", "mission": "get your friend to play Remnant"})

if __name__ == '__main__':
    app.run(debug=True)
