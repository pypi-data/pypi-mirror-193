from termcolor import colored

from django.db import models
from django.utils import timezone

LEVELER = '│  '
BRANCH_MARK = '`-'
INFO = colored('[·] ', 'cyan')
SUCCESS = colored('[·] ', 'green')
ERROR = colored('[·] ', 'red')

class Procedure(models.Model):
    c_at = models.DateTimeField(default=timezone.now)

    root = models.ForeignKey('self', related_name='nodes', null=True, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='children', null=True, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    parameters = models.JSONField(default=dict)
    results = models.JSONField(null=True)

    name = models.TextField(default=str)
    environ = models.JSONField(default=dict)
    executed = models.BooleanField(default=False)
    logs = models.TextField(default=str)
    exception = models.TextField(null=True)

    def __str__(self):
        return self.name

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if type is None:
            self.executed = True
            self.save(update_fields=['executed'])
        return False

    def sub(self, name):
        (sub_procedure, _) = self.children.get_or_create(
            name=name,
            defaults={'root': self.root, 'level': self.level+1}
        )
        return sub_procedure

    def run(self, task, *args, **kwargs):
        return task(*args, **kwargs)

    def get(self, variable, default=None):
        return self.environ.get(variable, default)

    def set(self, variable, value, commit=True):
        self.environ[variable] = value
        if commit:
            self.save(update_fields=['variable'])

    def log(self, text, commit=True, new_line=True):
        self._display_line(text)
        self.logs += text
        if new_line:
            self.logs += '\n'
        if commit:
            self.save(update_fields=['logs'])

    def _display_line(self, text):
        empty_holder = ' '+(self.level+1) * LEVELER
        print(empty_holder, text)

    def _display_procedure(self, replay=False):
        if self.executed:
            if replay:
                name = colored(f'[·] {self.name}', 'green')
            else:
                name = colored(f'[·] {self.name} (Skipped)', 'green')
        elif not replay:
            if self.exception:
                self.exception = None
                self.logs = ''
                self.save(update_fields=['exception', 'logs'])
                name = colored(f'[·] {self.name} (Retry)', 'yellow')
            else:
                name = colored(f'[·] {self.name}', 'cyan')
        else:
            name = colored(f'[·] {self.name}', 'red')
        if self.level == 0:
            place_holder = ''
        else:
            place_holder = ' '+(self.level-1) * LEVELER + BRANCH_MARK

        print(place_holder + name)

    def _display_error(self, text):
        empty_holder = ' ' + (self.level+1) * LEVELER
        print(empty_holder, colored(text, 'red'))

    def replay(self):
        self._display_procedure(replay=True)
        if self.logs:
            for log in self.logs.split('\n'):
                if log:
                    self._display_line(log)
                elif self.parent and not self.exception:
                    self.parent._display_line('')

        if self.exception:
            self._display_error(self.exception)

        for subprocedure in self.children.order_by('c_at'):
            subprocedure.replay()
