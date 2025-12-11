import os
from flask import Flask, render_template

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Route utama untuk menampilkan ringkasan dan visualisasi
@app.route("/")
def index():
    # Ringkasan hasil simulasi Monte Carlo (hard-coded)
    summary = {
        "n_sim": 2000,
        "pred_mean": 19347730.79,
        "std_sim": 5758805.52,
        "min_sim": 10648035.50,
        "max_sim": 28641221.19
    }
    return render_template("index.html", summary=summary)

# Menjalankan aplikasi
if __name__ == "__main__":
    # Untuk Railway: gunakan port dari environment variable PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)  # debug=True hanya untuk lokal
