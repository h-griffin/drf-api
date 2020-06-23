from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Tree

# Create your tests here.
class TreeModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_tree = Tree.objects.create(
            name = 'Name of Tree',
            planter = test_user,
            description = 'Words about the tree',
        )
        test_tree.save()

    def test_tree_content(self):
        tree = Tree.objects.get(id=1)

        self.assertEqual(tree.name, 'Name of Tree')
        self.assertEqual(str(tree.planter), 'tester')
        self.assertEqual(tree.description, 'Words about the tree')

        