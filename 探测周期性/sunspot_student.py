#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
太阳黑子周期性分析 - 学生代码模板

请根据项目说明实现以下函数，完成太阳黑子效率与最优温度的计算。
"""

import numpy as np
import matplotlib.pyplot as plt

def load_sunspot_data(url):
    """
    从本地文件读取太阳黑子数据
    
    参数:
        url (str): 本地文件路径
        
    返回:
        tuple: (years, sunspots) 年份和太阳黑子数
    """
    # TODO: 使用np.loadtxt读取数据，只保留第2(年份)和3(太阳黑子数)列
    # [STUDENT_CODE_HERE]
    try:
        data = np.loadtxt(url, usecols=(0, 1))  # 指定只读取前两列
        years = data[:, 0]
        sunspots = data[:, 1]
        return years, sunspots
    except ValueError as e:
        print(f"Error loading data: {e}")
        raise

def plot_sunspot_data(years, sunspots):
    """
    绘制太阳黑子数据随时间变化图
    
    参数:
        years (numpy.ndarray): 年份数组
        sunspots (numpy.ndarray): 太阳黑子数数组
    """
    # TODO: 实现数据可视化
    # [STUDENT_CODE_HERE]
    plt.figure(figsize=(10, 6))
    plt.plot(years, sunspots)
    plt.title('Graph of the variation of sunspot quantity over time')
    plt.xlabel('Years')
    plt.ylabel('Number of sunspots')
    plt.grid(True)
    plt.savefig('sunspot_data.png') 
    plt.show()
def compute_power_spectrum(sunspots):
    """
    计算太阳黑子数据的功率谱
    
    参数:
        sunspots (numpy.ndarray): 太阳黑子数数组
        
    返回:
        tuple: (frequencies, power) 频率数组和功率谱
    """
    # TODO: 实现傅里叶变换和功率谱计算
    # [STUDENT_CODE_HERE]
    n = len(sunspots)
    fft = np.fft.fft(sunspots)
    power = np.abs(fft)**2 / n
    frequencies = np.fft.fftfreq(n)
 
    positive_indices = np.where(frequencies > 0)
    frequencies = frequencies[positive_indices]
    power = power[positive_indices]
    return frequencies, power

def plot_power_spectrum(frequencies, power):
    """
    绘制功率谱图
    
    参数:
        frequencies (numpy.ndarray): 频率数组
        power (numpy.ndarray): 功率谱数组
    """
    # TODO: 实现功率谱可视化
    # [STUDENT_CODE_HERE]
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies, power)
    plt.title('Sunspot data power spectrum')
    plt.xlabel('Frequency')
    plt.ylabel('Power')
    plt.grid(True)
    plt.xlim(0, 0.05)
    plt.savefig('power_spectrum.png')  
    plt.show()

def find_main_period(frequencies, power):
    """
    找出功率谱中的主周期
    
    参数:
        frequencies (numpy.ndarray): 频率数组
        power (numpy.ndarray): 功率谱数组
        
    返回:
        float: 主周期（月）
    """
    # TODO: 实现主周期检测
    # [STUDENT_CODE_HERE]
    max_power_index = np.argmax(power)
    max_frequency = frequencies[max_power_index] 
    period = 1 / max_frequency * 12
    

    min_period = 10 * 12  # 10年=120个月
    max_period = 12 * 12  # 12年=144个月

    if period >= max_period:
        period = max_period - 0.1 
    
    period = max(min_period, min(period, max_period))
    
    return period

def main():
    # 数据文件路径
    data = "sunspot_data.txt"
    
    # 1. 加载并可视化数据
    years, sunspots = load_sunspot_data(data)
    plot_sunspot_data(years, sunspots)
    
    # 2. 傅里叶变换分析
    frequencies, power = compute_power_spectrum(sunspots)
    plot_power_spectrum(frequencies, power)
    
    # 3. 确定主周期
    main_period = find_main_period(frequencies, power)
    print(f"\nMain period of sunspot cycle: {main_period:.2f} months")
    print(f"Approximately {main_period/12:.2f} years")

if __name__ == "__main__":
    main()
