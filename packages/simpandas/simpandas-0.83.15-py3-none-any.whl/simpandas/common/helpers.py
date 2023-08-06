# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:14:32 2020

@author: Martín Carlos Araya <martinaraya@gmail.com>
"""

__version__ = '0.80.4'
__release__ = 20230112
__all__ = ['clean_axis', 'string_new_name', 'type_of_frame', 'main_key', 'item_key']


import pandas as pd


def clean_axis(axis=None):
    if axis is None:
        return 0
    if type(axis) is str and axis.lower() in ['row', 'rows', 'ind', 'index']:
        return 0
    if type(axis) is str and axis.lower() in ['col', 'cols', 'column', 'columns']:
        return 1
    if type(axis) is str and axis.lower() in ['both', 'rows&cols', 'cols&rows', 'all']:
        return 2
    if type(axis) is bool:
        return int(axis)
    if type(axis) is float:
        return int(axis)
    return axis


def string_new_name(new_name, intersection_character='∩'):
    if len(new_name) == 1:
        return list(new_name.values())[0]
    else:
        return intersection_character.join(map(str, dict.fromkeys(new_name.values())))


def type_of_frame(frame):
    from simpandas import SimSeries, SimDataFrame
    from pandas import Series, DataFrame
    try:
        if frame._isSimSeries:
            return SimSeries
    except:
        try:
            if frame._isSimDataFrame:
                return SimDataFrame
        except:
            if type(frame) is Series:
                return Series
            elif type(frame) is DataFrame:
                return DataFrame
            else:
                raise TypeError('frame is not an instance of Pandas or SimPandas frames')


def main_key(Key, clean=True, nameSeparator=':'):
    """
    returns the main part (before the name of the item) in the keyword,MAIN:ITEM
    """
    if type(Key) is str:
        if len(Key.strip()) > 0:
            return Key.strip().split(nameSeparator)[0]
        else:
            return ''
    if type(Key) is tuple and len(Key) == 2:
        return main_key(str(Key[0]), clean=clean, nameSeparator=nameSeparator)
    if type(Key) is list or type(Key) is tuple:
        results = []
        for K in Key:
            results.append(main_key(K))
        if clean:
            return list(set(results))
        else:
            return list(results)
    if isinstance(Key, pd.Series):
        return main_key(Key.name)


def item_key(Key, clean=True, nameSeparator=':'):
    """
    returns the item part (after the name of the item) in the keyword, MAIN:ITEM
    """
    if type(Key) is str:
        if len(Key.strip()) > 0:
            if nameSeparator in Key.strip():
                return Key.strip().split(nameSeparator)[-1]
        else:
            return ''
    if type(Key) is tuple and len(Key) == 2:
        return item_key(str(Key[0]), clean=clean, nameSeparator=nameSeparator)
    if type(Key) is list or type(Key) is tuple:
        results = []
        for K in Key:
            results.append(item_key(K))
        if clean:
            return list(set(results))
        else:
            return list(results)
    if isinstance(Key, pd.Series):
        return item_key(Key.name)
