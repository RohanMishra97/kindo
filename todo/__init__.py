import configparser
from datetime import datetime
import todoist

config = configparser.ConfigParser()
config.read("config.ini")
_username = config.get('todoist_config', 'username')
_password = config.get('todoist_config', 'password')
_api = todoist.TodoistAPI()
_api.user.login(_username, _password)
_keys = ['items', 'labels', 'projects', 'sections']
_state = {key: {} for key in _keys}


def _refresh():
    global _state
    _status = _api.sync()
    for k in _keys:
        for x in _status[k]:
            _state[k][x['id']] = x


def _is_due_today(datestr):
    formats = ["%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"]
    today = datetime.today().date()
    for fmt in formats:
        try:
            return datetime.strptime(datestr, fmt).date() == today
        except ValueError as e:
            pass
    return False


def _format_time(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S").strftime("%I:%M%p")
    except ValueError as e:
        return ""


def _format_task(item):
    global _state
    task = {'id': item['id'],
            'title': item['content'],
            'due': _format_time(item['due']['date']),
            'is_recurring': item['due']['is_recurring'],
            'project_name': _state['projects'][item['project_id']]['name']}
    if item['section_id']:
        task['section_name'] = _state['sections'][item['section_id']]['name']
    return task


def get_items():
    global _state
    _refresh()
    tasks_due_today = []
    for k, v in _state['items'].items():
        if v['due'] and _is_due_today(v['due']['date']):
            tasks_due_today.append(_format_task(v))
    return tasks_due_today

# TODO - Add Logic to handle partial updates
# TODO - Add Logic to handle task complete event
# TODO - Add Unit Tests
