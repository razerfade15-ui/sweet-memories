html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>For You</title>
  <style>
    body {
      font-family: "Segoe UI", sans-serif;
      background: linear-gradient(135deg, #ffe6f0 0%, #fff5e6 100%);
      color: #4a2d4c;
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      padding: 20px;
    }
    .card {
      width: min(100%, 760px);
      background: rgba(255, 255, 255, 0.9);
      border-radius: 28px;
      box-shadow: 0 20px 50px rgba(0,0,0,.12);
      overflow: hidden;
    }
    .hero {
      padding: 32px;
      text-align: center;
    }
    .hero h1 {
      margin: 0;
      font-size: clamp(2rem, 3.5vw, 3.5rem);
      letter-spacing: 0.02em;
    }
    .hero p {
      margin: 14px auto 0;
      max-width: 520px;
      line-height: 1.7;
      color: #6c435f;
    }
    .slideshow {
      position: relative;
      height: 360px;
      overflow: hidden;
      background: #f8e9f3;
    }
    .slide {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: none;
    }
    .slide.active { display: block; }
    .controls {
      position: absolute;
      inset: 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 12px;
      pointer-events: none;
    }
    .button {
      pointer-events: auto;
      border: none;
      background: rgba(255,255,255,.85);
      color: #843b67;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      font-size: 1.4rem;
      cursor: pointer;
      transition: transform .2s;
    }
    .button:hover { transform: scale(1.05); }
    .media {
      padding: 24px;
      display: grid;
      gap: 18px;
    }
    .note {
      padding: 22px;
      border-radius: 18px;
      background: #fff0f8;
      border: 1px solid #f2d3e2;
      font-family: "Comic Sans MS", "Comic Neue", cursive, sans-serif;
      line-height: 1.8;
      color: #6e3a5e;
      white-space: pre-wrap;
    }
    audio {
      width: 100%;
      border-radius: 12px;
    }
  </style>
</head>
<body>
  <article class="card">
    <section class="hero">
      <h1>For my favorite person</h1>
      <p>Every photo is a memory, every note is love, and this song is our little soundtrack.</p>
    </section>

    <section class="slideshow">
      <img class="slide active" src="photo1.jpg" alt="Memory 1" />
      <img class="slide" src="photo2.jpg" alt="Memory 2" />
      <img class="slide" src="photo3.jpg" alt="Memory 3" />
      <div class="controls">
        <button class="button" id="prev">&lsaquo;</button>
        <button class="button" id="next">&rsaquo;</button>
      </div>
    </section>

    <section class="media">
      <audio controls>
        <source src="favorite-song.mp3" type="audio/mpeg" />
        Your browser does not support audio playback.
      </audio>

      <div class="note">
        Dear love,
        
        I wanted to make something sweet just for you.
        Every day with you feels like the best song.
        
        Love,
        [Your Name]
      </div>
    </section>
  </article>

  <script>
    const slides = document.querySelectorAll('.slide');
    let current = 0;

    function showSlide(index) {
      slides[current].classList.remove('active');
      current = (index + slides.length) % slides.length;
      slides[current].classList.add('active');
    }

    document.getElementById('prev').addEventListener('click', () => showSlide(current - 1));
    document.getElementById('next').addEventListener('click', () => showSlide(current + 1));

    setInterval(() => showSlide(current + 1), 5000);
  </script>
</body>
</html>"""

if __name__ == "__main__":
  print(html)