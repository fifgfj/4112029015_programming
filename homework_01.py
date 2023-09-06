# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#BMI計算
height = float(input("請輸入身高(公尺)"))
weight = float(input("請輸入體重(公斤)"))
bmi = weight / (height**2)
print(f"你的bmi為:{bmi:.2f}")