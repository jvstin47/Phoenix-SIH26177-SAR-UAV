"""
Reposition Impact Pipeline above and Stakeholder Cards below on Slide 5 of Copy of SIH26177_v7.pptx.pptx,
and align all elements with millimeter-grade precision.
"""

import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

TARGET_PPTX = "Copy of SIH26177_v7.pptx.pptx"

def align_slide5():
    prs = pptx.Presentation(TARGET_PPTX)
    slide = prs.slides[4] # Slide 5 is 0-indexed as 4

    print(f"Loaded Slide 5 with {len(slide.shapes)} shapes.")

    # 1. Micro-align pipeline metrics row in Column 2 & 3 to exactly match Column 1 (9.250 in)
    ref_top_88 = slide.shapes[41].top # Group 88 in Col 1 (< 3 min)
    slide.shapes[48].top = ref_top_88  # Group 103 in Col 2 (2 km²)
    slide.shapes[55].top = ref_top_88  # Group 118 in Col 3 (0 cell towers)
    slide.shapes[62].top = ref_top_88  # Group 133 in Col 4 (Ranked queue)
    slide.shapes[69].top = ref_top_88  # Group 148 in Col 5 (₹1.2 Lakh)
    print("Normalized top metrics row to exactly 9.250 inches.")

    ref_top_91 = slide.shapes[42].top # Group 91 in Col 1 (unboxing to flight)
    slide.shapes[49].top = ref_top_91  # Group 106 in Col 2 (search sector)
    slide.shapes[56].top = ref_top_91  # Group 121 in Col 3 (needed to report locations)
    slide.shapes[63].top = ref_top_91  # Group 136 in Col 4 (+ safe rescue route)
    slide.shapes[70].top = ref_top_91  # Group 151 in Col 5 (vs ₹12-14 Lakhs)
    print("Normalized bottom metrics label row to exactly 9.690 inches.")

    # 2. Shift PIPELINE (shapes 27 to 70) ABOVE:
    # Target top: 2.150 inches (under subtitle which ends at 1.905 inches)
    pipeline_container = slide.shapes[27]
    old_pipe_top = pipeline_container.top
    new_pipe_top = Inches(2.150)
    delta_y_pipe = new_pipe_top - old_pipe_top

    for idx in range(27, 71):
        s = slide.shapes[idx]
        s.top = s.top + delta_y_pipe

    print(f"Shifted PIPELINE shapes (27-70) by delta_y = {delta_y_pipe / Inches(1):.4f} in. New top = {pipeline_container.top / Inches(1):.3f} in.")

    # 3. Shift CARDS (shapes 7 to 26) BELOW:
    # Target top: 6.856 inches (leaving 0.400 in gap below pipeline which ends at 2.150 + 4.306 = 6.456 in)
    # Target left: 0.892 inches (matching pipeline container left = 0.892 in)
    card1_container = slide.shapes[7]
    old_card_top = card1_container.top
    new_card_top = Inches(6.856)
    delta_y_cards = new_card_top - old_card_top

    old_card_left = card1_container.left
    new_card_left = Inches(0.892)
    delta_x_cards = new_card_left - old_card_left

    for idx in range(7, 27):
        s = slide.shapes[idx]
        s.top = s.top + delta_y_cards
        s.left = s.left + delta_x_cards

    print(f"Shifted CARDS shapes (7-26) by delta_y = {delta_y_cards / Inches(1):.4f} in, delta_x = {delta_x_cards / Inches(1):.4f} in. New top = {card1_container.top / Inches(1):.3f} in, left = {card1_container.left / Inches(1):.3f} in.")

    # 4. Standardize text box heights on cards and purge "through mud" vulnerability
    for tb_idx in [11, 16, 21, 26]:
        slide.shapes[tb_idx].height = Inches(1.854)

    # In TextBox 29 (Card 1), refine "Discovered through mud & debris" -> "Detected across debris & smoke"
    tb29 = slide.shapes[11]
    if len(tb29.text_frame.paragraphs) > 1:
        p1 = tb29.text_frame.paragraphs[1]
        if "mud" in p1.text.lower():
            # Update while preserving formatting
            for r in p1.runs:
                if "mud" in r.text.lower():
                    r.text = "Detected across debris & smoke"
                    print("Updated Card 1 text: 'Detected across debris & smoke' (purged mud vulnerability).")

    prs.save(TARGET_PPTX)
    print(f"Saved updated presentation to {TARGET_PPTX}")

if __name__ == "__main__":
    align_slide5()
