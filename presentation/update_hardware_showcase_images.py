"""
Generate and update hardware showcase images in Copy of SIH26177_v7.pptx.pptx:
1. Arduino UNO Q Dual-Brain Architecture Showcase (top-right of Slide 3).
   - High-res top-down transparent board render (Qualcomm Dragonwing QRB2210 + STM32U585).
   - Crisp technical callouts for Mission Computer & Flight Controller.
   - Physical unboxing photo inset ("Physical Hardware in Hand").
   - Specs banner: 4GB LPDDR4, 32GB eMMC, Sub-5W Compute, 42g AUW.
2. Multi-Spectral Sensor Payload Showcase (bottom-middle of Slide 3).
   - High-res macro render of gimbal sensor.
   - Callout badges: 1080p Optical RGB (OV2710) + Radiometric LWIR Thermal (MLX90640) + ToF Rangefinder.
"""

import os
import shutil
import zipfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter

font_bold = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
font_reg = "/System/Library/Fonts/Supplemental/Arial.ttf"

def generate_uno_q_showcase(output_path="/tmp/arduino_uno_q_showcase.jpg"):
    W, H = 1400, 1064
    canvas = Image.new("RGB", (W, H), (11, 17, 32)) # Tactical Dark Navy
    draw = ImageDraw.Draw(canvas)

    f_sub = ImageFont.truetype(font_bold, 20)
    f_box_h = ImageFont.truetype(font_bold, 20)
    f_chip_name = ImageFont.truetype(font_bold, 22)
    f_box_b = ImageFont.truetype(font_reg, 17)
    f_badge = ImageFont.truetype(font_bold, 18)
    f_spec = ImageFont.truetype(font_bold, 17)

    # Card border
    draw.rounded_rectangle([(8, 8), (W-8, H-8)], radius=20, outline=(30, 48, 76), width=3)

    # Header Bar
    draw.rounded_rectangle([(28, 24), (350, 66)], radius=10, fill=(217, 112, 15)) # Orange
    draw.text((42, 33), "ARDUINO UNO Q (ABX00163)", fill=(255, 255, 255), font=f_badge)
    draw.text((370, 35), "DUAL-BRAIN EDGE-AI & FLIGHT STABILIZATION SBC", fill=(148, 163, 184), font=f_sub)

    # Load Board
    board = Image.open("presentation/assets/arduino_uno_q_board.png").convert("RGBA")
    bw, bh = 640, 510
    board_resized = board.resize((bw, bh), Image.Resampling.LANCZOS)

    # Board drop shadow
    shadow = Image.new("RGBA", (bw + 60, bh + 60), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.ellipse([(20, 20), (bw + 40, bh + 40)], fill=(0, 0, 0, 180))
    shadow = shadow.filter(ImageFilter.GaussianBlur(30))

    bx = (W - bw) // 2 + 10
    by = 130

    canvas.paste(shadow, (bx - 30, by - 10), shadow)
    canvas.paste(board_resized, (bx, by), board_resized)

    # LEFT CALLOUT CARD: Mission Computer (QRB2210)
    lx, ly, lw, lh = 30, 140, 330, 480
    draw.rounded_rectangle([(lx, ly), (lx + lw, ly + lh)], radius=14, fill=(17, 24, 39, 230), outline=(56, 189, 248), width=2)
    draw.rounded_rectangle([(lx + 15, ly + 15), (lx + 230, ly + 47)], radius=6, fill=(14, 116, 144))
    draw.text((lx + 25, ly + 20), "MISSION COMPUTER", fill=(255, 255, 255), font=f_box_h)
    draw.text((lx + 15, ly + 65), "Qualcomm Dragonwing", fill=(255, 255, 255), font=f_chip_name)
    draw.text((lx + 15, ly + 95), "QRB2210 System-on-Chip", fill=(56, 189, 248), font=f_chip_name)

    qrb_lines = [
        "• Quad-Core Cortex-A53 @ 2.0 GHz",
        "• Debian Linux OS Environment",
        "• Adreno 702 GPU / Hexagon DSP",
        "• INT8 YOLOv8n Object Detection",
        "• Real-Time Tait-Bryan Raycasting",
        "• E22 LoRa UART Telemetry [3]",
        "• Sub-5W Heterogeneous AI Budget"
    ]
    for idx, line in enumerate(qrb_lines):
        draw.text((lx + 15, ly + 145 + idx * 42), line, fill=(226, 232, 240), font=f_box_b)

    # Pointer line to QRB2210
    draw.line([(lx + lw, ly + 110), (bx + 200, by + 190)], fill=(56, 189, 248), width=2)
    draw.ellipse([(bx + 195, by + 185), (bx + 205, by + 195)], fill=(56, 189, 248))

    # RIGHT CALLOUT CARD: Flight Controller (STM32U585)
    rx, ry, rw, rh = W - 360, 140, 330, 480
    draw.rounded_rectangle([(rx, ry), (rx + rw, ry + rh)], radius=14, fill=(17, 24, 39, 230), outline=(251, 146, 60), width=2)
    draw.rounded_rectangle([(rx + 15, ry + 15), (rx + 240, ry + 47)], radius=6, fill=(194, 65, 12))
    draw.text((rx + 25, ry + 20), "FLIGHT CONTROLLER", fill=(255, 255, 255), font=f_box_h)
    draw.text((rx + 15, ry + 65), "STMicroelectronics", fill=(255, 255, 255), font=f_chip_name)
    draw.text((rx + 15, ry + 95), "STM32U585 Microcontroller", fill=(251, 146, 60), font=f_chip_name)

    stm_lines = [
        "• ARM Cortex-M33 @ 160 MHz",
        "• Dedicated Zephyr RTOS Core",
        "• 250 Hz (4ms) Flight Loop",
        "• Direct 350 Hz PWM ESC Control",
        "• I2C: MPU6050 + MS5611 + ToF",
        "• UART: u-blox NEO-M8N GNSS",
        "• Fail-Safe Deterministic Layer"
    ]
    for idx, line in enumerate(stm_lines):
        draw.text((rx + 15, ry + 145 + idx * 42), line, fill=(226, 232, 240), font=f_box_b)

    # Pointer line to STM32
    draw.line([(rx, ry + 110), (bx + 440, by + 260)], fill=(251, 146, 60), width=2)
    draw.ellipse([(bx + 435, by + 255), (bx + 445, by + 265)], fill=(251, 146, 60))

    # BOTTOM INSET: Physical Unboxed Hardware in Hand
    unbox = Image.open("presentation/assets/arduino_uno_q_unbox.jpg").convert("RGB")
    uw, uh = 300, 225
    unbox_resized = unbox.resize((uw, uh), Image.Resampling.LANCZOS)
    u_card = Image.new("RGB", (uw + 12, uh + 44), (17, 24, 39))
    u_draw = ImageDraw.Draw(u_card)
    u_draw.rounded_rectangle([(0, 0), (uw + 11, uh + 43)], radius=10, outline=(217, 112, 15), width=2)
    u_card.paste(unbox_resized, (6, 6))
    u_draw.text((18, uh + 14), "✓ PHYSICAL HARDWARE IN HAND", fill=(251, 191, 36), font=f_badge)

    ux = W - uw - 45
    uy = H - uh - 120
    canvas.paste(u_card, (ux, uy))

    # BOTTOM SPECS BANNER
    draw.rounded_rectangle([(28, H - 76), (W - 28, H - 24)], radius=12, fill=(17, 24, 39), outline=(40, 56, 84), width=1)
    specs_text = "4 GB LPDDR4 RAM  •  32 GB eMMC STORAGE  •  SUB-5W TOTAL COMPUTE  •  42g BOARD AUW  •  DGCA MICRO-UAV COMPLIANT"
    draw.text((80, H - 58), specs_text, fill=(241, 245, 249), font=f_spec)

    canvas.save(output_path, quality=95)
    print(f"Generated {output_path}")

def generate_sensor_showcase(output_path="/tmp/sensor_payload_showcase.jpg"):
    gimbal = Image.open("presentation/assets/gimbal_sensor_macro_render.jpg").convert("RGB")
    W, H = 1000, 650
    gimbal_resized = gimbal.resize((W, H), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(gimbal_resized)

    f_badge = ImageFont.truetype(font_bold, 20)
    f_label = ImageFont.truetype(font_bold, 17)
    f_sub = ImageFont.truetype(font_reg, 15)

    # Outer border
    draw.rounded_rectangle([(6, 6), (W-6, H-6)], radius=16, outline=(56, 189, 248), width=3)

    # Header Badge
    draw.rounded_rectangle([(20, 18), (450, 58)], radius=10, fill=(15, 23, 42, 230), outline=(56, 189, 248), width=1)
    draw.text((32, 26), "MULTI-SPECTRAL SENSOR PAYLOAD", fill=(56, 189, 248), font=f_badge)

    # Bottom Info Overlay
    draw.rounded_rectangle([(20, H - 95), (W - 20, H - 20)], radius=12, fill=(15, 23, 42, 230), outline=(30, 48, 76), width=1)
    draw.text((35, H - 85), "• 1080p Optical RGB (OV2710) + Melexis MLX90640 Radiometric LWIR Thermal (8–14 μm)", fill=(255, 255, 255), font=f_label)
    draw.text((35, H - 55), "• ST VL53L1X Downward Laser ToF (Ground AGL)  |  Silicone Harmonic Vibration Isolation", fill=(203, 213, 225), font=f_sub)

    gimbal_resized.save(output_path, quality=95)
    print(f"Generated {output_path}")

def update_pptx():
    generate_uno_q_showcase()
    generate_sensor_showcase()

    src_pptx = "Copy of SIH26177_v7.pptx.pptx"
    tmp_pptx = "Copy of SIH26177_v7_tmp.pptx"

    with zipfile.ZipFile(src_pptx, "r") as zin:
        with zipfile.ZipFile(tmp_pptx, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == "ppt/media/image14.jpeg":
                    with open("/tmp/arduino_uno_q_showcase.jpg", "rb") as f:
                        zout.writestr(item, f.read())
                    print("Updated image14.jpeg (Arduino UNO Q Showcase)")
                elif item.filename == "ppt/media/image15.jpeg":
                    with open("/tmp/sensor_payload_showcase.jpg", "rb") as f:
                        zout.writestr(item, f.read())
                    print("Updated image15.jpeg (Sensor Payload Showcase)")
                else:
                    zout.writestr(item, zin.read(item.filename))

    shutil.move(tmp_pptx, src_pptx)
    print("Successfully committed updated media to PPTX.")

if __name__ == "__main__":
    update_pptx()
