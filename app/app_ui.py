import tkinter as tk
from tkinter import ttk, messagebox
import joblib

VECTOR_PATH = "vectorizer.pkl"

MODEL_PATHS = {
    "Logistic Regression": "LogisticRegression.pkl",
    "Random Forest": "RandomForestClassifier.pkl",
    "Decision Tree": "DecisionTreeClassifier.pkl",
}

vectorizer = joblib.load(VECTOR_PATH)
models = {name: joblib.load(path) for name, path in MODEL_PATHS.items()}

def clamp01(x):
    return 0.0 if x < 0 else 1.0 if x > 1 else x

def blend(c1, c2, t):
    t = clamp01(t)
    r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
    r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return f"#{r:02x}{g:02x}{b:02x}"

def set_badge(text, bg, fg):
    badge.config(text=text, background=bg, foreground=fg)

def set_progress_styles(ai_p):
    ai_color = blend("#16a34a", "#dc2626", ai_p)
    human_color = blend("#dc2626", "#16a34a", ai_p)

    style.configure("AI.Horizontal.TProgressbar", background=ai_color)
    style.configure("HUMAN.Horizontal.TProgressbar", background=human_color)

    lbl_ai_val.configure(foreground=ai_color)
    lbl_human_val.configure(foreground=human_color)

def predict():
    code = txt_code.get("1.0", "end").strip()
    if not code:
        messagebox.showwarning("Uyarı", "Lütfen kod gir.")
        return

    model_name = model_var.get()
    model = models[model_name]

    X = vectorizer.transform([code])
    proba = model.predict_proba(X)[0]

    ai_prob = clamp01(float(proba[1]))
    human_prob = clamp01(float(proba[0]))

    lbl_model_val.config(text=model_name)
    lbl_ai_val.config(text=f"%{ai_prob * 100:.2f}")
    lbl_human_val.config(text=f"%{human_prob * 100:.2f}")

    meter_ai["value"] = ai_prob * 100
    meter_human["value"] = human_prob * 100

    set_progress_styles(ai_prob)

    if ai_prob >= 0.70:
        set_badge("AI Yüksek", "#dc2626", "white")
    elif ai_prob >= 0.40:
        set_badge("Kararsız", "#d97706", "white")
    else:
        set_badge("İnsan Yüksek", "#16a34a", "white")

def clear_text():
    txt_code.delete("1.0", "end")
    lbl_model_val.config(text="-")
    lbl_ai_val.config(text="-", foreground="#64748b")
    lbl_human_val.config(text="-", foreground="#64748b")
    meter_ai["value"] = 0
    meter_human["value"] = 0
    set_badge("Hazır", "#334155", "white")
    style.configure("AI.Horizontal.TProgressbar", background="#6366f1")
    style.configure("HUMAN.Horizontal.TProgressbar", background="#16a34a")

root = tk.Tk()
root.title("Kodun AI mı İnsan mı Yazımı")
root.geometry("1100x640")
root.minsize(1000, 580)

BG = "#f5f7fb"
CARD = "#ffffff"
TEXT = "#0f172a"
MUTED = "#64748b"
BORDER = "#d9dbe1"
ACCENT = "#6366f1"

PANEL = "#f1f5f9"
PANEL_CARD = "#ffffff"
PANEL_TEXT = "#0f172a"
PANEL_MUTED = "#475569"

style = ttk.Style()
try:
    style.theme_use("clam")
except:
    pass

style.configure("TFrame", background=BG)
style.configure("Card.TFrame", background=CARD)

style.configure("Title.TLabel", background=BG, foreground=TEXT, font=("Segoe UI", 18, "bold"))
style.configure("Sub.TLabel", background=BG, foreground=MUTED, font=("Segoe UI", 10))
style.configure("CardTitle.TLabel", background=CARD, foreground=TEXT, font=("Segoe UI", 12, "bold"))

style.configure("Key.TLabel", background=CARD, foreground=MUTED, font=("Segoe UI", 10))
style.configure("Val.TLabel", background=CARD, foreground=TEXT, font=("Segoe UI", 16, "bold"))

style.configure("Panel.TFrame", background=PANEL)
style.configure("PanelCard.TFrame", background=PANEL_CARD)

style.configure("PanelTitle.TLabel", background=PANEL, foreground=PANEL_TEXT, font=("Segoe UI", 12, "bold"))
style.configure("PanelSub.TLabel", background=PANEL, foreground=PANEL_MUTED, font=("Segoe UI", 9))

style.configure("PanelKey.TLabel", background=PANEL_CARD, foreground=PANEL_MUTED, font=("Segoe UI", 10))
style.configure("PanelVal.TLabel", background=PANEL_CARD, foreground=PANEL_TEXT, font=("Segoe UI", 16, "bold"))

style.configure("TButton", font=("Segoe UI", 10), padding=10)
style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), padding=10, background=ACCENT, foreground="white")
style.map("Accent.TButton", background=[("active", "#4f46e5")])

style.configure("AI.Horizontal.TProgressbar", troughcolor="#e5e7eb", background=ACCENT, thickness=10)
style.configure("HUMAN.Horizontal.TProgressbar", troughcolor="#e5e7eb", background="#16a34a", thickness=10)

outer = ttk.Frame(root, padding=16)
outer.pack(fill="both", expand=True)

header = ttk.Frame(outer)
header.pack(fill="x", pady=(0, 12))

ttk.Label(header, text="Kodun AI mı İnsan mı Yazımı", style="Title.TLabel").pack(anchor="w")
ttk.Label(header, text="Kodu yapıştır • Model seç • Olasılıkları premium panelde gör", style="Sub.TLabel").pack(anchor="w", pady=(2, 0))

content = ttk.Frame(outer)
content.pack(fill="both", expand=True)

left = ttk.Frame(content)
left.pack(side="left", fill="both", expand=True, padx=(0, 14))

right = ttk.Frame(content, style="Panel.TFrame", width=360)
right.pack(side="right", fill="y")
right.pack_propagate(False)

code_card = ttk.Frame(left, style="Card.TFrame", padding=12)
code_card.pack(fill="both", expand=True)

ttk.Label(code_card, text="Kod Girişi", style="CardTitle.TLabel").pack(anchor="w", pady=(0, 8))

txt_code = tk.Text(
    code_card,
    font=("Consolas", 11),
    wrap="none",
    bd=0,
    background="#fbfcff",
    foreground=TEXT,
    insertbackground=TEXT,
    highlightthickness=1,
    highlightbackground=BORDER,
    highlightcolor=ACCENT
)
txt_code.pack(fill="both", expand=True)

top_panel = ttk.Frame(right, style="Panel.TFrame", padding=14)
top_panel.pack(fill="x")

ttk.Label(top_panel, text="Kontrol Paneli", style="PanelTitle.TLabel").pack(anchor="w")
ttk.Label(top_panel, text="Model seç, tahmin al, sonucu anında gör", style="PanelSub.TLabel").pack(anchor="w", pady=(2, 10))

badge = ttk.Label(top_panel, text="Hazır", background="#334155", foreground="white",
                  font=("Segoe UI", 9, "bold"), padding=(10, 4))
badge.pack(anchor="w", pady=(0, 10))

model_var = tk.StringVar(value=list(MODEL_PATHS.keys())[0])
cmb = ttk.Combobox(top_panel, textvariable=model_var, values=list(MODEL_PATHS.keys()), state="readonly")
cmb.pack(fill="x", pady=(0, 10))

btn_row = ttk.Frame(top_panel, style="Panel.TFrame")
btn_row.pack(fill="x")

btn_predict = ttk.Button(btn_row, text="Tahmin Et", style="Accent.TButton", command=predict)
btn_predict.pack(side="left", fill="x", expand=True)

btn_clear = ttk.Button(btn_row, text="Temizle", command=clear_text)
btn_clear.pack(side="left", padx=(8, 0))

panel_body = ttk.Frame(right, style="PanelCard.TFrame", padding=14)
panel_body.pack(fill="both", expand=True, padx=14, pady=(0, 14))

ttk.Label(panel_body, text="Sonuçlar", background=PANEL_CARD, foreground=PANEL_TEXT,
          font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0, 12))

row = ttk.Frame(panel_body, style="PanelCard.TFrame")
row.pack(fill="x", pady=(0, 10))
ttk.Label(row, text="Model", style="PanelKey.TLabel").pack(side="left")
lbl_model_val = ttk.Label(row, text="-", style="PanelVal.TLabel")
lbl_model_val.pack(side="right")

row2 = ttk.Frame(panel_body, style="PanelCard.TFrame")
row2.pack(fill="x", pady=(0, 6))
ttk.Label(row2, text="Yapay zeka", style="PanelKey.TLabel").pack(side="left")
lbl_ai_val = ttk.Label(row2, text="-", style="PanelVal.TLabel")
lbl_ai_val.pack(side="right")

meter_ai = ttk.Progressbar(panel_body, style="AI.Horizontal.TProgressbar", maximum=100, value=0)
meter_ai.pack(fill="x", pady=(0, 12))

row3 = ttk.Frame(panel_body, style="PanelCard.TFrame")
row3.pack(fill="x", pady=(0, 6))
ttk.Label(row3, text="İnsan", style="PanelKey.TLabel").pack(side="left")
lbl_human_val = ttk.Label(row3, text="-", style="PanelVal.TLabel")
lbl_human_val.pack(side="right")

meter_human = ttk.Progressbar(panel_body, style="HUMAN.Horizontal.TProgressbar", maximum=100, value=0)
meter_human.pack(fill="x", pady=(0, 12))

ttk.Separator(panel_body).pack(fill="x", pady=10)

hint = ttk.Label(panel_body, text="İpucu: Aynı kodu farklı modellerde deneyip sonuçları karşılaştır.",
                 background=PANEL_CARD, foreground=PANEL_MUTED, font=("Segoe UI", 9))
hint.pack(anchor="w")

lbl_ai_val.configure(foreground="#64748b")
lbl_human_val.configure(foreground="#64748b")

root.mainloop()
