#!/bin/bash

# Ensure target directories exist
mkdir -p .agents/scripts/events .agents/scripts/rendering .agents/scripts/translation .agents/scripts/docs .agents/scripts/utils

echo "Moving remaining files to .agents/scripts/..."

# Events
mv -f manual_inputs_data_v2.json .agents/scripts/events/ 2>/dev/null
mv -f screen_name_list.json .agents/scripts/events/ 2>/dev/null

# Docs
mv -f export_spec_to_drive.py .agents/scripts/docs/ 2>/dev/null
mv -f export_to_doc.py .agents/scripts/docs/ 2>/dev/null
mv -f fetch_manual_inputs.py .agents/scripts/docs/ 2>/dev/null
mv -f fetch_manual_inputs_v2.py .agents/scripts/docs/ 2>/dev/null
mv -f fetch_requirements.py .agents/scripts/docs/ 2>/dev/null
mv -f fetch_urd_content.py .agents/scripts/docs/ 2>/dev/null

# Translation
mv -f translate.py .agents/scripts/translation/ 2>/dev/null
mv -f translate_final.py .agents/scripts/translation/ 2>/dev/null
mv -f translate_more.py .agents/scripts/translation/ 2>/dev/null
mv -f en_texts.txt .agents/scripts/translation/ 2>/dev/null
mv -f get_english_p.py .agents/scripts/translation/ 2>/dev/null

# Utils
mv -f gmail_auth.py .agents/scripts/utils/ 2>/dev/null
mv -f get_tele_id.py .agents/scripts/utils/ 2>/dev/null
mv -f parse_pdf.py .agents/scripts/utils/ 2>/dev/null
mv -f patch_getting_started.py .agents/scripts/utils/ 2>/dev/null
mv -f register_grab_screens.py .agents/scripts/utils/ 2>/dev/null
mv -f test_imap.py .agents/scripts/utils/ 2>/dev/null
mv -f fix_bottomsheet.py .agents/scripts/utils/ 2>/dev/null
mv -f auto_input_mail.ps1 .agents/scripts/utils/ 2>/dev/null
mv -f generate_mau_dau_doc.ps1 .agents/scripts/utils/ 2>/dev/null

# Temp files
mv -f temp_pdf_output.txt .agents/scripts/utils/ 2>/dev/null
mv -f urd_assessment_content.txt .agents/scripts/utils/ 2>/dev/null

echo "Cleanup complete!"
