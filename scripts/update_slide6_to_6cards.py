#!/usr/bin/env python3
"""
update_slide6_to_6cards.py

Updates Slide 6 of SIH26177_v8.pptx:
Replaces the 4 existing research paper cards with 6 individual numbered cards
('01' through '06'), each dedicated to one peer-reviewed research paper
(all dated 2023 or later).

Preserves Slides 1 through 5 completely untouched.
"""

import copy
import sys
from lxml import etree
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

NS = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}

PAPERS = [
    {
        'num': '01',
        'ref': '[1]',
        'header': 'IIT Jodhpur & Manipal Univ. (IEEE Access, Sept 2026) [1]',
        'title': '• "SwarmSAR-FW: Drone-Based Swarm Search & Rescue in Fire and Water Disasters"',
        'subsystem': '• HAZARD-AWARE DIJKSTRA ROUTING: ',
        'desc': 'Validates safe ingress routing (98.7% triage accuracy, 4.1s) avoiding obstacles. | ',
        'doi_label': 'DOI: ',
        'doi': '10.1109/ACCESS.2026.3730315',
        'url': 'https://doi.org/10.1109/ACCESS.2026.3730315'
    },
    {
        'num': '02',
        'ref': '[2]',
        'header': 'UPC Barcelona (IEEE Access, Sept 2026) [2]',
        'title': '• "Long-Range BLE Localization via Drone LoRa Relays for SAR Missions"',
        'subsystem': '• 868 MHZ LORA NLoS CANYON RELAY: ',
        'desc': 'Validates off-grid BLE-to-LoRa payload forwarding across deep terrain. | ',
        'doi_label': 'DOI: ',
        'doi': '10.1109/ACCESS.2026.3731317',
        'url': 'https://doi.org/10.1109/ACCESS.2026.3731317'
    },
    {
        'num': '03',
        'ref': '[3]',
        'header': 'Univ. of Cyprus & KIOS CoE (Elsevier Computer Communications, 2024) [3]',
        'title': '• "Mission-Critical ROS-LoRa Architecture for Autonomous Drone Search & Rescue"',
        'subsystem': '• 17-BYTE COMPACT TELEMETRY: ',
        'desc': 'Validates ultra-low-bandwidth bit-packed triage frames over off-grid LoRa links. | ',
        'doi_label': 'DOI: ',
        'doi': '10.1016/j.comcom.2024.04.015',
        'url': 'https://doi.org/10.1016/j.comcom.2024.04.015'
    },
    {
        'num': '04',
        'ref': '[4]',
        'header': 'TalTech Estonia (IEEE Access, July 2023) [4]',
        'title': '• "Applying RIS-Based Communication for Collaborative Swarm Computing"',
        'subsystem': '• DECENTRALIZED EDGE COMPUTE: ',
        'desc': 'Validates autonomous on-device compute (-32% energy, -18% latency) with zero cloud. | ',
        'doi_label': 'DOI: ',
        'doi': '10.1109/ACCESS.2023.3293737',
        'url': 'https://doi.org/10.1109/ACCESS.2023.3293737'
    },
    {
        'num': '05',
        'ref': '[5]',
        'header': 'IEEE Trans. Geoscience & Remote Sensing (IEEE TGRS, Nov 2023) [5]',
        'title': '• "RGB-T Multimodal Salient Object Detection for Disaster Search and Rescue"',
        'subsystem': '• DUAL-SPECTRAL AI FUSION: ',
        'desc': 'Validates 1080p RGB + LWIR thermal fusion with cross-attention for zero-light triage. | ',
        'doi_label': 'DOI: ',
        'doi': '10.1109/TGRS.2023.3332179',
        'url': 'https://doi.org/10.1109/TGRS.2023.3332179'
    },
    {
        'num': '06',
        'ref': '[6]',
        'header': 'IEEE Trans. Geoscience & Remote Sensing (IEEE TGRS, Dec 2023) [6]',
        'title': '• "Robust Monocular Visual-Inertial Odometry in GNSS-Denied Disaster Rubble"',
        'subsystem': '• GNSS-DENIED VIO SLAM: ',
        'desc': 'Validates anti-drift monocular VIO state estimation & obstacle avoidance in rubble. | ',
        'doi_label': 'DOI: ',
        'doi': '10.1109/TGRS.2023.3323519',
        'url': 'https://doi.org/10.1109/TGRS.2023.3323519'
    }
]

def update_presentation(pptx_path):
    prs = pptx.Presentation(pptx_path)
    slide6 = prs.slides[5]
    spTree = slide6.shapes._spTree

    # Templates to clone from the first card (indices in slide6.shapes: 17, 18, 19)
    # Shape 17 = Freeform 42 (background card)
    # Shape 18 = Group 43 (badge shadow)
    # Shape 19 = Group 45 (badge group with '01')
    template_bg = copy.deepcopy(slide6.shapes[17]._element)
    template_shadow = copy.deepcopy(slide6.shapes[18]._element)
    template_badge = copy.deepcopy(slide6.shapes[19]._element)

    # Calculate exact vertical geometry
    # Total vertical span: from 2511238 EMU (2.7463 in) to 9174724 EMU (10.0336 in)
    y_start = 2511238
    y_end = 9174724
    total_height = y_end - y_start  # 6663486 EMU (7.2873 in)

    num_cards = 6
    gap = 73152  # 0.080 in (5 gaps = 365760 EMU = 0.400 in)
    card_height = (total_height - (num_cards - 1) * gap) // num_cards  # 1049621 EMU (1.1479 in)
    pitch = card_height + gap  # 1122773 EMU (1.2279 in)

    badge_top_offset = 182880  # 0.200 in
    shadow_top_offset = badge_top_offset + 7144  # 0.2078 in

    text_top_offset = 73152    # 0.080 in
    text_left = 2029968        # 2.220 in
    text_width = 7818120       # 8.550 in
    text_height = 896112       # 0.980 in

    # Temporary holding list for created textbox elements
    created_textboxes = []

    # First, create the 6 textboxes using python-pptx high-level API
    for i, paper in enumerate(PAPERS):
        y_card = y_start + i * pitch
        tb = slide6.shapes.add_textbox(
            text_left,
            y_card + text_top_offset,
            text_width,
            text_height
        )
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0)
        tf.margin_right = Inches(0)
        tf.margin_top = Inches(0)
        tf.margin_bottom = Inches(0)

        # Paragraph 0: Header (Author & Venue)
        p0 = tf.paragraphs[0]
        p0.text = paper['header']
        p0.font.name = 'Calibri'
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)  # Navy
        p0.space_after = Pt(2)

        # Paragraph 1: Paper Title
        p1 = tf.add_paragraph()
        p1.text = paper['title']
        p1.font.name = 'Calibri'
        p1.font.size = Pt(10.5)
        p1.font.italic = True
        p1.font.color.rgb = RGBColor(0x56, 0x60, 0x74)  # Slate
        p1.space_after = Pt(2)

        # Paragraph 2: Subsystem & Technical Validation & DOI
        p2 = tf.add_paragraph()
        r_sub = p2.add_run()
        r_sub.text = paper['subsystem']
        r_sub.font.name = 'Calibri'
        r_sub.font.size = Pt(9.5)
        r_sub.font.bold = True
        r_sub.font.color.rgb = RGBColor(0x1E, 0x26, 0x38)  # Dark Charcoal

        r_desc = p2.add_run()
        r_desc.text = paper['desc']
        r_desc.font.name = 'Calibri'
        r_desc.font.size = Pt(9.5)
        r_desc.font.color.rgb = RGBColor(0x3C, 0x46, 0x5A)  # Medium Charcoal

        r_lbl = p2.add_run()
        r_lbl.text = paper['doi_label']
        r_lbl.font.name = 'Calibri'
        r_lbl.font.size = Pt(9.5)
        r_lbl.font.bold = True
        r_lbl.font.color.rgb = RGBColor(0xB3, 0x5A, 0x00)  # Orange-Brown

        r_doi = p2.add_run()
        r_doi.text = paper['doi']
        r_doi.font.name = 'Calibri'
        r_doi.font.size = Pt(9.5)
        r_doi.font.color.rgb = RGBColor(0x00, 0x00, 0xFF)  # Blue
        r_doi.hyperlink.address = paper['url']

        created_textboxes.append(tb._element)

    # Detach newly created textboxes from end of spTree
    for el in created_textboxes:
        spTree.remove(el)

    # Now remove the 24 old card elements: spTree[19:43]
    # Verify spTree[19] is Freeform 42 and spTree[42] is TextBox 89
    first_old_name = spTree[19].find('.//p:cNvPr', NS).get('name')
    last_old_name = spTree[42].find('.//p:cNvPr', NS).get('name')
    assert 'Freeform 42' in first_old_name, f"Unexpected element at 19: {first_old_name}"
    assert 'TextBox 89' in last_old_name, f"Unexpected element at 42: {last_old_name}"

    for _ in range(24):
        del spTree[19]

    # Verify that what is now at spTree[19] is Freeform 90 (right column container)
    post_del_name = spTree[19].find('.//p:cNvPr', NS).get('name')
    assert 'Freeform 90' in post_del_name, f"Unexpected element after deletion: {post_del_name}"

    # Now insert the 6 new cards (each having: background, badge shadow, badge group, textbox)
    insert_pos = 19
    shape_id_counter = 400

    for i, paper in enumerate(PAPERS):
        y_card = y_start + i * pitch

        # 1. Background Card
        bg = copy.deepcopy(template_bg)
        shape_id_counter += 1
        bg.find('.//p:cNvPr', NS).set('id', str(shape_id_counter))
        bg.find('.//p:cNvPr', NS).set('name', f'ResearchCard_BG_{paper["num"]}')
        bg_xfrm = bg.find('.//a:xfrm', NS)
        bg_xfrm.find('a:off', NS).set('y', str(y_card))
        bg_xfrm.find('a:ext', NS).set('cy', str(card_height))
        # Update path bounds
        path = bg.find('.//a:path', NS)
        path.set('h', str(card_height))
        for pt in path.findall('.//a:pt', NS):
            if pt.get('y') == '1561195':
                pt.set('y', str(card_height))

        # 2. Badge Shadow
        shadow = copy.deepcopy(template_shadow)
        shape_id_counter += 1
        shadow.find('.//p:cNvPr', NS).set('id', str(shape_id_counter))
        shadow.find('.//p:cNvPr', NS).set('name', f'BadgeShadow_{paper["num"]}')
        for child_nv in shadow.findall('.//p:cNvPr', NS)[1:]:
            shape_id_counter += 1
            child_nv.set('id', str(shape_id_counter))
        sh_xfrm = shadow.find('.//a:xfrm', NS)
        sh_xfrm.find('a:off', NS).set('y', str(y_card + shadow_top_offset))

        # 3. Badge Group
        badge = copy.deepcopy(template_badge)
        shape_id_counter += 1
        badge.find('.//p:cNvPr', NS).set('id', str(shape_id_counter))
        badge.find('.//p:cNvPr', NS).set('name', f'BadgeGroup_{paper["num"]}')
        for child_nv in badge.findall('.//p:cNvPr', NS)[1:]:
            shape_id_counter += 1
            child_nv.set('id', str(shape_id_counter))
        bd_xfrm = badge.find('.//a:xfrm', NS)
        bd_xfrm.find('a:off', NS).set('y', str(y_card + badge_top_offset))
        # Update badge number text
        t_el = badge.find('.//a:t', NS)
        t_el.text = paper['num']

        # 4. Textbox
        tb_el = created_textboxes[i]
        shape_id_counter += 1
        tb_el.find('.//p:cNvPr', NS).set('id', str(shape_id_counter))
        tb_el.find('.//p:cNvPr', NS).set('name', f'ResearchCard_Text_{paper["num"]}')

        # Insert all 4 elements in order
        spTree.insert(insert_pos, bg)
        insert_pos += 1
        spTree.insert(insert_pos, shadow)
        insert_pos += 1
        spTree.insert(insert_pos, badge)
        insert_pos += 1
        spTree.insert(insert_pos, tb_el)
        insert_pos += 1

    prs.save(pptx_path)
    print(f"Successfully updated Slide 6 of {pptx_path} with 6 individual numbered research cards!")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'SIH26177_v8.pptx'
    update_presentation(target)
