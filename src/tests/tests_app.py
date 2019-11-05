import unittest
from unittest.mock import patch
import json
from pathlib import Path
from src.app import update_date, add_new_shelf, add_new_doc, \
    move_doc_to_shelf

documents = []
directories = {}


@patch('src.app.documents', documents, create=True)
@patch('src.app.directories', directories, create=True)
class SecretaryAppTest(unittest.TestCase):

    def setUp(self):
        current_path = str(Path.cwd()).strip(
            'tests')  # TODO: Выяснить и поправить образование путей
        p_dirs = current_path + r'\fixtures\directories.json'
        p_docs = current_path + r'\fixtures\documents.json'
        with open(p_dirs, 'r', encoding='utf-8') as dirs:
            directories.update(json.load(dirs))
        with open(p_docs, 'r', encoding='utf-8') as docs:
            documents.extend(json.load(docs))

    def test_update_data(self):
        self.zero_docs = []
        self.zero_dirs = {}
        update_date()
        self.assertGreater(len(directories),
                           len(self.zero_dirs))
        self.assertGreater(len(documents),
                           len(self.zero_docs))

    def test_add_new_shelf(self):
        start_len = (len(directories))
        test_value = '12'
        self.assertNotIn(test_value, directories.keys())
        add_new_shelf(test_value)
        self.assertNotEqual(start_len, len(directories))

    # @patch('src.app.input', side_effect = ['1010', '3'])
    def test_move_non_existing_doc_to_shelf(self):
        non_exist_doc = 'несуществующий документ'
        test_shelf = '3'
        self.assertNotIn(non_exist_doc, documents)
        with patch('src.app.input',
                   side_effect=[non_exist_doc, test_shelf]):
            move_doc_to_shelf()
        self.assertIn(non_exist_doc, directories[test_shelf])
        # документ исправно копируется на полку, потому что
        # в исходном коде при запросе на удаление документа
        # несуществующий документ просто "не удаляется" из полки,
        # не вызывая ошибки.

    def test_add_new_document(self):
        with patch('src.app.input',
                   side_effect=['007', 'license', 'James Bond', '1']):
            result = add_new_doc()
        self.assertIn('007', directories['1'])
        self.assertEqual(result, '1')



if __name__ == '__main__':
    unittest.main()
