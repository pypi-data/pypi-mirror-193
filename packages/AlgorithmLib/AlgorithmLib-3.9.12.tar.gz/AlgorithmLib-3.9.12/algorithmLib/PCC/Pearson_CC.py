# -*- coding: UTF-8 -*-
import sys,os
from os import  path
sys.path.append(path.dirname(__file__))
sys.path.append(os.path.dirname(path.dirname(__file__)))
from ctypes import *
import ctypes
import numpy as np

#  * -------------------------------------------------------------------------
#  * Arguments    : const emxArray_real_T *ref_in
#  *                const emxArray_real_T *sig_in
#  *                double fs
#  *                double *delay
#  *                double *err
#  * Return Type  : void
#  */
# void delay_estimation_15s(const emxArray_real_T *ref_in, const emxArray_real_T
#   *sig_in, double fs, double *delay, double *err)

def cal_PCC(refData, testData,calSize,mydll):
    """
    """

    refstruct = np.ascontiguousarray(refData, dtype=c_double).ctypes.data_as(ctypes.POINTER(c_double))
    teststruct = np.ascontiguousarray(testData, dtype=c_double).ctypes.data_as(ctypes.POINTER(c_double))
    mydll.Pearson_Correlation.argtypes = [POINTER(c_double),POINTER(c_double),c_long,POINTER(c_double)]
    pcc= c_double(0.0)
    mydll.Pearson_Correlation(refstruct,teststruct,c_long(calSize),byref(pcc))
    return pcc.value




if __name__ == '__main__':
    ref = r'C:\Users\vcloud_avl\Documents\我的POPO\src.wav'
    test = r'C:\Users\vcloud_avl\Documents\我的POPO\test.wav'
    from commFunction import  get_data_array_double
    import platform,time
    newdata,fs,ch = get_data_array_double(ref)
    refdata,fs,ch = get_data_array_double(test)
    newdata = newdata[:10000]
    refdata = refdata[:10000]
    mydll = None
    cur_paltform = platform.platform().split('-')[0]
    if cur_paltform == 'Windows':
        mydll = ctypes.windll.LoadLibrary(sys.prefix + '/pcc.dll')
    if cur_paltform == 'macOS':
        mydll = CDLL(sys.prefix + '/pcc.dylib')
    if cur_paltform == 'Linux':
        mydll = CDLL(sys.prefix + '/pcc.so')
    #mydll.Pearson_Correlation.argtypes = [POINTER(c_double), POINTER(c_double), c_long, POINTER(c_double)]
    # newdata = np.arange(0,20000,2)
    # refdata = np.arange(10000,30000,2)
    # print(len(newdata),len(refdata))
    # print(time.time())
    # print(np.corrcoef(refdata,newdata))
    # print(time.time())
    # print(cal_PCC(refdata,newdata,10000,mydll))
    # print(time.time())
    suma,sumb = 0,0
    for e in range(10000):
        a = time.time()
        res = np.corrcoef(refdata, newdata)
        print(res)
        b = time.time()
        suma += b - a
        c = time.time()
        res = cal_PCC(refdata, newdata, 10000, mydll)
        print(res)
        d = time.time()
        sumb += d - c
    print(suma/10000)
    print(sumb/10000)
    pass