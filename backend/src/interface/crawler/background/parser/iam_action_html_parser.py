from html.parser import HTMLParser


class TableReader:
    def __init__(self):
        self.col_index = -1
        self.row_index = -1
        self.rowspan = 1
        self.colspan = 1
        self.cells = {}

    def create_row(self):
        self.col_index = 0
        self.row_index += 1

        if self.row_index not in self.cells:
            self.cells[self.row_index] = {}

    def create_cell(self, rowspan=1, colspan=1):
        self.col_index += colspan

        while True:
            if self.col_index in self.cells[self.row_index]:
                self.col_index += 1
            else:
                break

        self.rowspan = rowspan
        self.colspan = colspan

        for r in range(self.row_index, self.row_index + rowspan):
            if r not in self.cells:
                self.cells[r] = {}

            self.col_index = len(self.cells[r])

            for c in range(self.col_index, self.col_index + colspan):
                if c not in self.cells[r]:
                    self.cells[r][c] = {}

    def add_data(self, data):
        for r in range(self.row_index, self.row_index + self.rowspan):
            for c in range(self.col_index, self.col_index + self.colspan):
                if "data" not in self.cells[r][c]:
                    self.cells[r][c]["data"] = data
                else:
                    self.cells[r][c]["data"] += f",{data}"

    def add_link(self, link):
        for r in range(self.row_index, self.row_index + self.rowspan):
            for c in range(self.col_index, self.col_index + self.colspan):
                self.cells[r][c]["link"] = link

    def get_cells(self):
        result = []
        for r in range(self.row_index + 1):
            row = []
            for c in range(self.col_index + 1):
                cell = self.cells[r].get(c, {})
                data = cell.get("data", "")
                link = cell.get("link", "")
                # row.append((data, link))
                row.append(data)
            result.append(row)
        return result


class IAMActionHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.table_reader = TableReader()
        self.in_table = False
        self.in_action_table = False
        self.in_th = False
        self.in_cell = False
        self.rows = []

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.in_table = True
        if tag == "th":
            self.in_th = True
        if self.in_table and self.in_action_table and tag == "tr":
            self.table_reader.create_row()
        if self.in_table and self.in_action_table and tag == "td":
            self.in_cell = True
            rowspan = 1
            colspan = 1
            for attr in attrs:
                if attr[0] == "rowspan":
                    rowspan = int(attr[1])
                if attr[0] == "colspan":
                    colspan = int(attr[1])
            self.table_reader.create_cell(rowspan=rowspan, colspan=colspan)
        if self.in_table and self.in_action_table and tag == "a":
            link = attrs[0][1] if attrs else ""
            self.table_reader.add_link(link)

    def handle_endtag(self, tag):
        if tag == "table":
            if self.in_action_table:
                self.rows = self.table_reader.get_cells()

            self.in_table = False
            self.in_action_table = False
        if tag == "th":
            self.in_th = False
        if tag == "td":
            self.in_cell = False

    def handle_data(self, data):
        if self.in_th:
            if data.strip().lower() == "action" or data.strip().lower() == "actions":
                self.in_action_table = True
        if self.in_table and self.in_cell and data.strip() and data != " ":
            self.table_reader.add_data(data.strip())
