class ObjectNotFoundError(Exception):
    def __init__(self, obj_id):
        msg = 'Object not found: {0}'.format(obj_id)
        super().__init__(msg)

class AccessDenied(Exception):
    def __init__(self, obj_id):
        msg = 'Operation prohibited on: {0}'.format(obj_id)
        super().__init__(msg)

class ObjectPendingDeletion(Exception):
    def __init__(self, obj_id):
        msg = 'Object pending deletion: {0}'.format(obj_id)
        super().__init__(msg)

class InvalidTrackedSetting(Exception):
    def __init__(self, tracked_setting):
        msg = repr(tracked_setting)
        super().__init__(msg)

class VersionConflictError(Exception):
    def __init(self, old_ver, new_ver):
        msg = 'Modified version mismatch: {0}:{1}'.format(old_ver, new_ver)
        super().__init__(msg)
