#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:19:28 2026

@author: duru
"""
trains_schedule = {
"T1": {"origin_city": "istanbul", "destination_city": "ankara", "departure_time": 10, "time_duration": 330},
"T2": {"origin_city": "istanbul", "destination_city": "ankara", "departure_time": 14, "time_duration": 210},
"T3": {"origin_city": "istanbul", "destination_city": "bursa", "departure_time": 9, "time_duration": 90},
"T4": {"origin_city": "bursa", "destination_city": "ankara", "departure_time": 12, "time_duration": 180},
"T5": {"origin_city": "istanbul", "destination_city": "izmit", "departure_time": 10, "time_duration": 60},
"T6": {"origin_city": "izmit", "destination_city": "ankara", "departure_time": 11, "time_duration": 270},
"T7": {"origin_city": "istanbul", "destination_city": "bolu", "departure_time": 11, "time_duration": 120},
"T8": {"origin_city": "bolu", "destination_city": "ankara", "departure_time": 15, "time_duration": 90},
"T9": {"origin_city": "samsun", "destination_city": "giresun", "departure_time": 9, "time_duration": 120},
"T10": {"origin_city": "giresun", "destination_city": "trabzon", "departure_time": 13, "time_duration": 90},
"T11": {"origin_city": "izmir", "destination_city": "afyon", "departure_time": 10, "time_duration": 150},
"T12": {"origin_city": "afyon", "destination_city": "antalya", "departure_time": 14, "time_duration": 120},}

def is_valid_trip(start_city, end_city, start_time, trip):
    if len(trip) == 1:
        train_id = trip[0]
        
        if train_id not in trains_schedule:
            return False
        
        train = trains_schedule[train_id]
        
        if train["origin_city"] != start_city or train["destination_city"] != end_city:
            return False
        
        if train["departure_time"] < start_time:
            return False
        return True
    
    elif len(trip) == 2:
        first, second = trip
        
        if first not in trains_schedule or second not in trains_schedule:
            return False
        
        first_train = trains_schedule[first]
        second_train = trains_schedule[second]
        
        if first_train["origin_city"] != start_city:
            return False
        if second_train["destination_city"] != end_city :
            return False
        if first_train["destination_city"] != second_train["origin_city"]:
            return False
        if first_train["departure_time"] < start_time:
            return False
        
        first_train_time = first_train["departure_time"] + first_train["time_duration"] / 60
        
        if second_train["departure_time"] < first_train_time:
            return False
        return True
    return False
