from api.controllers import Delivery
from django_mock_queries.query import MockSet, MockModel

def test_LotsOfItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  delivery_distance = 6
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 7.5

def test_MiddleOfTheRoadItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  delivery_distance = 4
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 5

def test_LittleItems():
  #Arrange
  # TODO: Arrange the items to run the test
  order = MockSet()
  order.add(MockModel(quantity=3))
  order.add(MockModel(quantity=1))
  del_dist = 2
  #Act
  # TODO: Call the function that will be tested
  cost = Delivery.calculate(order, del_dist)  
  #Assert
  # TODO: replace the pass with an assert to test the value returned.
  assert cost == 2.50

def test_DeliveryFees():
  # ----------------------------------------------------------
  # Edge cases for first logical branch
  #Arrange
  order1 = MockSet()
  order1.add(MockModel(quantity=11))
  del_dist1 = 4
  
  order2 = MockSet()
  order2.add(MockModel(quantity=10))
  del_dist2 = 5
  
  order3 = MockSet()
  order3.add(MockModel(quantity=6))
  del_dist3 = 7
  
  #Act
  cost1 = Delivery.calculate(order1, del_dist1)
  cost2 = Delivery.calculate(order2, del_dist2)
  cost3 = Delivery.calculate(order3, del_dist3)
    
  #Assert
  assert cost1 == 5
  assert cost2 == 5
  assert cost3 == 5
  
  # ----------------------------------------------------------
  # Edge cases for second logical branch
  #Arrange
  order1 = MockSet()
  order1.add(MockModel(quantity=5))
  del_dist1 = 3
  
  order2 = MockSet()
  order2.add(MockModel(quantity=3))
  del_dist2 = 4
  
  order3 = MockSet()
  order3.add(MockModel(quantity=7))
  del_dist3 = 2
  
  #Act
  cost1 = Delivery.calculate(order1, del_dist1)
  cost2 = Delivery.calculate(order2, del_dist2)
  cost3 = Delivery.calculate(order3, del_dist3)
    
  #Assert
  assert cost1 == 2.5
  assert cost2 == 2.5
  assert cost3 == 2.5
  
  # ----------------------------------------------------------
  # Edge cases for third logical branch
  # NO EDGE CASES FOR THIS BRANCH, ALL OTHER CASES FALL INTO THIS BRANCH
  
  # ----------------------------------------------------------
  # Edge cases for the entire unit
  #Arrange
  order1 = MockSet()
  order1.add(MockModel(quantity=1000))
  del_dist1 = 1000
  
  order2 = MockSet()
  order2.add(MockModel(quantity=1000))
  del_dist2 = 1
  
  order3 = MockSet()
  order3.add(MockModel(quantity=1))
  del_dist3 = 1
  
  #Act
  cost1 = Delivery.calculate(order1, del_dist1)
  cost2 = Delivery.calculate(order2, del_dist2)
  cost3 = Delivery.calculate(order3, del_dist3)
    
  #Assert
  assert cost1 == 7.5
  assert cost2 == 2.5
  assert cost3 == 2.5