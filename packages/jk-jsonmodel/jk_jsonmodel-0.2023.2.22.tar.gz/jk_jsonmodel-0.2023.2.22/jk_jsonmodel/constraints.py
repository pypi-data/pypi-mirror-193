

__all__ = (
	"minValue", "maxValue", "valueIn",
	"minLength", "maxLength",
	"matchRegEx",
)



import typing
import re

from .AbstractConstraint import AbstractConstraint





################################################################################################################################

class _MinValue(AbstractConstraint):

	def __init__(self, value) -> None:
		self.__value = value
	#

	def __call__(self, value) -> typing.Union[str,None]:
		if value >= self.__value:
			return None
		return ">= {}".format(repr(self.__value))
	#

#

################################################################################################################################

class _MaxValue(AbstractConstraint):

	def __init__(self, value) -> None:
		self.__value = value
	#

	def __call__(self, value) -> typing.Union[str,None]:
		if value <= self.__value:
			return None
		return "<= {}".format(repr(self.__value))
	#

#

################################################################################################################################

class _ValueIn(AbstractConstraint):

	def __init__(self, values) -> None:
		self.__values = values
	#

	def __call__(self, value) -> typing.Union[str,None]:
		if value in self.__values:
			return None
		return "in {}".format(repr(self.__values))
	#

#

################################################################################################################################

class _MinLength(AbstractConstraint):

	def __init__(self, value) -> None:
		self.__value = value
	#

	def __call__(self, value) -> typing.Union[str,None]:
		if len(value) >= self.__value:
			return None
		return "length >= {}".format(repr(self.__value))
	#

#

################################################################################################################################

class _MaxLength(AbstractConstraint):

	def __init__(self, value) -> None:
		self.__value = value
	#

	def __call__(self, value) -> typing.Union[str,None]:
		if len(value) <= self.__value:
			return None
		return "length <= {}".format(repr(self.__value))
	#

#

################################################################################################################################

class _MatchesRegEx(AbstractConstraint):

	def __init__(self, regExPatternStr:str) -> None:
		self.__regExPatternStr = regExPatternStr
		self.__regExPattern = re.compile(regExPatternStr)
	#

	def __call__(self, value) -> typing.Union[str,None]:
		m = self.__regExPattern.match(value)
		if m:
			return None
		return "/{}/".format(repr(self.__regExPatternStr)[1:-1])
	#

#

################################################################################################################################







def minValue(value:typing.Union[int,float]) -> AbstractConstraint:
	assert isinstance(value, (int,float))
	return _MinValue(value)
#

def maxValue(value:typing.Union[int,float]) -> AbstractConstraint:
	assert isinstance(value, (int,float))
	return _MaxValue(value)
#

def valueIn(value:typing.Union[list,tuple]) -> AbstractConstraint:
	assert isinstance(value, (list,tuple))
	return _ValueIn(value)
#

def minLength(value:int) -> AbstractConstraint:
	assert isinstance(value, int)
	return _MinLength(value)
#

def maxLength(value:int) -> AbstractConstraint:
	assert isinstance(value, int)
	return _MaxLength(value)
#

def matchRegEx(regExPattern:str) -> AbstractConstraint:
	assert isinstance(regExPattern, str)
	return _MatchesRegEx(regExPattern)
#




