# -*- coding: utf-8 -*-


def unique_result(array):
    unique_results = []
    for obj in array:
        if obj.game.gb_id not in unique_results:
            unique_results.append(obj)
    return unique_results
