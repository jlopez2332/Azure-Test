from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Border Collie World</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=Crimson+Pro:ital,wght@0,300;0,400;0,600;1,300;1,400&display=swap" rel="stylesheet">
    <style>
        :root {
            --cream: #f7f3ec;
            --warm-white: #fdfaf5;
            --bark: #5c3d2e;
            --bark-light: #8b6352;
            --grass: #2d5016;
            --grass-light: #4a7c28;
            --grass-muted: #7aad4e;
            --sky: #c8dde8;
            --gold: #c9922a;
            --gold-light: #e8b84b;
            --text: #2a1f15;
            --text-muted: #7a6355;
            --border: rgba(92,61,46,0.15);
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body {
            background: var(--cream);
            color: var(--text);
            font-family: 'Crimson Pro', Georgia, serif;
            font-size: 18px;
            line-height: 1.7;
            overflow-x: hidden;
        }
        nav {
            position: fixed;
            top: 0; left: 0; right: 0;
            z-index: 100;
            padding: 18px 40px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(247,243,236,0.94);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border);
        }
        .nav-logo {
            font-family: 'Playfair Display', serif;
            font-size: 22px;
            font-weight: 900;
            color: var(--bark);
        }
        .nav-logo span { color: var(--grass); }
        .nav-links { display: flex; gap: 36px; list-style: none; }
        .nav-links a {
            text-decoration: none;
            color: var(--text-muted);
            font-size: 14px;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            font-weight: 600;
            transition: color 0.2s;
        }
        .nav-links a:hover { color: var(--grass); }

        /* HERO */
        .hero {
            min-height: 100vh;
            display: grid;
            grid-template-columns: 1fr 1fr;
            padding-top: 70px;
        }
        .hero-left {
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 80px 60px 80px 80px;
            background: var(--warm-white);
            animation: fadeLeft 1s ease both;
        }
        @keyframes fadeLeft {
            from { opacity: 0; transform: translateX(-40px); }
            to { opacity: 1; transform: translateX(0); }
        }
        .hero-tag {
            font-size: 12px;
            letter-spacing: 4px;
            text-transform: uppercase;
            color: var(--grass-muted);
            font-weight: 600;
            margin-bottom: 24px;
        }
        .hero h1 {
            font-family: 'Playfair Display', serif;
            font-size: clamp(48px, 5vw, 76px);
            font-weight: 900;
            line-height: 1.05;
            color: var(--bark);
            margin-bottom: 24px;
        }
        .hero h1 em { font-style: italic; color: var(--grass); }
        .hero-desc {
            color: var(--text-muted);
            font-size: 19px;
            font-weight: 300;
            max-width: 420px;
            margin-bottom: 40px;
            line-height: 1.8;
        }
        .hero-btns { display: flex; gap: 16px; flex-wrap: wrap; }
        .btn-primary {
            background: var(--grass);
            color: white;
            padding: 14px 36px;
            text-decoration: none;
            font-size: 16px;
            font-weight: 600;
            letter-spacing: 1px;
            transition: all 0.2s;
            display: inline-block;
        }
        .btn-primary:hover { background: var(--grass-light); transform: translateY(-2px); }
        .btn-outline {
            border: 1.5px solid var(--bark-light);
            color: var(--bark);
            padding: 14px 36px;
            text-decoration: none;
            font-size: 16px;
            font-weight: 600;
            letter-spacing: 1px;
            transition: all 0.2s;
            display: inline-block;
        }
        .btn-outline:hover { background: var(--bark); color: white; }
        .hero-right {
            position: relative;
            background: var(--grass);
            overflow: hidden;
            animation: fadeRight 1s ease 0.2s both;
        }
        @keyframes fadeRight {
            from { opacity: 0; transform: translateX(40px); }
            to { opacity: 1; transform: translateX(0); }
        }
        .hero-right img {
            width: 100%; height: 100%;
            object-fit: cover;
            opacity: 0.85;
            mix-blend-mode: multiply;
        }
        .hero-stats-bar {
            position: absolute;
            bottom: 0; left: 0; right: 0;
            background: rgba(247,243,236,0.94);
            padding: 24px 32px;
            display: flex;
            gap: 40px;
            border-top: 3px solid var(--gold);
        }
        .stat-num {
            font-family: 'Playfair Display', serif;
            font-size: 32px;
            font-weight: 900;
            color: var(--bark);
            line-height: 1;
        }
        .stat-lbl {
            font-size: 11px;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: var(--text-muted);
            margin-top: 4px;
        }

        /* SECTIONS */
        section { padding: 100px 80px; }
        .section-header { text-align: center; margin-bottom: 64px; }
        .section-tag {
            font-size: 12px;
            letter-spacing: 4px;
            text-transform: uppercase;
            color: var(--grass-muted);
            font-weight: 600;
            margin-bottom: 14px;
        }
        .section-header h2 {
            font-family: 'Playfair Display', serif;
            font-size: clamp(34px, 4vw, 54px);
            font-weight: 900;
            color: var(--bark);
            line-height: 1.1;
        }
        .section-header p {
            color: var(--text-muted);
            font-size: 19px;
            font-weight: 300;
            max-width: 560px;
            margin: 14px auto 0;
        }

        /* ABOUT */
        .about { background: var(--warm-white); }
        .about-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 80px;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
        }
        .about-image-stack { position: relative; height: 500px; }
        .about-img-main {
            position: absolute;
            top: 0; left: 0;
            width: 74%; height: 84%;
            object-fit: cover;
            box-shadow: 20px 20px 60px rgba(0,0,0,0.15);
        }
        .about-img-accent {
            position: absolute;
            bottom: 0; right: 0;
            width: 54%; height: 52%;
            object-fit: cover;
            border: 6px solid var(--cream);
            box-shadow: 10px 10px 40px rgba(0,0,0,0.12);
        }
        .about-badge {
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            background: var(--gold);
            color: white;
            width: 88px; height: 88px;
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-family: 'Playfair Display', serif;
            font-size: 11px;
            font-weight: 700;
            text-align: center;
            letter-spacing: 1px;
            text-transform: uppercase;
            box-shadow: 0 8px 30px rgba(201,146,42,0.4);
            z-index: 2;
        }
        .about-content h2 {
            font-family: 'Playfair Display', serif;
            font-size: 40px;
            font-weight: 900;
            color: var(--bark);
            line-height: 1.15;
            margin-bottom: 22px;
        }
        .about-content h2 em { font-style: italic; color: var(--grass); }
        .about-content p { color: var(--text-muted); font-weight: 300; margin-bottom: 18px; }
        .trait-list {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-top: 28px;
            list-style: none;
        }
        .trait-list li {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 15px;
            font-weight: 600;
        }
        .trait-list li::before { content: '✦'; color: var(--gold); font-size: 12px; }

        /* GALLERY */
        .gallery { background: var(--cream); }
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-template-rows: 280px 280px;
            gap: 14px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .gallery-item { overflow: hidden; position: relative; cursor: pointer; }
        .gallery-item:first-child { grid-column: span 2; grid-row: span 2; }
        .gallery-item img {
            width: 100%; height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
            display: block;
        }
        .gallery-item:hover img { transform: scale(1.06); }
        .gallery-overlay {
            position: absolute; inset: 0;
            background: linear-gradient(to top, rgba(45,80,22,0.75) 0%, transparent 55%);
            opacity: 0;
            transition: opacity 0.3s;
            display: flex;
            align-items: flex-end;
            padding: 20px;
        }
        .gallery-item:hover .gallery-overlay { opacity: 1; }
        .gallery-label {
            color: white;
            font-family: 'Playfair Display', serif;
            font-size: 18px;
            font-style: italic;
        }

        /* VIDEOS */
        .videos { background: var(--bark); }
        .videos .section-tag { color: var(--gold-light); }
        .videos .section-header h2 { color: white; }
        .videos .section-header p { color: rgba(255,255,255,0.55); }
        .videos-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .video-card {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
            overflow: hidden;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .video-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 20px 50px rgba(0,0,0,0.35);
        }
        .video-thumb { position: relative; aspect-ratio: 16/9; }
        .video-thumb iframe { width: 100%; height: 100%; border: none; display: block; }
        .video-info { padding: 20px 24px; }
        .video-category {
            font-size: 11px;
            letter-spacing: 3px;
            text-transform: uppercase;
            color: var(--gold-light);
            font-weight: 600;
            margin-bottom: 6px;
        }
        .video-title {
            font-family: 'Playfair Display', serif;
            font-size: 20px;
            font-weight: 700;
            color: white;
            line-height: 1.3;
            margin-bottom: 8px;
        }
        .video-desc { font-size: 15px; color: rgba(255,255,255,0.5); font-weight: 300; }

        /* PRODUCTS */
        .products { background: var(--warm-white); }
        .products-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 24px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .product-card {
            background: white;
            border: 1px solid var(--border);
            overflow: hidden;
            transition: all 0.3s;
            position: relative;
        }
        .product-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 16px 40px rgba(0,0,0,0.1);
            border-color: var(--grass-muted);
        }
        .product-badge {
            position: absolute;
            top: 12px; left: 12px;
            background: var(--gold);
            color: white;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            padding: 4px 10px;
            z-index: 1;
        }
        .product-img { width: 100%; aspect-ratio: 1; object-fit: cover; display: block; }
        .product-info { padding: 20px; }
        .product-category {
            font-size: 11px;
            letter-spacing: 3px;
            text-transform: uppercase;
            color: var(--grass-muted);
            font-weight: 600;
            margin-bottom: 6px;
        }
        .product-name {
            font-family: 'Playfair Display', serif;
            font-size: 18px;
            font-weight: 700;
            color: var(--bark);
            margin-bottom: 6px;
            line-height: 1.3;
        }
        .stars { color: var(--gold); font-size: 13px; margin-bottom: 8px; }
        .product-desc { font-size: 14px; color: var(--text-muted); font-weight: 300; margin-bottom: 16px; line-height: 1.5; }
        .product-footer { display: flex; align-items: center; justify-content: space-between; }
        .product-price {
            font-family: 'Playfair Display', serif;
            font-size: 22px;
            font-weight: 900;
            color: var(--bark);
        }
        .product-buy {
            background: var(--grass);
            color: white;
            border: none;
            padding: 8px 18px;
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 1px;
            cursor: pointer;
            transition: background 0.2s;
            text-decoration: none;
            display: inline-block;
        }
        .product-buy:hover { background: var(--grass-light); }

        /* TIPS */
        .tips { background: var(--cream); }
        .tips-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 28px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .tip-card {
            padding: 36px;
            border: 1px solid var(--border);
            background: var(--warm-white);
            position: relative;
            transition: all 0.3s;
        }
        .tip-card:hover {
            border-color: var(--grass-muted);
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0,0,0,0.08);
        }
        .tip-number {
            font-family: 'Playfair Display', serif;
            font-size: 70px;
            font-weight: 900;
            color: rgba(45,80,22,0.07);
            position: absolute;
            top: 12px; right: 18px;
            line-height: 1;
        }
        .tip-icon { font-size: 30px; margin-bottom: 14px; display: block; }
        .tip-title {
            font-family: 'Playfair Display', serif;
            font-size: 21px;
            font-weight: 700;
            color: var(--bark);
            margin-bottom: 10px;
        }
        .tip-desc { color: var(--text-muted); font-size: 16px; font-weight: 300; line-height: 1.7; }

        /* FOOTER */
        footer {
            background: var(--text);
            color: rgba(255,255,255,0.5);
            padding: 60px 80px;
            text-align: center;
        }
        .footer-logo {
            font-family: 'Playfair Display', serif;
            font-size: 28px;
            font-weight: 900;
            color: white;
            margin-bottom: 14px;
        }
        .footer-logo span { color: var(--grass-muted); }
        footer p { font-size: 15px; max-width: 500px; margin: 0 auto; line-height: 1.7; }
        footer a { color: var(--gold-light); text-decoration: none; }
        .footer-divider {
            border: none;
            border-top: 1px solid rgba(255,255,255,0.1);
            margin: 28px auto;
            max-width: 400px;
        }

        /* REVEAL */
        .reveal {
            opacity: 0;
            transform: translateY(28px);
            transition: opacity 0.7s ease, transform 0.7s ease;
        }
        .reveal.visible { opacity: 1; transform: translateY(0); }

        @media (max-width: 900px) {
            nav { padding: 14px 20px; }
            .nav-links { display: none; }
            section { padding: 60px 20px; }
            .hero { grid-template-columns: 1fr; }
            .hero-right { display: none; }
            .hero-left { padding: 50px 20px; }
            .about-grid, .about-image-stack { grid-template-columns: 1fr; height: 300px; }
            .gallery-grid { grid-template-columns: 1fr 1fr; grid-template-rows: auto; }
            .gallery-item:first-child { grid-column: span 2; }
            .videos-grid { grid-template-columns: 1fr; }
            .products-grid { grid-template-columns: 1fr 1fr; }
            .tips-grid { grid-template-columns: 1fr; }
            footer { padding: 40px 20px; }
        }
    </style>
</head>
<body>

<nav>
    <div class="nav-logo">Border<span>Collie</span>World</div>
    <ul class="nav-links">
        <li><a href="#about">About</a></li>
        <li><a href="#gallery">Gallery</a></li>
        <li><a href="#training">Training</a></li>
        <li><a href="#products">Products</a></li>
        <li><a href="#tips">Tips</a></li>
    </ul>
</nav>

<!-- HERO -->
<div class="hero">
    <div class="hero-left">
        <p class="hero-tag">🐾 The World's Most Intelligent Dog</p>
        <h1>Born to<br><em>Run, Herd</em><br>& Shine.</h1>
        <p class="hero-desc">Your complete guide to Border Collies — training tips, stunning photos, expert videos, and the best gear for your brilliant companion.</p>
        <div class="hero-btns">
            <a href="#training" class="btn-primary">Watch Training Videos</a>
            <a href="#products" class="btn-outline">Shop Gear</a>
        </div>
    </div>
    <div class="hero-right">
        <img src="https://images.unsplash.com/photo-1503256207526-0d5d80fa2f47?w=900&q=80" alt="Border Collie running in field">
        <div class="hero-stats-bar">
            <div>
                <div class="stat-num">#1</div>
                <div class="stat-lbl">Intelligence Rank</div>
            </div>
            <div>
                <div class="stat-num">30mph</div>
                <div class="stat-lbl">Top Speed</div>
            </div>
            <div>
                <div class="stat-num">15 yrs</div>
                <div class="stat-lbl">Avg Lifespan</div>
            </div>
        </div>
    </div>
</div>

<!-- ABOUT -->
<section class="about" id="about">
    <div class="about-grid">
        <div class="about-image-stack reveal">
            <img class="about-img-main" src="https://images.unsplash.com/photo-1589941013453-ec89f33b5e95?w=700&q=80" alt="Border Collie portrait">
            <img class="about-img-accent" src="https://images.unsplash.com/photo-1558788353-f76d92427f16?w=500&q=80" alt="Border Collie puppy">
            <div class="about-badge">Rank<br>#1<br>Smart</div>
        </div>
        <div class="about-content reveal">
            <h2>The <em>Einsteins</em><br>of the Dog World</h2>
            <p>Border Collies originated in the border regions of Scotland and England, bred to herd sheep across rugged highlands. Their intense focus, remarkable agility, and extraordinary intelligence make them unlike any other breed.</p>
            <p>Ranked the most intelligent dog breed by Dr. Stanley Coren, Border Collies can learn a new command in under five repetitions and obey it 95% of the time. They thrive when given both physical and mental challenges every single day.</p>
            <ul class="trait-list">
                <li>Exceptional intelligence</li>
                <li>High energy levels</li>
                <li>Strong herding instinct</li>
                <li>Extremely loyal</li>
                <li>Highly trainable</li>
                <li>Agility champions</li>
                <li>Scottish & English origins</li>
                <li>Long lifespan</li>
            </ul>
        </div>
    </div>
</section>

<!-- GALLERY -->
<section class="gallery" id="gallery">
    <div class="section-header reveal">
        <p class="section-tag">📸 Photo Gallery</p>
        <h2>Stunning Border Collies</h2>
        <p>A visual celebration of one of nature's most beautiful and athletic working dogs.</p>
    </div>
    <div class="gallery-grid reveal">
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1472491235688-bdc81a63246e?w=900&q=80" alt="Border Collie in open field">
            <div class="gallery-overlay"><span class="gallery-label">In the Open Field</span></div>
        </div>
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=600&q=80" alt="Border Collie close up">
            <div class="gallery-overlay"><span class="gallery-label">The Famous Stare</span></div>
        </div>
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=600&q=80" alt="Dogs running together">
            <div class="gallery-overlay"><span class="gallery-label">Born to Run</span></div>
        </div>
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1583511655826-05700d52f4d9?w=600&q=80" alt="Border Collie puppy">
            <div class="gallery-overlay"><span class="gallery-label">Puppy Days</span></div>
        </div>
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1601979031925-424e53b6caaa?w=600&q=80" alt="Border Collie playing">
            <div class="gallery-overlay"><span class="gallery-label">Always Playtime</span></div>
        </div>
    </div>
</section>

<!-- TRAINING VIDEOS -->
<section class="videos" id="training">
    <div class="section-header reveal">
        <p class="section-tag">🎬 Training Videos</p>
        <h2 style="color:white;">Learn From the Experts</h2>
        <p>Hand-picked training videos covering everything from basic obedience to advanced agility and herding.</p>
    </div>
    <div class="videos-grid reveal">
        <div class="video-card">
            <div class="video-thumb">
                <iframe src="https://www.youtube.com/embed/gGC8ZqJJBo4"
                    title="Border Collie Basic Training"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen></iframe>
            </div>
            <div class="video-info">
                <p class="video-category">Beginner</p>
                <h3 class="video-title">Basic Obedience Training</h3>
                <p class="video-desc">Sit, stay, come — master the essential commands every Border Collie should know from day one.</p>
            </div>
        </div>
        <div class="video-card">
            <div class="video-thumb">
                <iframe src="https://www.youtube.com/embed/29Q0aYQfGkQ"
                    title="Border Collie Agility Training"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen></iframe>
            </div>
            <div class="video-info">
                <p class="video-category">Intermediate</p>
                <h3 class="video-title">Agility Course Training</h3>
                <p class="video-desc">Channel your Border Collie's boundless energy into agility — the sport they were born for.</p>
            </div>
        </div>
        <div class="video-card">
            <div class="video-thumb">
                <iframe src="https://www.youtube.com/embed/VEbSRhMW6l0"
                    title="Border Collie Advanced Tricks"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen></iframe>
            </div>
            <div class="video-info">
                <p class="video-category">Advanced</p>
                <h3 class="video-title">Herding Instinct & Tricks</h3>
                <p class="video-desc">Tap into their natural herding instincts with structured advanced training and trick sessions.</p>
            </div>
        </div>
    </div>
</section>

<!-- PRODUCTS -->
<section class="products" id="products">
    <div class="section-header reveal">
        <p class="section-tag">🛒 Recommended Products</p>
        <h2>Gear for Active Dogs</h2>
        <p>The best equipment chosen specifically for the high energy and sharp intelligence of Border Collies.</p>
    </div>
    <div class="products-grid reveal">
        <div class="product-card">
            <div class="product-badge">Best Seller</div>
            <img class="product-img" src="https://images.unsplash.com/photo-1601758124510-52d02ddb7cbd?w=400&q=80" alt="Dog frisbee toy">
            <div class="product-info">
                <p class="product-category">Fetch & Play</p>
                <h3 class="product-name">Pro Disc Frisbee</h3>
                <div class="stars">★★★★★</div>
                <p class="product-desc">Soft-edge flying disc designed for high-speed fetch. Easy on the mouth, tough enough for daily use.</p>
                <div class="product-footer">
                    <span class="product-price">$18</span>
                    <a href="https://www.amazon.com/s?k=dog+frisbee+border+collie" target="_blank" class="product-buy">Shop Now</a>
                </div>
            </div>
        </div>
        <div class="product-card">
            <img class="product-img" src="https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?w=400&q=80" alt="Dog puzzle toy">
            <div class="product-info">
                <p class="product-category">Mental Stimulation</p>
                <h3 class="product-name">IQ Puzzle Feeder</h3>
                <div class="stars">★★★★★</div>
                <p class="product-desc">Challenge their genius mind with this Level 3 puzzle feeder. Keeps them busy and mentally sharp.</p>
                <div class="product-footer">
                    <span class="product-price">$34</span>
                    <a href="https://www.amazon.com/s?k=dog+puzzle+feeder+advanced" target="_blank" class="product-buy">Shop Now</a>
                </div>
            </div>
        </div>
        <div class="product-card">
            <div class="product-badge">Top Rated</div>
            <img class="product-img" src="https://images.unsplash.com/photo-1559715745-e1b33a271c8f?w=400&q=80" alt="Dog harness">
            <div class="product-info">
                <p class="product-category">Walking & Running</p>
                <h3 class="product-name">No-Pull Harness</h3>
                <div class="stars">★★★★☆</div>
                <p class="product-desc">Ergonomic design with front clip for better control on high-energy walks and trail runs.</p>
                <div class="product-footer">
                    <span class="product-price">$42</span>
                    <a href="https://www.amazon.com/s?k=no+pull+dog+harness" target="_blank" class="product-buy">Shop Now</a>
                </div>
            </div>
        </div>
        <div class="product-card">
            <img class="product-img" src="https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400&q=80" alt="Agility training set">
            <div class="product-info">
                <p class="product-category">Agility Training</p>
                <h3 class="product-name">Agility Starter Kit</h3>
                <div class="stars">★★★★★</div>
                <p class="product-desc">Tunnels, weave poles, and jumps — everything you need to start agility training at home.</p>
                <div class="product-footer">
                    <span class="product-price">$89</span>
                    <a href="https://www.amazon.com/s?k=dog+agility+training+kit" target="_blank" class="product-buy">Shop Now</a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- TIPS -->
<section class="tips" id="tips">
    <div class="section-header reveal">
        <p class="section-tag">💡 Owner Tips</p>
        <h2>Raising a Happy Border Collie</h2>
        <p>Essential advice for living with the world's smartest, most energetic, and most rewarding dog breed.</p>
    </div>
    <div class="tips-grid reveal">
        <div class="tip-card">
            <span class="tip-number">01</span>
            <span class="tip-icon">🏃</span>
            <h3 class="tip-title">Exercise Daily — A Lot</h3>
            <p class="tip-desc">Border Collies need at least 2 hours of vigorous exercise per day. Running, fetch, swimming, and agility keep them happy and prevent destructive behavior at home.</p>
        </div>
        <div class="tip-card">
            <span class="tip-number">02</span>
            <span class="tip-icon">🧩</span>
            <h3 class="tip-title">Challenge Their Mind</h3>
            <p class="tip-desc">Physical exercise alone isn't enough. Use puzzle feeders, teach new tricks weekly, and engage in scent work or herding games. A bored Border Collie is a destructive one.</p>
        </div>
        <div class="tip-card">
            <span class="tip-number">03</span>
            <span class="tip-icon">🎓</span>
            <h3 class="tip-title">Start Training Early</h3>
            <p class="tip-desc">Begin obedience training from 8 weeks old. They pick up commands incredibly fast — which means good habits and bad habits form equally quickly. Consistency is everything.</p>
        </div>
        <div class="tip-card">
            <span class="tip-number">04</span>
            <span class="tip-icon">🐑</span>
            <h3 class="tip-title">Manage the Herding Instinct</h3>
            <p class="tip-desc">They may try to herd children, cars, or other pets. Redirect this instinct into structured activities like herding sports rather than trying to eliminate it entirely.</p>
        </div>
        <div class="tip-card">
            <span class="tip-number">05</span>
            <span class="tip-icon">❤️</span>
            <h3 class="tip-title">Socialize Widely</h3>
            <p class="tip-desc">Expose puppies to different people, dogs, sounds, and environments early. Border Collies can be reserved and sensitive — early socialization builds a confident adult dog.</p>
        </div>
        <div class="tip-card">
            <span class="tip-number">06</span>
            <span class="tip-icon">🍗</span>
            <h3 class="tip-title">Feed for Performance</h3>
            <p class="tip-desc">Their high activity level demands quality nutrition. Look for high-protein formulas designed for active breeds. Monitor weight closely — they burn a lot but can also overeat.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer>
    <div class="footer-logo">Border<span>Collie</span>World</div>
    <p>Your ultimate resource for Border Collie care, training, and lifestyle. Built with love for the world's most remarkable dogs.</p>
    <hr class="footer-divider">
    <p style="font-size:13px; letter-spacing:1px;">Made with Flask &middot; Deployed on Azure &middot; Photos via <a href="https://unsplash.com" target="_blank">Unsplash</a></p>
</footer>

<script>
    const reveals = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, i) => {
            if (entry.isIntersecting) {
                setTimeout(() => entry.target.classList.add('visible'), i * 120);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.08 });
    reveals.forEach(el => observer.observe(el));

    const sections = document.querySelectorAll('section[id], div.hero');
    const navLinks = document.querySelectorAll('.nav-links a');
    window.addEventListener('scroll', () => {
        let current = '';
        document.querySelectorAll('[id]').forEach(s => {
            if (window.scrollY >= s.offsetTop - 130) current = s.id;
        });
        navLinks.forEach(link => {
            link.style.color = link.getAttribute('href') === '#' + current ? 'var(--grass)' : '';
        });
    });
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return {"status": "ok", "app": "Border Collie World"}

if __name__ == '__main__':
    app.run(debug=True)
