from repositories.reports import DataBaseReport, JsonReport, PDFReport, XLSXReport

REPORT_TYPES = {"xlsx": XLSXReport, "json": JsonReport, "pdf": PDFReport, "db": DataBaseReport}
