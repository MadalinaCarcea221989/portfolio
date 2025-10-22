#!/usr/bin/env python3
"""
PDF to PNG Converter for Certificates
Converts PDF certificates to PNG format for web use
"""

import os
import sys
from pathlib import Path

try:
    from pdf2image import convert_from_path
    print("✓ pdf2image library found")
except ImportError:
    print("❌ pdf2image library not found. Installing...")
    os.system("pip install pdf2image")
    try:
        from pdf2image import convert_from_path
        print("✓ pdf2image library installed successfully")
    except ImportError:
        print("❌ Failed to install pdf2image. Please install manually: pip install pdf2image")
        print("Note: You may also need to install poppler: conda install -c conda-forge poppler")
        sys.exit(1)

def convert_pdf_to_png(pdf_path, output_path=None, dpi=300):
    """
    Convert a PDF file to PNG format

    Args:
        pdf_path (str): Path to the PDF file
        output_path (str, optional): Output PNG path. If None, uses same name as PDF
        dpi (int): DPI for conversion (higher = better quality, larger file)
    """
    if not os.path.exists(pdf_path):
        print(f"❌ PDF file not found: {pdf_path}")
        return False

    if output_path is None:
        output_path = pdf_path.replace('.pdf', '.png')

    try:
        print(f"🔄 Converting {pdf_path} to {output_path}...")

        # Convert PDF to images (returns list of PIL images)
        images = convert_from_path(pdf_path, dpi=dpi)

        # For certificates, we typically want the first page only
        if images:
            # Save the first page as PNG
            images[0].save(output_path, 'PNG')
            print(f"✅ Successfully converted: {output_path}")
            return True
        else:
            print(f"❌ No images found in PDF: {pdf_path}")
            return False

    except Exception as e:
        print(f"❌ Error converting {pdf_path}: {str(e)}")
        return False

def convert_directory_pdfs(input_dir, output_dir=None, dpi=300):
    """
    Convert all PDFs in a directory to PNGs

    Args:
        input_dir (str): Directory containing PDF files
        output_dir (str, optional): Output directory. If None, uses input_dir
        dpi (int): DPI for conversion
    """
    if output_dir is None:
        output_dir = input_dir

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Find all PDF files
    pdf_files = list(Path(input_dir).glob('*.pdf'))

    if not pdf_files:
        print(f"❌ No PDF files found in {input_dir}")
        return

    print(f"📁 Found {len(pdf_files)} PDF files to convert")

    converted = 0
    for pdf_file in pdf_files:
        pdf_path = str(pdf_file)
        png_filename = pdf_file.stem + '.png'
        png_path = os.path.join(output_dir, png_filename)

        if convert_pdf_to_png(pdf_path, png_path, dpi):
            converted += 1

    print(f"✅ Converted {converted}/{len(pdf_files)} PDF files")

def convert_certificates():
    """
    Convert all PDFs from certificates_pdf/ to PNGs in certificates/
    """
    input_dir = "certificates_pdf"
    output_dir = "certificates"

    if not os.path.exists(input_dir):
        print(f"❌ Input directory '{input_dir}' does not exist")
        return

    print(f"🔄 Converting certificates from {input_dir}/ to {output_dir}/")
    convert_directory_pdfs(input_dir, output_dir)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python pdf_to_png.py <pdf_file>")
        print("  python pdf_to_png.py <input_dir>")
        print("  python pdf_to_png.py <pdf_file> <output_png>")
        print("  python pdf_to_png.py certificates")
        print("    # Convert from certificates_pdf/ to certificates/")
        print()
        print("Examples:")
        print("  python pdf_to_png.py certificate.pdf")
        print("  python pdf_to_png.py images/certificates/")
        print("  python pdf_to_png.py certificate.pdf output.png")
        print("  python pdf_to_png.py certificates")
        return

    input_path = sys.argv[1]

    if input_path.lower() == "certificates":
        convert_certificates()
    elif len(sys.argv) >= 3:
        output_path = sys.argv[2]
        convert_pdf_to_png(input_path, output_path)
    elif os.path.isdir(input_path):
        convert_directory_pdfs(input_path)
    elif os.path.isfile(input_path) and input_path.lower().endswith('.pdf'):
        convert_pdf_to_png(input_path)
    else:
        print(f"❌ Invalid input: {input_path}")
        print("Please provide a PDF file or directory containing PDFs")


if __name__ == "__main__":
    main()
