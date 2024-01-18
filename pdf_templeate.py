from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=10)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 0, 255)

    pdf.cell(w=0, h=10, txt=row["Topic"], align="L", ln=1)

    for i in range(20, 290, 10):
        pdf.line(10, i, 200, i)

    # set footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, h=10, txt=row['Topic'], align="R", ln=1)

    for i in range(row['Pages']-1):
        pdf.add_page()
        for y in range(20, 290, 10):
            pdf.line(10, y, 200, y)
        # set footer
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, h=10, txt=row['Topic'], align="R", ln=1)


pdf.output("output.pdf")
