import json
import os
from datetime import date
import flet as ft

DATA_FILE = "step_data.json"

# ===============================
# VERİ İŞLEMLERİ
# ===============================

def default_data():
    return {
        "date": str(date.today()),
        "steps": 0,
        "goal": 10000,
        "record": 0,
    }

def load_data():
    if not os.path.exists(DATA_FILE):
        return default_data()

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        # Gün değiştiyse adımları sıfırla ve rekoru güncelle
        if data.get("date") != str(date.today()):
            if data.get("steps", 0) > data.get("record", 0):
                data["record"] = data["steps"]
            data["date"] = str(date.today())
            data["steps"] = 0

        return data
    except Exception:
        return default_data()

def save_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Veri kaydedilirken hata oluştu: {e}")


# ===============================
# FLET UYGULAMASI
# ===============================

def main(page: ft.Page):
    page.title = "Step Pro"
    page.bgcolor = "#080A10"  # Kivy'deki koyu arka plan renk tonu
    page.padding = 20
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO

    # Verileri yükle
    data = load_data()

    # --- ŞEHİR VE DEĞİŞKENLER ---
    current_steps = data.get("steps", 0)
    current_goal = data.get("goal", 10000)
    current_record = data.get("record", 0)

    # --- UI ELEMANLARI ---

    # Başlık
    title_label = ft.Text(
        "👟 STEP PRO",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER,
    )

    # Durum Etiketi
    status_label = ft.Text(
        "Sensör Hazır / Manuel Takip",
        size=14,
        color="#4DB6AC",
        text_align=ft.TextAlign.CENTER,
    )

    # Adım Sayacı Göstergesi
    step_count_text = ft.Text(
        str(current_steps),
        size=48,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.LIGHT_BLUE_400,
    )

    goal_text = ft.Text(
        f"Hedef: {current_goal} adım",
        size=16,
        color=ft.colors.GREY_400,
    )

    record_text = ft.Text(
        f"Rekor: {current_record} adım",
        size=14,
        color=ft.colors.AMBER_400,
        weight=ft.FontWeight.W_500,
    )

    # İlerleme Çubuğu (Progress Bar)
    progress_val = min(current_steps / current_goal if current_goal > 0 else 0, 1.0)
    progress_bar = ft.ProgressBar(
        value=progress_val,
        color=ft.colors.LIGHT_BLUE_400,
        bgcolor="#1A1C23",
        height=12,
    )

    # Güncelleme ve Kaydetme Fonksiyonu
    def update_ui_and_save():
        nonlocal current_steps, current_record
        
        # Rekor kontrolü
        if current_steps > current_record:
            current_record = current_steps
            record_text.value = f"Rekor: {current_record} adım"

        # Görselleri güncelle
        step_count_text.value = str(current_steps)
        progress_bar.value = min(current_steps / current_goal if current_goal > 0 else 0, 1.0)
        
        # JSON'a kaydet
        data["steps"] = current_steps
        data["record"] = current_record
        data["goal"] = current_goal
        save_data(data)
        
        page.update()

    # --- BUTON KONTROLLERİ ---
    def add_steps(e, amount):
        nonlocal current_steps
        current_steps += amount
        update_ui_and_save()

    def reset_steps(e):
        nonlocal current_steps
        current_steps = 0
        update_ui_and_save()

    # --- KART TASARIMLARI (Kivy'deki Card sınıfı yerine Container) ---
    
    # Ana İlerleme Kartı
    main_card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("BUGÜNKÜ ADIMLAR", size=12, color=ft.colors.GREY_400, weight=ft.FontWeight.BOLD),
                step_count_text,
                progress_bar,
                ft.Row(
                    controls=[goal_text, record_text],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#141722",
        padding=25,
        border_radius=20,
    )

    # Hızlı Aksiyon/Test Kartı
    action_card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Hızlı Adım Ekle / Simüle Et", size=14, color=ft.colors.WHITE),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("+100", on_click=lambda e: add_steps(e, 100), bgcolor="#1E88E5", color=ft.colors.WHITE),
                        ft.ElevatedButton("+500", on_click=lambda e: add_steps(e, 500), bgcolor="#1565C0", color=ft.colors.WHITE),
                        ft.ElevatedButton("+1000", on_click=lambda e: add_steps(e, 1000), bgcolor="#0D47A1", color=ft.colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
                ft.OutlinedButton("Sıfırla", on_click=reset_steps, stroke_color=ft.colors.RED_400, color=ft.colors.RED_400),
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#141722",
        padding=20,
        border_radius=20,
    )

    # Sayfaya Elemanları Ekle
    page.add(
        ft.Column(
            controls=[
                title_label,
                status_label,
                ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                main_card,
                ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                action_card,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=10,
        )
    )

ft.app(target=main)
