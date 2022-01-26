class DBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'soccer_info':
            return 'mini'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'soccer_info':
            return 'mini'
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'soccer_info' or \
            obj2._meta.app_label == 'soccer_info':
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'soccer_info':
            return db == 'mini'
        return None