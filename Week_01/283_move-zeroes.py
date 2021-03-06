# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_q0HxI4xdpENe9oyuJUOi5AsoIq_I92w
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        if len(nums) == 1:
            return
        i = 0
        while nums[i] != 0:
            i += 1
            if i == len(nums):
                break
        for j in range(i + 1,len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1