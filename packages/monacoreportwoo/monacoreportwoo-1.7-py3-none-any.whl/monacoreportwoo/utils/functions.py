from collections import namedtuple
from datetime import datetime
from typing import Dict, List, Tuple

from texttable import Texttable

from .exceptions import (CustomFileNameException, CustomFormatDataException,
                         CustomIncorrectTimeException, CustomNotFoundException)
from .utilitys import import_folder, read_file


def create_abbreviations_data(files_full_path: Dict[str, str]) -> List[List[str]]:
    """Create abbreviation data from abbreviation file"""
    file_names = ["start", "end", "abbreviations"]
    if not all(item in files_full_path.keys() for item in file_names):
        raise CustomFileNameException(
            f"folder should contain following files: ('start.log', 'end.log', 'abbreviations.txt)'"
        )
    abbreviations_file = read_file(files_full_path["abbreviations"])
    riders_information_data = [element.split('_') for element in abbreviations_file]
    for rider in riders_information_data:
        for rider_item in rider:
            if not rider_item.isascii():
                raise CustomFormatDataException(
                    f"'{rider_item}' has an incorrect format, must be ASCII"
                )
    return riders_information_data


def create_riders_datetime_data(files_path: Dict[str, str]) -> Tuple[Dict[str, list], Dict[str, datetime]]:
    """Convert log files to dictionary with datetime objects"""
    datetime_format = "%Y-%m-%d %H:%M:%S.%f"
    start_file = read_file(files_path["start"])
    end_file = read_file(files_path["end"])
    prepared_start = {
        key[:3]: [datetime.strptime(key[3:].replace("_", " "), datetime_format)] for key in start_file
    }
    prepared_end = {
        key[:3]: datetime.strptime(key[3:].replace("_", " "), datetime_format) for key in end_file
    }
    return prepared_start, prepared_end


def join_start_and_finish_time(start_data: Dict[str, list], end_data: Dict[str, datetime]) -> Dict[str, list]:
    """Join start and finish times for all riders"""
    joined_rider_times = start_data.copy()
    for element in end_data:
        joined_rider_times[element].append(end_data[element])
    return joined_rider_times


def merge_logs_with_abbreviations(prepared_data: Dict[str, list], abbreviations_data: list) -> List[tuple]:
    """Join prepared riders data and abbreviations data sorted by ASC"""
    calculated_times = {}
    final_report_data = []
    for element in prepared_data:
        start_time, finish_time = prepared_data[element][0], prepared_data[element][1]
        if start_time > finish_time:

            raise CustomIncorrectTimeException(
                f"Time incorrect, start time: {start_time} is longer than the finish time: {finish_time}"
            )
        calculated_times.update({element: finish_time - start_time})
    for abbreviation, name, car in abbreviations_data:
        best_race_time = calculated_times.get(abbreviation)
        full_rider_data = namedtuple(abbreviation, "name car best_time")
        final_report_data.append(full_rider_data(name, car, best_race_time))
    return sorted(final_report_data, key=lambda time: time.best_time)


def create_table_report(riders_data: List[namedtuple], descending=False, rider_name=False) -> Texttable:
    """Create final table report as Texttable object"""
    final_table = Texttable()
    column_names = ['Number', 'Rider Name', 'Car', 'Best Time']
    delimiter_line = ['*********', '******************', '*************************', '************']
    delimiter_position = 15
    rider_position = 1

    if rider_name:
        rider_names = [name.name for name in riders_data]
        if rider_name not in rider_names:
            raise CustomNotFoundException(
                f"Rider name: '{rider_name}' does not exist"
            )
        for rider in riders_data:
            if rider.name == rider_name:
                best_rider_time = str(rider.best_time)[2:]
                final_table.add_rows([column_names, [rider_position, rider.name, rider.car, best_rider_time]])
    else:
        if descending:
            riders_data = sorted(riders_data, key=lambda x: x.best_time, reverse=True)
            delimiter_position = 4
        for rider in riders_data:
            best_rider_time = str(rider.best_time)[2:]
            final_table.add_rows([column_names, [rider_position, rider.name, rider.car, best_rider_time]])
            if rider_position == delimiter_position:
                final_table.add_rows([column_names, delimiter_line])
            rider_position += 1

    return final_table.draw()


def build_report(folder_path: str, descending=None, rider_name=None) -> Texttable:
    """Function for build final table report"""
    files_full_path = import_folder(folder_path)
    abbreviations_data = create_abbreviations_data(files_full_path)
    start_data, end_data = create_riders_datetime_data(files_full_path)
    joined_rider_times = join_start_and_finish_time(start_data, end_data)
    riders_data_sorted_acs = merge_logs_with_abbreviations(joined_rider_times, abbreviations_data)
    final_report = create_table_report(riders_data_sorted_acs, descending, rider_name)
    return final_report


def print_report(folder_path: str, rider_name=None, desc=None):
    """Function for print final table report"""
    print(build_report(folder_path, rider_name=rider_name, descending=desc))
