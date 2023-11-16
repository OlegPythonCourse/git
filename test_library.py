import pytest

import library
def test_convereter():
   result = library.converter(-2.54)
   assert result
def test_convereter_1():
   result = library.converter(-2.54)
   assert result
def test_convereter_2():
   with pytest.raises(TypeError):
      library.converter("xdddd")
