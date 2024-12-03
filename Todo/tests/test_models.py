from django.test import TestCase
from Todo.models import TodoData


class TestingModel(TestCase):
  def test_create_user(self):
    todotitle = "Studying"
    tododescription = "Study only"
    tododate = '2024-12-21'
    todostatus = "OPEN"

    tododata = TodoData.objects.create(todotitle=todotitle, tododescription=tododescription, tododate = tododate, todostatus=todostatus)

    self.assertEqual(tododata.todotitle, todotitle)
    self.assertEqual(tododata.tododescription,tododescription)
    self.assertEqual(tododata.todostatus, todostatus)

  def test_update_user(self):
    todotitle = "Gaming"
    tododescription = "Recording"
    tododate = '2024-12-30'
    todostatus = "WORKING"

    tododata = TodoData.objects.create(todotitle=todotitle, tododescription=tododescription, tododate = tododate, todostatus=todostatus)
    tododata.todostatus = "OPEN"

    self.assertEqual(tododata.todotitle, todotitle)
    self.assertEqual(tododata.tododescription,tododescription)
    self.assertEqual(tododata.todostatus, "OPEN")




