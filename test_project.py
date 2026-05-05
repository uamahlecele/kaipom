"""Lana ng'zofaka amaTest ami."""

from project import countdown_timer, parsing_ama_argument

import pytest

def test_count_down_timer_incorrect_input():
   with pytest.raises(TypeError):
      countdown_timer("cat","dog")


#How to test argeparse commands
def test_study_command_with_hour():
    args = parsing_ama_argument(['study', '50', '--hour', '3'])
    assert args.command == 'study'
    assert args.minutes == 50
    assert args.hour == 3
    

def test_study_command_no_hour():
   args = parsing_ama_argument(['study','25'])

   assert args.command == 'study'
   assert args.minutes == 25
   assert args.hour == 1
