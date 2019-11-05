import unittest
from src.ya_trans_simple import ya_translate_en_ru


class YaTranslatorAPITestCase(unittest.TestCase):


    def test_translation_request(self):
        source_text = 'Hi'
        result = ya_translate_en_ru(source_text)
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['text'][0], 'Привет')

    @unittest.expectedFailure
    def test_request_problems(self):
        source_text = 'Hi'
        result = ya_translate_en_ru(source_text)
        self.assertGreater(result['code'], 200)

    @unittest.expectedFailure
    def test_target_language_is_not_ru(self):
        source_text = 'Hi'
        result = ya_translate_en_ru(source_text)
        self.assertNotEqual(result['lang'], 'en-ru')
        self.assertNotEqual(result['text'][0], 'Привет')



if __name__ == '__main__':
    unittest.main()