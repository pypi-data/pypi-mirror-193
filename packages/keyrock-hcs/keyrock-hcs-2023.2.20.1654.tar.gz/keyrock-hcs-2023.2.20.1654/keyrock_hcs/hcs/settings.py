import logging
logger = logging.getLogger(__name__)

from . import exc


def int_none(val):
    try:
        return int(val)
    except:
        return None


def local_to_tracked(obj_id, settings_local, depth=0):
    settings_tracked = {
        'd': depth,     # Depth
        'r': obj_id,    # Root/Origin Id (where it first appeared)
        'p': obj_id,    # Previous Id (where it was previously set)
        'c': obj_id,    # Current Id (where it is currently set)
        # Optional:
        # 'v': Effective Value (if leaf)
        # 'pv': Previous Value (if leaf)
        # 'dict': Dict Value (if not leaf)
        # 'list': List Value (if not leaf)
    }

    if isinstance(settings_local, dict):
        setting_dict = {}
        for key, val in settings_local.items():
            setting_dict[key] = local_to_tracked(obj_id, val, depth)
        settings_tracked['dict'] = setting_dict
    elif isinstance(settings_local, list):
        setting_list = []
        for val in settings_local:
            setting_list.append(local_to_tracked(obj_id, val, depth))
        settings_tracked['list'] = setting_list
    else:
        settings_tracked['v'] = settings_local  # Effective Value
        settings_tracked['pv'] = settings_local # Parent Value

    return settings_tracked


def tracked_to_local(settings_tracked):
    if settings_tracked is None:
        return None

    if 'v' in settings_tracked:
        return settings_tracked['v']
    elif 'dict' in settings_tracked:
        settings_local = {}
        for key, val_tracked in settings_tracked['dict'].items():
            settings_local[key] = tracked_to_local(val_tracked)
        return settings_local
    elif 'list' in settings_tracked:
        settings_local = []
        for val_tracked in settings_tracked['list']:
            settings_local.append(tracked_to_local(val_tracked))
        return settings_local
    else:
        raise exc.InvalidTrackedSetting(settings_tracked)


def merge_tracked_settings(settings_parent, settings_child):
    '''
    Include all the parent settings
      merge with child settings if they exist
    Include the child settings which don't already exist in the parent
      theoretically could return settings_merged from every branch
    '''

    if settings_child is None:
        settings_child = {}

    settings_merged = {
        'r': settings_parent['r'],
    }

    # Simple value settings
    if 'v' in settings_parent:
        if 'v' in settings_child:
            settings_merged.update({
                'c': settings_child['c'],   # Child Id
                'd': settings_child['d'],   # Depth
                'p': settings_parent['c'],  # Parent Id
                'pv': settings_parent['v'], # Parent Value
                'v': settings_child['v'],   # Child Value
            })
        else:
            settings_merged.update({
                'c': settings_parent['c'],   # Child Id
                'd': settings_parent['d'],   # Depth
                'p': settings_parent['c'],   # Parent Id
                'pv': settings_parent['v'],  # Parent Value
                'v': settings_parent['v'],   # Child Value
            })
    elif 'v' in settings_child:
        settings_merged = settings_child
    else:
        # Handle dictionary (still record parent and child ids, and origin depth)
        settings_merged.update({
            'p': settings_parent['c'],                          # Parent Id
            'c': settings_child.get('c', settings_parent['c']), # Child Id
            'd': settings_child.get('d', settings_parent['d']), # Origin depth
        })

    # Dict settings
    if 'dict' in settings_parent:
        # Merge the tracked data from each dict entry
        child_dict = settings_child.get('dict', {})
        merged_dict = {}
        for key, parent_entry in settings_parent['dict'].items():
            child_entry = child_dict.get(key)
            merged_dict[key] = merge_tracked_settings(
                parent_entry,
                child_entry
            )
        settings_merged['dict'] = merged_dict
    # In case only the child has this dict
    if 'dict' in settings_child:
        merged_dict = settings_merged.setdefault('dict', {})
        for key, child_entry in settings_child['dict'].items():
            if key not in merged_dict:
                merged_dict[key] = child_entry

    # List settings
    if 'list' in settings_parent:
        settings_merged['list'] = settings_parent['list']
    if 'list' in settings_child:
        settings_merged.setdefault('list', []).extend(settings_child['list'])

    return settings_merged
