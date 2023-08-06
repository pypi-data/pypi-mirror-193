
class ProcedureWrapper:
    '''
    @procedure_task
    def task():

    The procedure_task decorator will wrap the task as a ProcedureWrapper, allowing following usecases
    task() # direct run
    task.run() # same as above, more readable
    task.auto_retry(interval=10, max_retry=20).run()
    @task.clean_up # clean up actions if a task failed
    '''
    def __init__(self, task):
        self.clean_up_function = None
        self.task = task

    def __str__(self):
        return f'Procedure task {self.task}'

    def __call__(self, procedure, *args, **kwargs):
        procedure._display_procedure()
        if procedure.executed:
            return procedure.results
        procedure.parameters = {
            'args': args,
            'kwargs': kwargs
        }
        try:
            results = self.task(procedure, *args, **kwargs)
        except Exception as e:
            if not e.__dict__.get('__PROCEDURE_RESOLVED'):
                procedure._display_error(str(e))
                procedure.exception = str(e)
                procedure.save(update_fields=['exception'])
                e.__dict__['__PROCEDURE_RESOLVED'] = True
            if self.clean_up_function:
                self.clean_up_function(procedure)
            raise e

        procedure.results = results
        procedure.executed = True
        procedure.save(update_fields=['results', 'executed'])
        return results

    def clean_up(self, task):
        self.clean_up_function
        return task


def procedure_task(task):
    return ProcedureWrapper(task)
