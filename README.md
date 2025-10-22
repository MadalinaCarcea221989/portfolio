# Madalina Carcea - Portfolio Website

![Portfolio Preview](https://img.shields.io/badge/Status-Active-success)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

## About

Personal portfolio website showcasing my work as a Data Science & AI Engineering student at BUas. Features my projects in AI compliance systems, computer vision, robotics, and game development.

## Image Setup Instructions

Your portfolio images have been renamed to descriptive names for better maintainability. The current image structure is:

```
portfolio-website/
├── index.html
├── images/
│   ├── Ai_presentation.png
│   ├── Brain_tumour.png
│   ├── CV_Madalina_Carcea.pdf
│   ├── Cybersecurity_research_paper.png
│   ├── Dashboard.png
│   ├── Diploma.png
│   ├── Erasmus_meeting.png
│   ├── Erasmus_work.png
│   ├── Madalina_Carcea_Resume.pdf
│   ├── profile_pic.png
│   ├── profile_pic_2.png
│   ├── Project_DKG_findings.png
│   ├── Report_football.png
│   ├── Streamlit.png
│   ├── Tumour_graph.png
│   └── what_is_nlp.png
└── README.md
```

All image references in the HTML have been updated to use these descriptive names.

## Features

- Responsive Design: Mobile-first, works on all devices
- Dark/Light Theme: Toggle between themes
- Interactive Terminal: Press `Ctrl + `` ` to open hidden terminal
- Project Showcase: 12+ diverse projects across AI, ML, and game dev
- Professional Gallery: Image carousel showcasing conferences and presentations
- Certificate Gallery: Interactive slideshow featuring 38 professional certifications
- About Section: Detailed work experience and education
- Performance Metrics: Real-time load time display
- Smooth Animations: Intersection Observer API for scroll effects

## Technologies

- Frontend: Pure HTML5, CSS3, Vanilla JavaScript
- Icons: Font Awesome 6.4.0
- Fonts: Inter & JetBrains Mono (Google Fonts)
- Certificate Processing: Python with pdf2image & poppler
- No Build Tools: Single-file architecture, ready to deploy

## Certificate Management

The portfolio includes automated PDF to PNG conversion for certificate management:

### PDF to PNG Conversion Script

```bash
# Convert all PDFs in certificates_pdf/ to PNGs in certificates/
python pdf_to_png.py

# Convert specific PDF
python pdf_to_png.py certificates_pdf/your-certificate.pdf

# Convert entire directory
python pdf_to_png.py certificates_pdf/
```

**Requirements:**

- Python 3.6+
- pdf2image library: `pip install pdf2image`
- Poppler (automatically installed with pdf2image on Windows)

**Features:**

- Batch conversion of multiple PDFs
- High-quality PNG output optimized for web
- Automatic naming based on PDF filenames
- Error handling for corrupted PDFs

## Project Structure

```text
portfolio-website/
├── index.html              # Complete portfolio (single file)
├── pdf_to_png.py           # PDF to PNG conversion script
├── images/                 # Professional images with descriptive names
├── certificates/           # PNG certificate images for slideshow
├── certificates_pdf/       # Original PDF certificates
├── README.md              # This file
└── .gitignore            # Git ignore rules
```

## Deployment Options

### GitHub Pages (Free + Easy)

```bash
cd D:\Repos\portfolio-website
git add .
git commit -m "Update portfolio"
git push origin main
```

Then enable GitHub Pages in your repo settings!

### Netlify (Free + Custom Domain)

1. Drag and drop the entire `portfolio-website` folder to [Netlify](https://app.netlify.com/drop)
2. Connect custom domain in settings
3. SSL auto-configured

### Vercel (Free + Custom Domain)

```bash
npm i -g vercel
cd D:\Repos\portfolio-website
vercel
```

### Traditional Web Hosting

Upload entire folder to any web server. Make sure `images/` folder is uploaded too!

## Sections Included

### 1. Hero Section

- Terminal-style animation
- Your name and title
- Quick CTA buttons
- Meta information (location, education, languages)

### 2. Featured Project

- Enterprise AI Compliance Platform (SNP)
- Comprehensive technical description
- 780 tests, 68% coverage showcase
- Tech stack with 12+ technologies

### 3. Projects Grid

- 11 diverse projects from your GitHub
- Real GitHub links
- Tech tags for each project
- Hover animations

### 4. About Section

- Your story and background
- Detailed work experience (3 positions)
- Erasmus+ program experience
- Professional workspace image

### 5. Professional Gallery

- 5 conference/presentation images
- Interactive carousel navigation
- Thumbnail preview
- Image captions

### 6. Certificate Gallery

- 38 professional certifications in interactive slideshow
- Zoom functionality for detailed viewing
- Thumbnail navigation
- Comprehensive descriptions for each certificate
- PDF to PNG conversion for optimal web display

### 7. Skills Section

- 6 categories, 26+ skills
- Python, C++, SQL, JavaScript, Java/C#
- PyTorch, TensorFlow, OpenCV, ROS
- FastAPI, Flask, Docker, Azure
- Unity, Unreal, Blender
- Power BI, NumPy, Jupyter, R

### 8. Contact Section

- Real email: madalinacarcea@yahoo.com
- Phone: +31 643 538 696
- LinkedIn & GitHub links
- Social media buttons

## What Makes This Portfolio Special

- Single-file simplicity - No dependencies, no build process
- 780 tests mentioned - Shows engineering excellence
- Microservices architecture - Demonstrates senior-level thinking
- 12+ projects - Diverse skillset showcase
- Professional imagery - Conference talks, presentations
- Certificate Gallery - 38 professional certifications in interactive slideshow
- Working terminal easter egg - Shows technical creativity
- Performance metrics - Auto-displays load times
- Fully responsive - Works on phone, tablet, desktop
- Dark/light themes - Modern UX features

## Customization Guide

### Change Colors

Find this in the `<style>` section (around line 20):

```css
:root {
    --bg-primary: #0a0e27;
    --accent-primary: #00f0ff;  // Change this for different accent color
    --accent-secondary: #7c3aed;
}
```

### Add More Certificates

1. Place new PDF certificates in the `certificates_pdf/` folder
2. Run the conversion script: `python pdf_to_png.py`
3. Add new entries to the `certificates` array in the JavaScript section:

```javascript
const certificates = [
    // existing certificates...
    {
        src: 'certificates/your-new-certificate.png',
        title: 'Your Certificate Title',
        description: 'Brief description of the certification and skills covered'
    }
];
```

### Add More Gallery Images

In the JavaScript section, add to the `galleryImages` array:

```javascript
const galleryImages = [
    // existing images...
    {
        src: 'images/your-new-image.png',
        caption: 'Your caption here'
    }
];
```

### Add More Projects

Duplicate a `.project-card` div in the HTML and update the content.

## Testing Locally

Simply open `index.html` in your browser:

```bash
# Windows
start index.html

# Or just double-click the file in File Explorer
```

Note: Make sure images are in the correct folder before testing!

## Performance

- Load Time: < 1 second (after images optimized)
- Size: ~60KB HTML + your images
- Lighthouse Score: 95+ (with optimized images)
- No Dependencies: Everything is self-contained

## Checklist Before Deploy

- [ ] All image references updated to descriptive names
- [ ] Tested locally (opened index.html in browser)
- [ ] Checked all sections display correctly
- [ ] Verified all links work
- [ ] Gallery carousel functions properly
- [ ] Certificate slideshow displays all certificates correctly
- [ ] Zoom functionality works in certificate gallery
- [ ] Social sharing meta tags updated

## Contact

- Email: `madalinacarcea@yahoo.com`
- LinkedIn: [linkedin.com/in/madalina-carcea](https://linkedin.com/in/madalina-carcea)
- GitHub: [github.com/MadalinaCarcea221989](https://github.com/MadalinaCarcea221989)

Built with pure HTML, CSS, and JavaScript
