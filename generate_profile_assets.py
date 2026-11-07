import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = r"C:\Users\user\.gemini\antigravity\scratch\github-profile-tonii325\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Fonts
FONT_DIR = "C:/Windows/Fonts"
font_serif_lg = ImageFont.truetype(f"{FONT_DIR}/georgiab.ttf", 72)
font_serif_md = ImageFont.truetype(f"{FONT_DIR}/georgiab.ttf", 46)
font_serif_sm = ImageFont.truetype(f"{FONT_DIR}/georgiab.ttf", 36)

font_serif_i_lg = ImageFont.truetype(f"{FONT_DIR}/georgiai.ttf", 72)
font_serif_i_md = ImageFont.truetype(f"{FONT_DIR}/georgiai.ttf", 46)

font_sans_bold = ImageFont.truetype(f"{FONT_DIR}/segoeuib.ttf", 26)
font_sans_md = ImageFont.truetype(f"{FONT_DIR}/segoeui.ttf", 23)
font_sans_sm = ImageFont.truetype(f"{FONT_DIR}/segoeui.ttf", 20)
font_sans_xs = ImageFont.truetype(f"{FONT_DIR}/segoeui.ttf", 16)
font_sans_xxs = ImageFont.truetype(f"{FONT_DIR}/segoeui.ttf", 14)

font_mono_bold = ImageFont.truetype(f"{FONT_DIR}/consola.ttf", 22)
font_mono_md = ImageFont.truetype(f"{FONT_DIR}/consola.ttf", 20)
font_mono_sm = ImageFont.truetype(f"{FONT_DIR}/consola.ttf", 18)
font_mono_xs = ImageFont.truetype(f"{FONT_DIR}/consola.ttf", 16)

# Colors
BG_DARK = (13, 17, 23, 255)         # #0d1117
BG_CARD = (18, 22, 30, 255)         # #12161e
BORDER_COLOR = (48, 54, 61, 255)     # #30363d
BORDER_SUBTLE = (33, 38, 45, 255)    # #21262d
GOLD = (210, 153, 34, 255)          # #d29922 (amber/gold accent)
GOLD_LIGHT = (242, 192, 80, 255)    # #f2c050
TEXT_WHITE = (240, 246, 252, 255)    # #f0f6fc
TEXT_MUTED = (139, 148, 158, 255)   # #8b949e
TEXT_SUBTLE = (110, 118, 129, 255)  # #6e7681
CYAN = (88, 166, 255, 255)          # #58a6ff
GREEN = (63, 185, 80, 255)          # #3fb950
RED = (248, 81, 73, 255)            # #f85149
PURPLE = (187, 128, 247, 255)       # #bb80f7
AMBER_AWS = (255, 153, 0, 255)

def draw_card_base(width, height, radius=24, border_color=BORDER_COLOR, bg_color=BG_DARK):
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, fill=bg_color)
    draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, outline=border_color, width=2)
    return img

def add_ambient_glow(img, cx, cy, radius, color):
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    r, g, b, max_a = color
    steps = 15
    for i in range(steps):
        cur_r = int(radius * (1 - i / steps))
        alpha = int(max_a * (1 - i / steps) ** 1.8)
        glow_draw.ellipse([cx - cur_r, cy - cur_r, cx + cur_r, cy + cur_r], fill=(r, g, b, alpha))
    glow = glow.filter(ImageFilter.GaussianBlur(radius // 5))
    return Image.alpha_composite(img, glow)

# ==========================================
# 1. BANNER HEADER (1840 x 560)
# ==========================================
def generate_banner():
    W, H = 1840, 560
    base = draw_card_base(W, H, radius=32, border_color=(45, 51, 60, 255), bg_color=(12, 15, 20, 255))
    base = add_ambient_glow(base, 400, 260, 320, (210, 153, 34, 45))
    base = add_ambient_glow(base, 1400, 280, 360, (56, 139, 253, 30))
    
    draw = ImageDraw.Draw(base)
    
    # Left Content
    draw.text((100, 95), "H O L A ,  S O Y  A N T O N I O  👋", fill=GOLD, font=font_mono_bold)
    draw.text((100, 155), "Construyo con", fill=TEXT_WHITE, font=font_serif_lg)
    
    y_line2 = 250
    draw.text((100, y_line2), "backend, ", fill=TEXT_WHITE, font=font_serif_lg)
    bbox_b = font_serif_lg.getbbox("backend, ")
    x_offset = 100 + (bbox_b[2] - bbox_b[0])
    
    draw.text((x_offset, y_line2), "IA", fill=GOLD_LIGHT, font=font_serif_i_lg)
    bbox_ia = font_serif_i_lg.getbbox("IA")
    x_offset += (bbox_ia[2] - bbox_ia[0]) + 15
    
    draw.text((x_offset, y_line2), "y hardware.", fill=TEXT_WHITE, font=font_serif_lg)
    draw.text((100, 380), "Ingeniería Informática  ·  UNLaM  ·  Buenos Aires", fill=TEXT_MUTED, font=font_sans_md)
    
    # Right Side: Terminal Card
    term_x, term_y = 1100, 90
    term_w, term_h = 640, 370
    draw.rounded_rectangle([term_x, term_y, term_x + term_w, term_y + term_h], radius=20, fill=(20, 24, 33, 255), outline=(48, 54, 61, 255), width=2)
    
    # Terminal Dots
    draw.ellipse([term_x + 30, term_y + 25, term_x + 46, term_y + 41], fill=RED)
    draw.ellipse([term_x + 58, term_y + 25, term_x + 74, term_y + 41], fill=GOLD)
    draw.ellipse([term_x + 86, term_y + 25, term_x + 102, term_y + 41], fill=GREEN)
    
    tx = term_x + 36
    ty = term_y + 75
    draw.text((tx, ty), "$", fill=GOLD, font=font_mono_bold)
    draw.text((tx + 22, ty), " whoami", fill=TEXT_WHITE, font=font_mono_bold)
    draw.text((tx + 22, ty + 36), "antonio · dev backend & agentes ia", fill=TEXT_MUTED, font=font_mono_md)
    
    ty2 = ty + 90
    draw.text((tx, ty2), "$", fill=GOLD, font=font_mono_bold)
    draw.text((tx + 22, ty2), " ls ./intereses", fill=TEXT_WHITE, font=font_mono_bold)
    draw.text((tx + 22, ty2 + 36), "agentes-ia/   nestjs/   sistemas-embebidos/", fill=CYAN, font=font_mono_sm)
    draw.text((tx + 22, ty2 + 70), "seguridad/    cloud/    hardware/", fill=CYAN, font=font_mono_sm)
    
    ty3 = ty2 + 124
    draw.text((tx, ty3), "$", fill=GOLD, font=font_mono_bold)
    draw.rectangle([tx + 24, ty3 + 2, tx + 38, ty3 + 26], fill=GOLD_LIGHT)
    
    out_path = os.path.join(OUTPUT_DIR, "banner-header.png")
    base.save(out_path, "PNG")
    print(f"Generated: {out_path}")

# ==========================================
# 2. CARD: HISTORIA CLÍNICA (920 x 480)
# ==========================================
def generate_card_historia_clinica():
    W, H = 920, 480
    base = draw_card_base(W, H, radius=28, border_color=(45, 51, 60, 255), bg_color=(12, 15, 21, 255))
    base = add_ambient_glow(base, 720, 240, 240, (56, 139, 253, 35))
    draw = ImageDraw.Draw(base)
    
    # Left Content
    draw.text((60, 60), "WEB MOBILE-FIRST • SALUD", fill=GOLD, font=font_mono_sm)
    draw.text((60, 105), "Historia Clínica", fill=TEXT_WHITE, font=font_serif_md)
    
    desc_lines = [
        "Aplicación mobile-first para guardias",
        "médicas. 100% client-side, autoguardado",
        "con debounce y exportación a PDF",
        "o WhatsApp con Web Share API."
    ]
    dy = 180
    for line in desc_lines:
        draw.text((60, dy), line, fill=TEXT_MUTED, font=font_sans_md)
        dy += 36
        
    draw.text((60, 405), "JAVASCRIPT • VITE • JSPDF • LOCALSTORAGE", fill=TEXT_SUBTLE, font=font_mono_xs)
    
    # Right Mockup: Medical Card UI
    mx, my, mw, mh = 530, 65, 330, 350
    draw.rounded_rectangle([mx, my, mx + mw, my + mh], radius=18, fill=(20, 25, 34, 255), outline=(48, 54, 61, 255), width=2)
    
    # Header inside phone
    draw.text((mx + 20, my + 20), "GUARDIA MÉDICA", fill=TEXT_WHITE, font=font_sans_sm)
    # Online Pill
    draw.rounded_rectangle([mx + mw - 95, my + 18, mx + mw - 20, my + 44], radius=10, fill=(35, 134, 54, 40), outline=GREEN, width=1)
    draw.text((mx + mw - 85, my + 22), "ONLINE", fill=GREEN, font=font_sans_xxs)
    
    # Patient bar
    draw.rounded_rectangle([mx + 20, my + 60, mx + mw - 20, my + 105], radius=10, fill=(15, 18, 25, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((mx + 32, my + 68), "Paciente: Adulto · Box 04", fill=TEXT_WHITE, font=font_sans_xs)
    draw.text((mx + 32, my + 86), "Ingreso: Código Amarillo", fill=GOLD_LIGHT, font=font_sans_xxs)
    
    # Vitals boxes
    bx1 = mx + 20
    bw = (mw - 50) // 2
    # Vital 1: PA
    draw.rounded_rectangle([bx1, my + 120, bx1 + bw, my + 180], radius=10, fill=(15, 18, 25, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((bx1 + 12, my + 126), "P. ARTERIAL", fill=TEXT_MUTED, font=font_sans_xxs)
    draw.text((bx1 + 12, my + 146), "120/80", fill=CYAN, font=font_sans_bold)
    
    # Vital 2: FC
    bx2 = bx1 + bw + 10
    draw.rounded_rectangle([bx2, my + 120, bx2 + bw, my + 180], radius=10, fill=(15, 18, 25, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((bx2 + 12, my + 126), "FREC. CARDÍACA", fill=TEXT_MUTED, font=font_sans_xxs)
    draw.text((bx2 + 12, my + 146), "74 bpm", fill=RED, font=font_sans_bold)
    
    # ECG waveform preview
    ecg_y = my + 225
    pts = [
        (mx + 20, ecg_y), (mx + 80, ecg_y), (mx + 95, ecg_y - 25), (mx + 110, ecg_y + 35),
        (mx + 125, ecg_y - 45), (mx + 140, ecg_y + 10), (mx + 155, ecg_y), (mx + 220, ecg_y),
        (mx + 235, ecg_y - 25), (mx + 250, ecg_y + 35), (mx + 265, ecg_y - 45), (mx + 280, ecg_y), (mx + mw - 20, ecg_y)
    ]
    draw.line(pts, fill=CYAN, width=3)
    
    # Export button
    btn_y = my + 280
    draw.rounded_rectangle([mx + 20, btn_y, mx + mw - 20, btn_y + 45], radius=10, fill=(31, 111, 235, 255))
    draw.text((mx + 65, btn_y + 11), "📄  Exportar a PDF / Share", fill=TEXT_WHITE, font=font_sans_sm)
    
    out_path = os.path.join(OUTPUT_DIR, "card-historia-clinica.png")
    base.save(out_path, "PNG")
    print(f"Generated: {out_path}")

# ==========================================
# 3. CARD: BANDONEAR (920 x 480)
# ==========================================
def generate_card_bandonear():
    W, H = 920, 480
    base = draw_card_base(W, H, radius=28, border_color=(45, 51, 60, 255), bg_color=(14, 16, 21, 255))
    base = add_ambient_glow(base, 720, 240, 240, (210, 153, 34, 40))
    draw = ImageDraw.Draw(base)
    
    # Left Content
    draw.text((60, 60), "HARDWARE + SOFTWARE • UNLaM", fill=GOLD, font=font_mono_sm)
    draw.text((60, 105), "BandoneAR", fill=TEXT_WHITE, font=font_serif_md)
    
    desc_lines = [
        "Bandoneón digital portátil e interactivo.",
        "Basado en Raspberry Pi (Pico + Zero),",
        "procesamiento de sonido en tiempo real,",
        "fuelle con encoder y motor FluidSynth."
    ]
    dy = 180
    for line in desc_lines:
        draw.text((60, dy), line, fill=TEXT_MUTED, font=font_sans_md)
        dy += 36
        
    draw.text((60, 405), "RASPBERRY PI • FLUIDSYNTH • C++ • HARDWARE", fill=TEXT_SUBTLE, font=font_mono_xs)
    
    # Right Graphic: Bandoneon Instrument & Synth Mockup
    gx, gy, gw, gh = 520, 65, 340, 350
    draw.rounded_rectangle([gx, gy, gx + gw, gy + gh], radius=18, fill=(22, 19, 26, 255), outline=(55, 45, 60, 255), width=2)
    
    # Bellows (fuelle) stylized representation
    bellow_x = gx + 25
    bellow_y = gy + 30
    bellow_w = 110
    bellow_h = 240
    
    folds = 7
    fh = bellow_h // folds
    for i in range(folds):
        y1 = bellow_y + i * fh
        y2 = y1 + fh
        # fold shape
        mid_x = bellow_x + bellow_w - 20 if i % 2 == 0 else bellow_x + bellow_w
        draw.polygon([(bellow_x, y1), (mid_x, (y1 + y2)//2), (bellow_x, y2)], fill=(38, 30, 42, 255), outline=GOLD)
    
    # Key panel (botonera de bandoneón)
    btn_panel_x = gx + 155
    btn_panel_y = gy + 30
    btn_panel_w = 160
    btn_panel_h = 240
    draw.rounded_rectangle([btn_panel_x, btn_panel_y, btn_panel_x + btn_panel_w, btn_panel_y + btn_panel_h], radius=12, fill=(28, 24, 32, 255), outline=(75, 62, 85, 255), width=1)
    
    # Ivory buttons grid
    cols, rows = 4, 5
    for c in range(cols):
        for r in range(rows):
            bx = btn_panel_x + 22 + c * 32
            by = btn_panel_y + 24 + r * 42
            # Offset every second col
            if c % 2 == 1:
                by += 15
            # Button rim & center
            draw.ellipse([bx - 10, by - 10, bx + 10, by + 10], fill=(235, 230, 220, 255), outline=(140, 130, 120, 255), width=2)
            draw.ellipse([bx - 4, by - 4, bx + 4, by + 4], fill=(255, 255, 255, 255))
            
    # Bottom specs pill
    pill_y = gy + 290
    draw.rounded_rectangle([gx + 25, pill_y, gx + gw - 25, pill_y + 40], radius=8, fill=(15, 14, 20, 255), outline=BORDER_COLOR, width=1)
    draw.text((gx + 40, pill_y + 10), "⚡ RPi Pico · Synth 44.1kHz · CONAISI", fill=GOLD_LIGHT, font=font_mono_xs)
    
    out_path = os.path.join(OUTPUT_DIR, "card-bandonear.png")
    base.save(out_path, "PNG")
    print(f"Generated: {out_path}")

# ==========================================
# 4. CARD: BOTÓN ANTIPÁNICO (920 x 480)
# ==========================================
def generate_card_boton_antipanico():
    W, H = 920, 480
    base = draw_card_base(W, H, radius=28, border_color=(45, 51, 60, 255), bg_color=(12, 15, 22, 255))
    base = add_ambient_glow(base, 720, 240, 240, (248, 81, 73, 35))
    draw = ImageDraw.Draw(base)
    
    # Left Content
    draw.text((60, 60), "SISTEMA EMBEBIDO • SEGURIDAD", fill=GOLD, font=font_mono_sm)
    draw.text((60, 105), "Botón Antipánico", fill=TEXT_WHITE, font=font_serif_md)
    
    desc_lines = [
        "Sistema de seguridad multicomponente",
        "en C++ sobre Raspberry Pi, con app",
        "Android para activación remota y",
        "alertas automáticas a emergencias."
    ]
    dy = 180
    for line in desc_lines:
        draw.text((60, dy), line, fill=TEXT_MUTED, font=font_sans_md)
        dy += 36
        
    draw.text((60, 405), "C++ • RASPBERRY PI • ANDROID • UNLAM", fill=TEXT_SUBTLE, font=font_mono_xs)
    
    # Right Graphic: Emergency Hardware Widget
    gx, gy, gw, gh = 520, 65, 340, 350
    draw.rounded_rectangle([gx, gy, gx + gw, gy + gh], radius=18, fill=(20, 23, 30, 255), outline=(50, 56, 68, 255), width=2)
    
    # Central Emergency Beacon
    cx, cy = gx + gw // 2, gy + 120
    # Radar rings
    for r in [90, 70, 50]:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(248, 81, 73, 60), width=1)
        
    # Big Emergency Button
    draw.ellipse([cx - 38, cy - 38, cx + cy, cy + 38], fill=(180, 30, 30, 255), outline=(248, 81, 73, 255), width=3)
    # Siren / Warning icon inside
    draw.polygon([(cx, cy - 20), (cx - 16, cy + 12), (cx + 16, cy + 12)], fill=(255, 255, 255, 255))
    draw.text((cx - 3, cy - 8), "!", fill=(180, 30, 30, 255), font=font_sans_bold)
    
    # Status badges
    card_y = gy + 200
    draw.rounded_rectangle([gx + 25, card_y, gx + gw - 25, card_y + 48], radius=10, fill=(15, 18, 24, 255), outline=BORDER_COLOR, width=1)
    draw.text((gx + 40, card_y + 14), "SISTEMA ACTIVO", fill=TEXT_WHITE, font=font_sans_xs)
    # Green armed pill
    draw.rounded_rectangle([gx + gw - 110, card_y + 11, gx + gw - 40, card_y + 37], radius=8, fill=(35, 134, 54, 40), outline=GREEN, width=1)
    draw.text((gx + gw - 100, card_y + 15), "ARMED", fill=GREEN, font=font_sans_xxs)
    
    # Android Alert notification simulation
    notif_y = card_y + 60
    draw.rounded_rectangle([gx + 25, notif_y, gx + gw - 25, notif_y + 60], radius=10, fill=(25, 30, 42, 255), outline=CYAN, width=1)
    draw.text((gx + 40, notif_y + 10), "📱 Notificación Android", fill=CYAN, font=font_sans_xxs)
    draw.text((gx + 40, notif_y + 30), "Alerta de pánico activada vía C++", fill=TEXT_WHITE, font=font_sans_xs)
    
    out_path = os.path.join(OUTPUT_DIR, "card-boton-antipanico.png")
    base.save(out_path, "PNG")
    print(f"Generated: {out_path}")

# ==========================================
# 5. CARD: AGENTES DE IA & BACKEND (920 x 480)
# ==========================================
def generate_card_ai_agents():
    W, H = 920, 480
    base = draw_card_base(W, H, radius=28, border_color=(45, 51, 60, 255), bg_color=(13, 16, 23, 255))
    base = add_ambient_glow(base, 720, 240, 240, (187, 128, 247, 35))
    draw = ImageDraw.Draw(base)
    
    # Left Content
    draw.text((60, 60), "AGENTES CONVERSACIONALES • CLOUD", fill=GOLD, font=font_mono_sm)
    draw.text((60, 105), "Agentes de IA & Ops", fill=TEXT_WHITE, font=font_serif_md)
    
    desc_lines = [
        "Implementación de agentes conversacionales",
        "con Salesforce Agentforce y ElevenLabs en",
        "WhatsApp. Automatización de ramas JSON y",
        "APIs REST con NestJS y MariaDB."
    ]
    dy = 180
    for line in desc_lines:
        draw.text((60, dy), line, fill=TEXT_MUTED, font=font_sans_md)
        dy += 36
        
    draw.text((60, 405), "ELEVENLABS • AGENTFORCE • NESTJS • AWS AI", fill=TEXT_SUBTLE, font=font_mono_xs)
    
    # Right Graphic: AI Conversational Flow
    gx, gy, gw, gh = 520, 65, 340, 350
    draw.rounded_rectangle([gx, gy, gx + gw, gy + gh], radius=18, fill=(19, 23, 32, 255), outline=(48, 54, 61, 255), width=2)
    
    # Flow Node 1: WhatsApp Channel
    n1_y = gy + 30
    draw.rounded_rectangle([gx + 25, n1_y, gx + gw - 25, n1_y + 55], radius=10, fill=(15, 25, 20, 255), outline=GREEN, width=1)
    draw.text((gx + 40, n1_y + 16), "💬  WhatsApp Canal Digital", fill=TEXT_WHITE, font=font_sans_xs)
    draw.text((gx + gw - 80, n1_y + 18), "INPUT", fill=GREEN, font=font_mono_xs)
    
    # Arrow 1
    draw.line([(gx + gw//2, n1_y + 55), (gx + gw//2, n1_y + 75)], fill=TEXT_SUBTLE, width=2)
    
    # Flow Node 2: ElevenLabs & Agentforce AI
    n2_y = n1_y + 75
    draw.rounded_rectangle([gx + 25, n2_y, gx + gw - 25, n2_y + 65], radius=10, fill=(28, 22, 38, 255), outline=PURPLE, width=1)
    draw.text((gx + 40, n2_y + 12), "🧠  Agentforce + ElevenLabs", fill=TEXT_WHITE, font=font_sans_xs)
    draw.text((gx + 40, n2_y + 36), "Prompt Engineering & Branch Sync", fill=PURPLE, font=font_sans_xxs)
    
    # Arrow 2
    draw.line([(gx + gw//2, n2_y + 65), (gx + gw//2, n2_y + 85)], fill=TEXT_SUBTLE, width=2)
    
    # Flow Node 3: Backend NestJS
    n3_y = n2_y + 85
    draw.rounded_rectangle([gx + 25, n3_y, gx + gw - 25, n3_y + 55], radius=10, fill=(24, 18, 22, 255), outline=RED, width=1)
    draw.text((gx + 40, n3_y + 16), "⚡  NestJS REST API · MariaDB", fill=TEXT_WHITE, font=font_sans_xs)
    draw.text((gx + gw - 90, n3_y + 18), "OUTPUT", fill=RED, font=font_mono_xs)
    
    # Bottom Cert Badge: AWS Certified AI Practitioner
    cert_y = gy + 290
    draw.rounded_rectangle([gx + 25, cert_y, gx + gw - 25, cert_y + 42], radius=8, fill=(35, 25, 15, 255), outline=AMBER_AWS, width=1)
    draw.text((gx + 40, cert_y + 11), "☁️  AWS Certified AI Practitioner", fill=AMBER_AWS, font=font_sans_sm)
    
    out_path = os.path.join(OUTPUT_DIR, "card-ai-agents.png")
    base.save(out_path, "PNG")
    print(f"Generated: {out_path}")

if __name__ == "__main__":
    generate_banner()
    generate_card_historia_clinica()
    generate_card_bandonear()
    generate_card_boton_antipanico()
    generate_card_ai_agents()
    print("All profile assets generated successfully!")
