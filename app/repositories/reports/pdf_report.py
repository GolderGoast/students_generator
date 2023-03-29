import fpdf

from domain.report_creator import IReportGetter


class PDFReport(IReportGetter):
    def get_report(self):
        fpdf.set_global("FPDF_CACHE_MODE", 1)

        pdf = fpdf.FPDF()
        pdf.add_font("DejaVu", "", "resource/fonts_for_pdf/DejaVuSansCondensed.ttf", uni=True)
        pdf.add_font("DejaVu", "B", "resource/fonts_for_pdf/DejaVuSansCondensed-Bold.ttf", uni=True)

        for group in self.groups:
            pdf.add_page()
            pdf.set_font("DejaVu", size=25, style="B")
            pdf.cell(400, 15, txt=f"Группа {group.name}", ln=1)

            for student in group.students:
                pdf.set_font("DejaVu", size=10, style="")
                pdf.cell(
                    400,
                    8,
                    txt=f"{student.full_name} Почта: {student.email} Возраст: {student.age}, Пол: {student.gender},"
                    f" Рост: {student.height}, Вес: {student.weight}, Балл: {student.average_score}",
                    ln=1,
                )

        pdf.output(f"{self.report_path}.pdf")
