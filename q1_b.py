#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:54:48 2026

@author: duru
"""
from q1_a import is_valid_trip

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

def find_trips(start_city, end_city, start_time):
    res = []
    
    train_ids = list(trains_schedule.keys())
    
    for train_id in train_ids:
        trip = (train_id,)
        
        if is_valid_trip(start_city, end_city, start_time, trip):
            train = trains_schedule[train_id]
            
            total_dur = train["time_duration"]
            
            res.append([trip, total_dur])
        
    for first_id in trains_schedule:
        for second_id in trains_schedule:
            if first_id == second_id:
                continue
            trip = (first_id, second_id)
            if is_valid_trip(start_city, end_city, start_time, trip):
                first_train = trains_schedule[first_id]
                second_train = trains_schedule[second_id]
                
                hours= (second_train["departure_time"]+ second_train["time_duration"] / 60) - first_train["departure_time"]
                total_dur = int(hours * 60)
                res.append([trip, total_dur] )
    res.sort(key = lambda x: (x[1],-len(x[0])))
    
    return res
