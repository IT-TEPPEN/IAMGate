import pytest
from src.interface.crawler.background.parser.iam_action_html_parser import (
    IAMActionHTMLParser,
)


def test_colspan_and_rowspan():
    html = """
    <table>
      <tr>
        <td rowspan="2">A</td>
        <td>B</td>
        <td>C</td>
      </tr>
      <tr>
        <td colspan="2">D</td>
      </tr>
      <tr>
        <td>E</td>
        <td>F</td>
        <td>G</td>
      </tr>
    </table>
    """
    parser = IAMActionHTMLParser()
    parser.feed(html)
    assert parser.rows == [["A", "B", "C"], ["A", "D", "D"], ["E", "F", "G"]]


def test_complex_colspan_rowspan():
    html = """
    <table>
      <tr>
        <td rowspan="2" colspan="2">A</td>
        <td>B</td>
      </tr>
      <tr>
        <td>C</td>
      </tr>
      <tr>
        <td>D</td>
        <td>E</td>
        <td>F</td>
      </tr>
    </table>
    """
    parser = IAMActionHTMLParser()
    parser.feed(html)
    assert parser.rows == [["A", "A", "B"], ["A", "A", "C"], ["D", "E", "F"]]
