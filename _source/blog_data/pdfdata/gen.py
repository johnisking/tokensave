from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib import colors
import subprocess, json, os

TEXT = [
"Keeping a small vegetable garden productive through a whole season is mostly a matter of steady, unglamorous habits rather than special tricks. The most common reason beginners give up is not bad soil or bad luck but an early burst of enthusiasm followed by weeks of neglect. A bed that gets ten minutes of attention every second day will almost always outperform one that gets a whole weekend once a month.",
"Start with the soil. Before planting, loosen the top twenty centimetres with a fork and mix in a generous layer of compost. Avoid digging when the ground is wet, because compacted clay dries into hard clods that roots cannot push through. If water still pools on the surface an hour after rain, the bed needs either raising or more organic matter, and usually both.",
"Choose crops that suit the space and the climate instead of the seed catalogue. Lettuce, radishes, spinach and peas tolerate cool weather and can be sown early. Tomatoes, peppers, beans and squash need warm soil and should wait until the risk of frost has passed. Sowing a short row of fast crops every two weeks gives a steady harvest instead of a glut followed by nothing.",
"Water deeply and less often. A thorough soaking twice a week encourages roots to grow down, while a light daily sprinkle keeps them near the surface where they dry out quickly. Water in the morning so that leaves dry before evening, which reduces fungal disease. A layer of straw or shredded leaves around the plants keeps moisture in and weeds down.",
"Check the plants for pests while you water. Turning over a few leaves takes a minute and catches aphids, caterpillars and slug damage before they spread. Many problems can be handled by hand: pick off caterpillars, knock aphids off with a jet of water, and lay boards on the path overnight to collect slugs in the morning. Healthy, unstressed plants resist most attacks on their own.",
"Finally, keep simple notes. Write down what you planted, when, and how it did. After one season the notebook becomes more useful than any general guide, because it describes your own soil, your own weather and your own mistakes. Most experienced gardeners say the same thing: the second year is always better than the first, mainly because they remembered what went wrong.",
]
ROWS = [["Item", "Category", "Unit", "Price", "Stock", "Supplier"]] + [
    [f"Product {i:02d}", ["Seeds", "Tools", "Soil", "Pots", "Fertiliser"][i % 5], ["pack", "piece", "bag", "set"][i % 4],
     f"{(i * 37 % 90) + 1.5:.2f}", str((i * 13) % 120), ["GreenLeaf", "RootWorks", "SoilCo", "Bloom & Co"][i % 4]]
    for i in range(1, 36)]

styles = getSampleStyleSheet()

def text_story(n_pages):
    story = []
    for p in range(n_pages):
        story.append(Paragraph(f"Garden notes, page {p + 1}", styles["Heading2"]))
        for para in TEXT:
            story.append(Paragraph(para, styles["BodyText"]))
            story.append(Spacer(1, 6))
        if p < n_pages - 1:
            story.append(PageBreak())
    return story

def build(name, story):
    SimpleDocTemplate(f"pdfs/{name}.pdf", pagesize=A4).build(story)

build("text_1p", text_story(1))
build("text_5p", text_story(5))
build("text_10p", text_story(10))
t = Table(ROWS)
t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.5, colors.grey), ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey), ("FONTSIZE", (0, 0), (-1, -1), 9)]))
build("table_1p", [Paragraph("Garden supply price list", styles["Heading2"]), t])
subprocess.run(["pdftoppm", "-r", "150", "-png", "-singlefile", "pdfs/text_1p.pdf", "pdfs/scan"], check=True)
w, h = A4
from reportlab.pdfgen import canvas
c = canvas.Canvas("pdfs/scan_1p.pdf", pagesize=A4)
c.drawImage("pdfs/scan.png", 0, 0, width=w, height=h)
c.showPage()
c.save()
plain = f"Garden notes, page 1\n\n" + "\n\n".join(TEXT)
json.dump({"text_page_plain": plain, "table_plain": "\n".join(",".join(r) for r in ROWS)}, open("plain.json", "w"), indent=1)
for f in sorted(os.listdir("pdfs")):
    print(f, os.path.getsize(f"pdfs/{f}"))
