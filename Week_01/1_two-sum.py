# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_q0HxI4xdpENe9oyuJUOi5AsoIq_I92w
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, element in enumerate(nums):
            if target - element in dic:
                return [dic[target - element], i]
            dic[element] = i