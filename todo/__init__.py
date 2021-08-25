import configparser
from datetime import datetime
import todoist

config = configparser.ConfigParser()
config.read("config.ini")
_username = config.get('todoist_config', 'username')
_password = config.get('todoist_config', 'password')
_api = todoist.TodoistAPI()
_api.user.login(_username, _password)
_status = None
_projects = None
_tasks = None
_sections = None
_due_today = []


def refresh():
    global _status
    _status = _api.sync()
    get_projects()
    get_sections()


def get_projects():
    global _status, _projects
    _projects = {}
    for data in _status['projects']:
        _projects[data['id']] = data


def get_sections():
    global _status, _sections
    _sections = {}
    for section in _status['sections']:
        _sections[section['id']] = section


def is_due_today(datestr):
    formats = ["%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"]
    today = datetime.today().date()
    for fmt in formats:
        try:
            return datetime.strptime(datestr, fmt).date() == today
        except ValueError as e:
            pass
    return False


def format_time(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S").strftime("%I:%M%p")
    except ValueError as e:
        return ""


def format_task(item):
    task = {'title': item['content'], 'is_recurring': item['due']['is_recurring'],
            'due_time': format_time(item['due']['date']),
            'project_name': _projects[item['project_id']]['name']}
    if item['section_id']:
        task['section_name'] = _sections[item['section_id']]['name']
    return task


def get_items():
    global _due_today
    refresh()
    for item in _status['items']:
        print(item)
        if item['due'] and is_due_today(item['due']['date']):
            _due_today.append(format_task(item))
    print(_due_today)
    return _due_today

# TODO - Add Logic to handle partial updates
# TODO - Add Logic to handle task complete event
# TODO - Add Unit Tests
