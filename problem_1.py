# -*- coding: utf-8 -*-
"""
Created on Jul 13 2021, 8:33 PM
@author: amanj
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def numberInList_1(listOfElement: object, number: object):
    """
    Solution 1: Using 2 loops (Brute Force)
    Time complexity: O(n^2)
    :type listOfElement: object
    :param listOfElement:
    :type listOfElement:object
    :param number:
    :type number:
    """
    flag = False
    index = ()
    for i in range(len(listOfElement)):
        for j in range(i, len(listOfElement)):
            if number == listOfElement[i] + listOfElement[j]:
                flag = True
                index = (i, j)
                break
            else:
                continue
    return flag, index


def numberInList_2(listOfElement: object, number: object):
    """
    Solution 1: Using 1 loops
    Time complexity: O(n)
    :type listOfElement: object
    :param listOfElement:
    :type listOfElement:object
    :param number:
    :type number:
    """
    flag = False
    index = ()
    for i in listOfElement:
        if (number - i) in listOfElement:
            flag = True
            index = listOfElement.index(i), listOfElement.index(number-i)
    return flag, index


def numberInList_3(listOfElement: object, number: object):
    """
    Solution 1: Using 1 loops
    Time complexity: O(n)
    :type listOfElement: object
    :param listOfElement:
    :type listOfElement:object
    :param number:
    :type number:
    """
    flag = False
    index = ()
    for i in listOfElement:
        if (number - i) in listOfElement:
            flag = True
            index = listOfElement.index(i), listOfElement.index(number-i)
    return flag, index


if __name__ == '__main__':
    listOfElement = [10, 15, 3, 7]
    number = 17
    print(numberInList_1(listOfElement, number))
    print(numberInList_2(listOfElement, number))
    print(numberInList_3(listOfElement, number))
