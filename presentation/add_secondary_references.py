"""
Add SARDO (IEEE TMC 2022) and Mishra et al. (Elsevier 2020) as secondary
'Also cited:' lines inside existing card body TextBox 56 (Card 03) and
TextBox 65 (Card 04), preserving existing typography.
"""
import pptx
from pptx.dml.color import RGBColor
from pptx.util import Pt
from pptx.oxml.ns import qn
from lxml import etree
import copy

FILEPATH = "Copy of SIH26177_v6.pptx.pptx"

# Typography constants
FONT_NAME   = "Calibri"
BODY_SIZE   = 15.5
ALSO_SIZE   = 14.0
BODY_COLOR  = RGBColor(30, 38, 56)       # dark slate
LABEL_COLOR = RGBColor(0xB3, 0x5A, 0x00) # deep amber (matches → Strategy: )
ITALIC_COLOR= RGBColor(86, 96, 116)      # slate grey

def make_run(para, text, bold=False, italic=False, size=None, color=None, font=FONT_NAME):
    r = para.add_run()
    r.text = text
    r.font.name = font
    if size:
        r.font.size = Pt(size)
    if bold is not None:
        r.font.bold = bold
    if italic is not None:
        r.font.italic = italic
    if color:
        r.font.color.rgb = color
    return r

def append_also_cited(tf, label, citation_text):
    """Append a new paragraph with 'Also cited: <citation>' styling."""
    p = tf.add_paragraph()
    # Bold amber label
    r1 = make_run(p, "Also cited: ", bold=True, size=ALSO_SIZE, color=LABEL_COLOR)
    # Normal body citation
    r2 = make_run(p, citation_text, bold=False, italic=True, size=ALSO_SIZE, color=ITALIC_COLOR)

def main():
    prs = pptx.Presentation(FILEPATH)
    slide6 = prs.slides[5]

    shape_map = {s.name: s for s in slide6.shapes}

    # --- Card 03 (TalTech, IEEE Access 2023): add SARDO 2022 ---
    tb56 = shape_map.get("TextBox 56")
    if tb56:
        tf = tb56.text_frame
        append_also_cited(
            tf,
            "Also cited: ",
            "Albanese et al., SARDO — Automated SDR-based Victim Localization, IEEE TMC, 2022. "
            "Baseline comparison: Phoenix X achieves equivalent victim localization at 1/8th payload weight."
        )
        print(f"  Card 03 updated: TextBox 56 — SARDO (IEEE TMC 2022) appended")
    else:
        print("  ERROR: TextBox 56 not found")

    # --- Card 04 (Bouabdallah, EPFL/IEEE ICRA): add Mishra et al. 2020 ---
    tb65 = shape_map.get("TextBox 65")
    if tb65:
        tf = tb65.text_frame
        append_also_cited(
            tf,
            "Also cited: ",
            "Mishra et al. (BITS Pilani & Bennett Univ.), CNN-Based Aerial Human Action Detection, "
            "Elsevier Computer Communications, Vol. 156, 2020. "
            "Validates Phoenix X's YOLOv8n multi-spectral aerial detection pipeline."
        )
        print(f"  Card 04 updated: TextBox 65 — Mishra et al. (Elsevier 2020) appended")
    else:
        print("  ERROR: TextBox 65 not found")

    prs.save(FILEPATH)
    print(f"\nSaved: {FILEPATH}")

if __name__ == "__main__":
    main()
