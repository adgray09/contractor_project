from unittest import TestCase, main as unittest_main
from app import app

class ContractorTests(TestCase):
    """Flask tests."""


sample_chip = {
    'title': 'Salt and Vinegar',
    'description': 'Cats acting weird',
    'url': [
    'https://i5.walmartimages.com/asr/2d982a8d-39aa-4f78-a2a8-9ac9dae0f004_1.d97af068ee3d60be94301b502f074e7a.jpeg'
]
    
    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
    
    def test_new(self):
        """Test the new playlist creation page."""
        result = self.client.get('/chips/new')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'New Chip', result.data)
        
    def test_index(self):
        """Test the playlists homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Chip', result.data)
        
    @mock.patch('pymongo.collection.Collection.update_one')
    def test_chips_edit(self, mock_update):
        result = self.client.post(f'/playlists/{sample_chip_id}', data=sample_form_data)

        self.assertEqual(result.status, '302 FOUND')
        mock_update.assert_called_with({'_id': sample_chip_id}, {'$set': sample_playlist})
    
if __name__ == '__main__':
    unittest_main()